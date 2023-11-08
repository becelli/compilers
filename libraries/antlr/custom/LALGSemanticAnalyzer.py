from __future__ import annotations
from re import I
from typing import Literal, Optional
from libraries.antlr.LALGParser import LALGParser
from libraries.antlr.LALGParserVisitor import LALGParserVisitor
from libraries.antlr.custom.LALGErrorListener import LALGErrorListener
from dataclasses import dataclass
from abc import ABC


VariableType = Literal["int", "boolean"]


@dataclass
class Symbol(ABC):
    name: str


@dataclass
class VariableSymbol(Symbol):
    type: VariableType
    is_used: bool = False


@dataclass
class ProcedureParamSymbol(Symbol):
    type: VariableType
    is_used: bool = False


@dataclass
class ProcedureSymbol(Symbol):
    params: list[VariableSymbol]
    is_used: bool = False


class Scope:
    def __init__(self, scope_name: str, enclosing_scope: Optional[Scope] = None):
        self.scope_name = scope_name
        self.enclosing_scope: Optional[Scope] = enclosing_scope
        self.symbols: dict[str, Symbol] = {}

    def define(self, symbol: Symbol):
        self.symbols[symbol.name] = symbol

    def resolve(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)


class LALGSemanticAnalyzer(LALGParserVisitor):
    def __init__(self, errorListener: LALGErrorListener):
        self.current_scope = Scope("global")
        self.errorListener = errorListener

    def enterScope(self, scope_name: str):
        scope = Scope(scope_name, self.current_scope)
        self.current_scope = scope

    def exitScope(self):
        if self.current_scope.enclosing_scope is not None:
            self.current_scope = self.current_scope.enclosing_scope

    def visitProgram(self, ctx: LALGParser.ProgramContext):
        self.visitChildren(ctx)
        self.exitScope()

    def visitVariableDeclaration(self, ctx: LALGParser.VariableDeclarationContext):
        var_type: VariableType = ctx.type_().getText()  # type: ignore
        identifiers = ctx.identifierList().IDENTIFIER()  # type: ignore
        for identifier in identifiers:
            variable_name: str = identifier.getText()
            if self.current_scope.resolve(variable_name):
                self.errorListener.semanticError(
                    identifier.symbol.line,
                    identifier.symbol.column,
                    f"Variable {variable_name} already declared in the {self.current_scope.scope_name} scope",
                )
            else:
                self.current_scope.define(VariableSymbol(variable_name, var_type))

        self.visitChildren(ctx)

    def visitProcedureDeclaration(self, ctx: LALGParser.ProcedureDeclarationContext):
        proc_name: str = ctx.IDENTIFIER().getText()  # type: ignore
        if self.current_scope.resolve(proc_name):
            identifier = ctx.IDENTIFIER()
            self.errorListener.semanticError(
                identifier.symbol.line,  # type: ignore
                identifier.symbol.column,  # type: ignore
                f"Procedure {proc_name} already declared",
            )
        else:
            self.enterScope(proc_name)
            assert self.current_scope.enclosing_scope is not None
            self.visitChildren(ctx)
            param_condition = lambda symbol: isinstance(symbol, ProcedureParamSymbol)
            collected_symbols = self.current_scope.symbols.values()
            symbol = ProcedureSymbol(proc_name, list(filter(param_condition, collected_symbols)))  # type: ignore
            self.current_scope.enclosing_scope.define(symbol)
            self.exitScope()

    def visitFormalParameterList(self, ctx: LALGParser.FormalParameterListContext):
        params_section: list = ctx.formalParameterSection()  # type: ignore
        for section in params_section:
            var_type: VariableType = section.type_().getText()
            identifiers: list = section.identifierList().IDENTIFIER()
            for identifier in identifiers:
                variable_name: str = identifier.getText()
                symbol = self.current_scope.resolve(variable_name)
                if symbol is not None:
                    line, column = identifier.symbol.line, identifier.symbol.column
                    msg = f"Param {variable_name} is duplicated in the procedure {self.current_scope.scope_name}"
                    self.errorListener.semanticError(line, column, msg)
                else:
                    symbol = ProcedureParamSymbol(variable_name, var_type)
                    self.current_scope.define(symbol)

    def visitProcedureCallStatement(
        self, ctx: LALGParser.ProcedureCallStatementContext
    ):
        proc_name: str = ctx.IDENTIFIER().getText()  # type: ignore
        proc_symbol = self.current_scope.resolve(proc_name)
        if proc_symbol is None or not isinstance(proc_symbol, ProcedureSymbol):
            identifier = ctx.IDENTIFIER()
            line, column = identifier.symbol.line, identifier.symbol.column  # type: ignore
            msg = f"Procedure {proc_name} not declared"
            return self.errorListener.semanticError(line, column, msg)

        proc_expression_list: list | None = ctx.expressionList()
        if proc_expression_list:
            expressions_list: list = proc_expression_list.expression()
            expression_list_length = len(expressions_list)
            proc_params = proc_symbol.params
            proc_params_length = len(proc_params) if proc_params else 0
            if proc_params_length != expression_list_length:
                self.errorListener.semanticError(
                    ctx.IDENTIFIER().symbol.line,  # type: ignore
                    ctx.IDENTIFIER().symbol.column,  # type: ignore
                    f"Procedure {proc_name} expected {proc_params_length} parameters, got {expression_list_length}",
                )

            for param in zip(proc_params, expressions_list):
                param_symbol, expression = param
                expression_type = self.get_expression_type(expression)
                if expression_type != param_symbol.type:
                    self.errorListener.semanticError(
                        ctx.IDENTIFIER().symbol.line,  # type: ignore
                        ctx.IDENTIFIER().symbol.column,  # type: ignore
                        f"Procedure {proc_name} expected {param_symbol.type} parameter, got {expression_type}",
                    )

        else:
            if len(proc_symbol.params) > 0:
                self.errorListener.semanticError(
                    ctx.IDENTIFIER().symbol.line,  # type: ignore
                    ctx.IDENTIFIER().symbol.column,  # type: ignore
                    f"Procedure {proc_name} expected {len(proc_symbol.params)} parameters, got 0",
                )

    def get_expression_type(
        self, expression: LALGParser.ExpressionContext
    ) -> VariableType:
        if expression.relationalOperator() is not None:
            return "boolean"

        simple_expression: LALGParser.SimpleExpressionContext = expression.simpleExpression()[0]  # type: ignore

        # TODO: How to extract the type of the expression, looking inside "simpleExpression"?
        return "int"

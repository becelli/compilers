from __future__ import annotations
from re import I
import re
from typing import Literal, Optional
from libraries.antlr.LALGParser import LALGParser
from libraries.antlr.LALGParserVisitor import LALGParserVisitor
from libraries.antlr.custom.LALGErrorListener import LALGErrorListener
from dataclasses import dataclass
from abc import ABC


VariableType = Literal["int", "boolean", "real", "unknown"]


@dataclass
class Position:
    line: int
    column: int

    @staticmethod
    def from_symbol(symbol):
        return Position(symbol.line, symbol.column)


@dataclass
class Symbol(ABC):
    name: str
    source: Position
    is_used = False


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

    def find(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)


class TypeExtractor:
    def __init__(self, scope: Scope, listener: LALGErrorListener):
        self.scope = scope
        self.listener = listener

    def from_primary_expression(
        self, primary_expression: LALGParser.PrimaryExpressionContext
    ) -> VariableType:
        if primary_expression.literal():
            return "boolean"
        elif primary_expression.number():
            return "int" if primary_expression.number().INT() else "real"  # type: ignore
        elif primary_expression.variable():
            identifier = primary_expression.variable().IDENTIFIER()  # type: ignore
            variable_name = identifier.getText()
            symbol = self.scope.find(variable_name)
            if symbol is None or not (
                isinstance(symbol, VariableSymbol)
                or isinstance(symbol, ProcedureParamSymbol)
            ):
                line, column = identifier.symbol.line, identifier.symbol.column
                msg = f"Variable {variable_name} not declared"
                self.listener.semanticError(line, column, msg)
                return "unknown"
            else:
                symbol.is_used = True
                return symbol.type

        expression = primary_expression.expression()  # type: ignore
        assert expression is not None
        return self.from_expression(expression)

    def from_unary_expression(
        self, unary_expression: LALGParser.UnaryExpressionContext
    ) -> VariableType:
        type = self.from_primary_expression(unary_expression.primaryExpression())  # type: ignore
        unary_operator = unary_expression.unaryOperator()
        if unary_operator is None:
            return type

        unary_for_number = unary_operator.SUM() or unary_operator.SUB()
        expression_is_number = type == "int" or type == "real"
        if unary_for_number and expression_is_number:
            return type
        elif unary_operator.NOT() and type == "boolean":
            return type
        else:
            line, column = unary_operator.start.line, unary_operator.start.column
            msg = f"Invalid unary operator {unary_operator.getText()} for {type}"
            self.listener.semanticError(line, column, msg)
            return "unknown"

    def from_multiplicative_expression(
        self, multiplicative_expression: LALGParser.MultiplicativeExpressionContext
    ) -> VariableType:
        unary_expression = multiplicative_expression.unaryExpression()
        assert isinstance(unary_expression, list)
        type = self.from_unary_expression(unary_expression[0])  # type: ignore
        if len(unary_expression) == 1:
            return type

        type_is_boolean = type == "boolean"
        type_is_int = type == "int"
        for i, expression in enumerate(unary_expression[1:]):
            expression_type = self.from_unary_expression(expression)
            if type != expression_type:
                line, column = expression.start.line, expression.start.column
                msg = f"Unmatched types in expression. Got {type} and {expression_type}"
                self.listener.semanticError(line, column, msg)
                return "unknown"

            # Multiplicative operator
            operator = multiplicative_expression.multiplicativeOperator(i)
            assert operator is not None
            operator_is_and = operator.AND()
            operator_is_div = operator.DIV()
            if type_is_boolean and not operator_is_and:
                line, column = operator.start.line, operator.start.column
                msg = f"Expected AND operator, got {operator.getText()}"
                self.listener.semanticError(line, column, msg)
                return "unknown"
            elif not type_is_boolean and operator_is_and:
                line, column = operator.start.line, operator.start.column
                msg = f"Expected arithmetic operator, got {operator.getText()}"
                self.listener.semanticError(line, column, msg)
                return "unknown"
            
            if type_is_int and operator_is_div:
                line, column = operator.start.line, operator.start.column
                msg = f"The {operator.getText()} is only valid for real numbers. Use the DIV operator instead"
                self.listener.semanticError(line, column, msg)
                return "unknown"

        return type

    def from_additive_expression(
        self, additive_expression: LALGParser.AdditiveExpressionContext
    ) -> VariableType:
        multiplicative_expression = additive_expression.multiplicativeExpression()
        assert isinstance(multiplicative_expression, list)
        type = self.from_multiplicative_expression(multiplicative_expression[0])
        if len(multiplicative_expression) == 1:
            return type

        type_is_boolean = type == "boolean"
        for i, expression in enumerate(multiplicative_expression[1:]):
            expression_type = self.from_multiplicative_expression(expression)
            if type != expression_type:
                line, column = expression.start.line, expression.start.column
                msg = f"Expected {type} expression, got {expression_type}"
                self.listener.semanticError(line, column, msg)
                return "unknown"

            operator = additive_expression.additiveOperator(i)
            assert operator is not None
            operator_is_or = operator.OR()
            if type_is_boolean and not operator_is_or:
                line, column = operator.start.line, operator.start.column
                msg = f"Expected OR operator, got {operator.getText()}"
                self.listener.semanticError(line, column, msg)
                return "unknown"
            elif not type_is_boolean and operator_is_or:
                line, column = operator.start.line, operator.start.column
                msg = f"Expected arithmetic operator, got {operator.getText()}"
                self.listener.semanticError(line, column, msg)
                return "unknown"

        return type

    def from_expression(self, expression: LALGParser.ExpressionContext) -> VariableType:
        additive_expression = expression.additiveExpression()
        assert isinstance(additive_expression, list)
        type = self.from_additive_expression(additive_expression[0])
        if len(additive_expression) == 1:
            return type

        for expression in additive_expression[1:]:
            expression_type = self.from_additive_expression(expression)  # type: ignore
            if type != expression_type:
                line, column = expression.start.line, expression.start.column  # type: ignore
                msg = f"Expected {type} expression, got {expression_type}"
                self.listener.semanticError(line, column, msg)
                return "unknown"

        # At this point, if there are two additive expressions, they have a relational operator between them
        return "boolean"


class LALGSemanticAnalyzer(LALGParserVisitor):
    def __init__(self, errorListener: LALGErrorListener):
        self.current_scope = Scope("global")
        self.errorListener = errorListener
        self.type_extractor = TypeExtractor(self.current_scope, errorListener)

    def enterScope(self, scope_name: str):
        scope = Scope(scope_name, self.current_scope)
        self.type_extractor.scope = scope
        self.current_scope = scope

    def exitScope(self):
        if self.current_scope.enclosing_scope is not None:
            self.type_extractor.scope = self.current_scope.enclosing_scope
            self.current_scope = self.current_scope.enclosing_scope

    def visitProgram(self, ctx: LALGParser.ProgramContext):
        self.visitChildren(ctx)
        self.exitScope()

    def visitVariableDeclaration(self, ctx: LALGParser.VariableDeclarationContext):
        var_type: VariableType = ctx.type_().getText()  # type: ignore
        identifiers: list = ctx.identifierList().IDENTIFIER()  # type: ignore
        for identifier in identifiers:
            variable_name: str = identifier.getText()
            if self.current_scope.find(variable_name):
                self.errorListener.semanticError(
                    identifier.symbol.line,
                    identifier.symbol.column,
                    f"Variable {variable_name} already declared in the {self.current_scope.scope_name} scope",
                )
            else:
                self.current_scope.define(
                    VariableSymbol(
                        variable_name, Position.from_symbol(identifier.symbol), var_type
                    )
                )

    def visitProcedureDeclaration(self, ctx: LALGParser.ProcedureDeclarationContext):
        proc_name: str = ctx.IDENTIFIER().getText()  # type: ignore
        if self.current_scope.find(proc_name):
            identifier = ctx.IDENTIFIER()
            self.errorListener.semanticError(
                identifier.symbol.line,  # type: ignore
                identifier.symbol.column,  # type: ignore
                f"Procedure {proc_name} already declared",
            )
        else:
            self.enterScope(scope_name=proc_name)
            assert self.current_scope.enclosing_scope is not None
            self.visitChildren(ctx)

            param_condition = lambda symbol: isinstance(symbol, ProcedureParamSymbol)
            collected_symbols = self.current_scope.symbols.values()
            identifier = ctx.IDENTIFIER()
            symbol = ProcedureSymbol(
                proc_name,
                Position.from_symbol(identifier.symbol),  # type: ignore
                list(filter(param_condition, collected_symbols)),  # type: ignore
            )  # type: ignore
            self.current_scope.enclosing_scope.define(symbol)
            self.exitScope()

    def visitFormalParameterList(self, ctx: LALGParser.FormalParameterListContext):
        params_section: list = ctx.formalParameterSection()  # type: ignore
        for section in params_section:
            var_type: VariableType = section.type_().getText()
            identifiers: list = section.identifierList().IDENTIFIER()
            for identifier in identifiers:
                variable_name: str = identifier.getText()
                symbol = self.current_scope.find(variable_name)
                if symbol is not None:
                    line, column = identifier.symbol.line, identifier.symbol.column
                    msg = f"Param {variable_name} is duplicated in the procedure {self.current_scope.scope_name}"
                    self.errorListener.semanticError(line, column, msg)
                else:
                    symbol = ProcedureParamSymbol(
                        variable_name, Position.from_symbol(identifier.symbol), var_type
                    )
                    self.current_scope.define(symbol)

    def visitProcedureCallStatement(
        self, ctx: LALGParser.ProcedureCallStatementContext
    ):
        proc_name: str = ctx.IDENTIFIER().getText()  # type: ignore
        proc_symbol = self.current_scope.find(proc_name)
        if proc_symbol is None or not isinstance(proc_symbol, ProcedureSymbol):
            identifier = ctx.IDENTIFIER()
            line, column = identifier.symbol.line, identifier.symbol.column  # type: ignore
            msg = f"Procedure {proc_name} not declared"
            return self.errorListener.semanticError(line, column, msg)
        else:
            proc_symbol.is_used = True

        proc_expression_list: list | None = ctx.expressionList()
        if proc_expression_list is not None:
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

            types_from_proc_params = [param.type for param in proc_params]
            types_from_expression_list = [
                self.type_extractor.from_expression(expression)
                for expression in expressions_list
            ]

            for i, (proc_params_type, expression_type) in enumerate(
                zip(types_from_proc_params, types_from_expression_list)
            ):
                if proc_params_type != expression_type:
                    self.errorListener.semanticError(
                        expressions_list[i].start.line,
                        expressions_list[i].start.column,
                        f"Procedure {proc_name} expected {proc_params_type} parameter, got {expression_type}",
                    )

        else:
            if len(proc_symbol.params) > 0:
                self.errorListener.semanticError(
                    ctx.IDENTIFIER().symbol.line,  # type: ignore
                    ctx.IDENTIFIER().symbol.column,  # type: ignore
                    f"Procedure {proc_name} expected {len(proc_symbol.params)} parameters, got 0",
                )

    def visitVariable(self, ctx: LALGParser.VariableContext):
        variable_name = ctx.IDENTIFIER().getText()  # type: ignore
        symbol = self.current_scope.find(variable_name)
        if symbol is None or not (
            isinstance(symbol, VariableSymbol)
            or isinstance(symbol, ProcedureParamSymbol)
        ):
            identifier = ctx.IDENTIFIER()
            line, column = identifier.symbol.line, identifier.symbol.column  # type: ignore
            msg = f"Variable {variable_name} not declared"
            return self.errorListener.semanticError(line, column, msg)

        symbol.is_used = True

    def visitAssignmentStatement(self, ctx: LALGParser.AssignmentStatementContext):
        variable = ctx.variable()
        assert variable is not None
        variable_name: str = variable.IDENTIFIER().getText()
        symbol = self.current_scope.find(variable_name)
        if symbol is None or not (
            isinstance(symbol, VariableSymbol)
            or isinstance(symbol, ProcedureParamSymbol)
        ):
            identifier = ctx.IDENTIFIER()  # type: ignore
            line, column = identifier.symbol.line, identifier.symbol.column
            msg = f"Variable {variable_name} not declared"
            return self.errorListener.semanticError(line, column, msg)

        symbol.is_used = True

        expression = ctx.expression()
        self.visit(expression)
        assert expression is not None
        expression_type = self.type_extractor.from_expression(expression)
        if symbol.type != expression_type:
            self.errorListener.semanticError(
                variable.IDENTIFIER().symbol.line,  # type: ignore
                variable.IDENTIFIER().symbol.column,  # type: ignore
                f"Variable {variable_name} expected {symbol.type} type, got {expression_type}",
            )

    def visitConditionalStatement(self, ctx: LALGParser.ConditionalStatementContext):
        expression = ctx.expression()
        assert expression is not None
        expression_type = self.type_extractor.from_expression(expression)
        if expression_type != "boolean":
            self.errorListener.semanticError(
                ctx.IF().symbol.line,  # type: ignore
                ctx.IF().symbol.column,  # type: ignore
                f"Expected boolean expression, got {expression_type}",
            )

        self.visitChildren(ctx)

    def visitLoopStatement(self, ctx: LALGParser.LoopStatementContext):
        expression = ctx.expression()
        self.visitChildren(ctx)
        assert expression is not None
        expression_type = self.type_extractor.from_expression(expression)
        if expression_type != "boolean":
            self.errorListener.semanticError(
                ctx.WHILE().symbol.line,  # type: ignore
                ctx.WHILE().symbol.column,  # type: ignore
                f"Expected boolean expression, got {expression_type}",
            )

    def visitBlock(self, ctx: LALGParser.BlockContext):
        self.visitChildren(ctx)
        for symbol in self.current_scope.symbols.values():
            if not symbol.is_used:
                symbol_family: str  # Deve ter uma forma melhor de fazer isso
                if isinstance(symbol, VariableSymbol):
                    symbol_family = "Variable"
                elif isinstance(symbol, ProcedureParamSymbol):
                    symbol_family = "Parameter"
                elif isinstance(symbol, ProcedureSymbol):
                    symbol_family = "Procedure"
                else:
                    symbol_family = "Unknown"
                self.errorListener.semanticError(
                    symbol.source.line,
                    symbol.source.column,
                    f"{symbol_family} {symbol.name} declared but not used",
                )

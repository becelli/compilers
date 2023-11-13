from __future__ import annotations
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

    def resolve(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)


class TypeExtractor:
    def __init__(self, scope: Scope, listener: LALGErrorListener):
        self.scope = scope
        self.listener = listener

    def from_factor(self, factor: LALGParser.FactorContext) -> VariableType:
        # Check if the factor is a variable
        if factor.variable():
            # Retrieve and return the variable's type from the symbol table
            identifier = factor.variable().IDENTIFIER()  # type: ignore
            variable_name = identifier.getText()
            symbol = self.scope.resolve(variable_name)
            if symbol is None or not (
                isinstance(symbol, VariableSymbol)
                or isinstance(symbol, ProcedureParamSymbol)
            ):
                self.listener.semanticError(
                    identifier.symbol.line,  # type: ignore
                    identifier.symbol.column,  # type: ignore
                    f"Variable {variable_name} not declared",
                )
            else:
                symbol.is_used = True
                return symbol.type
        # Check if the factor is a number
        elif factor.number():
            if factor.number().INT():  # type: ignore
                return "int"
            elif factor.number().REAL():  # type: ignore
                return "real"
        # Check if the factor is a literal
        elif factor.literal():
            return "boolean"
        # Check if the factor is a sub-expression
        elif factor.expression():
            return self.from_expression(factor.expression())  # type: ignore
        # Check if the factor is a negated factor
        elif factor.NOT():
            # If there is a NOT operator, the type must be boolean
            return "boolean"
        else:
            self.listener.semanticError(
                factor.start.line, factor.start.column, "Unknown factor type"
            )
            return "unknown"

    def from_term(self, term: LALGParser.TermContext) -> str:
        factors: list = term.factor()  # type: ignore
        operation_types = set()

        for i, factor in enumerate(factors):
            factor_type = self.from_factor(factor)
            operation_types.add(factor_type)

            if (
                i > 0
            ):  # If there's more than one factor, check the operations between them
                operation = term.children[  # type: ignore
                    i * 2 - 1
                ]  # The operation is every second child (1, 3, 5, ...)
                if operation.getText() in ["*", "/", "div", "and"]:
                    if factor_type not in ["int", "real"]:
                        self.listener.semanticError(
                            operation.symbol.line,  # type: ignore
                            operation.symbol.column,  # type: ignore
                            "Invalid type for arithmetic operation",
                        )
                else:
                    self.listener.semanticError(
                        operation.symbol.line,  # type: ignore
                        operation.symbol.column,  # type: ignore
                        "Unknown operation type",
                    )

        if len(operation_types) > 1:
            self.listener.semanticError(
                term.start.line,
                term.start.column,
                "Mixed types in term without coercion",
            )

        return operation_types.pop()

    def from_simple_expression(
        self, simple_expression: LALGParser.SimpleExpressionContext
    ) -> VariableType:
        terms: list = simple_expression.term()  # type: ignore
        types_in_expression = set()

        for i, term in enumerate(terms):
            term_type = self.from_term(term)
            types_in_expression.add(term_type)

            if i > 0:  # If there's more than one term, check the operators between them
                operator = simple_expression.children[  # type: ignore
                    i * 2 - 1
                ]  # The operator is every second child (1, 3, 5, ...)
                if operator.getText() in ["+", "-", "or"]:
                    if term_type not in ["int", "real"]:
                        self.listener.semanticError(
                            operator.symbol.line,  # type: ignore
                            operator.symbol.column,  # type: ignore
                            "Invalid type for additive operation",
                        )
                else:
                    self.listener.semanticError(
                        operator.symbol.line,  # type: ignore
                        operator.symbol.column,  # type: ignore
                        "Unknown operator type",
                    )

        if len(types_in_expression) > 1:
            self.listener.semanticError(
                simple_expression.start.line,
                simple_expression.start.column,
                "Mixed types in simple expression without coercion",
            )

        return types_in_expression.pop()  # There should only be one type in the set

    def from_expression(self, expression: LALGParser.ExpressionContext) -> VariableType:
        if expression.relationalOperator() is not None:
            return "boolean"

        simple_expression = expression.simpleExpression()[0]  # type: ignore
        return self.from_simple_expression(simple_expression)


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
                self.current_scope.define(
                    VariableSymbol(
                        variable_name, Position.from_symbol(identifier.symbol), var_type
                    )
                )

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
            self.enterScope(scope_name=proc_name)
            assert self.current_scope.enclosing_scope is not None
            self.visitChildren(ctx)

            def param_condition(symbol):
                return isinstance(symbol, ProcedureParamSymbol)

            collected_symbols = self.current_scope.symbols.values()
            identifier = ctx.IDENTIFIER()
            symbol = ProcedureSymbol(
                proc_name,
                Position.from_symbol(identifier.symbol),
                list(filter(param_condition, collected_symbols)),
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
                symbol = self.current_scope.resolve(variable_name)
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
        proc_symbol = self.current_scope.resolve(proc_name)
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

    def visitAssignmentStatement(self, ctx: LALGParser.AssignmentStatementContext):
        variable = ctx.variable()
        assert variable is not None
        variable_name = variable.IDENTIFIER().getText()
        symbol = self.current_scope.resolve(variable_name)
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
        expression_type = self.type_extractor.from_expression(expression)
        if symbol.type != expression_type:
            self.errorListener.semanticError(
                variable.IDENTIFIER().symbol.line,  # type: ignore
                variable.IDENTIFIER().symbol.column,  # type: ignore
                f"Variable {variable_name} expected {symbol.type} type, got {expression_type}",
            )

    def visitConditionalStatement(self, ctx: LALGParser.ConditionalStatementContext):
        expression = ctx.expression()
        expression_type = self.type_extractor.from_expression(expression)
        if expression_type != "boolean":
            self.errorListener.semanticError(
                ctx.IF().symbol.line,  # type: ignore
                ctx.IF().symbol.column,  # type: ignore
                f"Expected boolean expression, got {expression_type}",
            )

    def visitLoopStatement(self, ctx: LALGParser.LoopStatementContext):
        expression = ctx.expression()
        expression_type = self.type_extractor.from_expression(expression)
        if expression_type != "boolean":
            self.errorListener.semanticError(
                ctx.WHILE().symbol.line,  # type: ignore
                ctx.WHILE().symbol.column,  # type: ignore
                f"Expected boolean expression, got {expression_type}",
            )

    def visitTerm(self, ctx: LALGParser.TermContext):
        # dividsion of integers only allowed with INT_DIV
        if ctx.INT_DIV():
            left_term = ctx.factor(0)
            right_term = ctx.factor(1)
            left_type = self.type_extractor.from_factor(left_term)
            right_type = self.type_extractor.from_factor(right_term)
            if left_type != "integer" or right_type != "integer":
                self.errorListener.semanticError(
                    ctx.INT_DIV().symbol.line,  # type: ignore
                    ctx.INT_DIV().symbol.column,  # type: ignore
                    f"Expected integer expression, got {left_type} and {right_type}",
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

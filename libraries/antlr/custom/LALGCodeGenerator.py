from __future__ import annotations
from typing import Literal, Optional
from libraries.antlr.LALGParser import LALGParser
from libraries.antlr.LALGParserVisitor import LALGParserVisitor
from libraries.antlr.custom.LALGErrorListener import LALGErrorListener
from abc import ABC
from enum import Enum


VariableType = Literal["int", "boolean"]


class Variable(ABC):
    def __init__(self, name: str, address: int):
        self.name = name
        self.address = address


class Boolean(Variable):
    def __init__(self, name: str, address: int, value: Optional[bool] = None):
        super().__init__(name, address)
        self.value = value


class Integer(Variable):
    def __init__(self, name: str, address: int, value: Optional[int] = None):
        super().__init__(name, address)
        self.value = value


class LALGCodeGenerator(LALGParserVisitor):
    def __init__(self):
        self.code = []
        self.variables = {}
        self.data_counter = 0

    def generate(self, tree: LALGParser.ProgramContext) -> list[str]:
        self.visit(tree)
        # save the code to a file
        with open("code.txt", "w") as f:
            f.write("\n".join(self.code))

        return self.code

    def visitProgram(self, ctx: LALGParser.ProgramContext):
        self.code.append("INPP")
        self.visitChildren(ctx)
        self.code.append("PARA")
        return self.code

    def visitVariableDeclaration(self, ctx: LALGParser.VariableDeclarationContext):
        var_type: VariableType = ctx.type_().getText()  # type: ignore
        identifiers = ctx.identifierList().IDENTIFIER()  # type: ignore
        for identifier in identifiers:
            name: str = identifier.getText()
            address = self.data_counter
            self.data_counter += 1
            Constructor = Integer if var_type == "int" else Boolean
            self.variables[name] = Constructor(name, address)
            self.code.append(f"AMEM 1")

        self.visitChildren(ctx)

    def visitAssignmentStatement(self, ctx: LALGParser.AssignmentStatementContext):
        name = ctx.variable().IDENTIFIER().getText()  # type: ignore
        variable = self.variables[name]
        self.visit(ctx.expression())
        self.code.append(f"ARMZ {variable.address}")

    def visitIoProcedureCallStatement(
        self, ctx: LALGParser.IoProcedureCallStatementContext
    ):
        variables = name = ctx.variable()
        assert isinstance(variables, list)
        for variable in variables:
            name = variable.IDENTIFIER().getText()
            var = self.variables[name]
            if ctx.READ_PROCEDURE():
                self.code.append(f"LEIT")
                self.code.append(f"ARMZ {var.address}")
            elif ctx.WRITE_PROCEDURE():
                self.code.append(f"CRVL {var.address}")
                self.code.append(f"IMPR")

    def visitVariable(self, ctx: LALGParser.VariableContext):
        name = ctx.IDENTIFIER().getText()  # type: ignore
        variable = self.variables[name]
        self.code.append(f"CRVL {variable.address}")

    def visitConditionalStatement(self, ctx: LALGParser.ConditionalStatementContext):
        # conditionalStatement: IF LP expression RP statement (ELSE statement)?;
        # DSVF (if false) and DSVS (always) instructions
        self.visit(ctx.expression())
        self.code.append("DSVF")
        l1 = len(self.code) - 1
        self.visit(ctx.statement(0))
        if ctx.ELSE():
            self.code.append("DSVS")
            l2 = len(self.code) - 1
            self.code[l1] += f" {l2 + 1}"
            self.visit(ctx.statement(1))
            self.code[l2] += f" {len(self.code)}"
        else:
            self.code[l1] += f" {len(self.code)}"

        return self.code
    
    def visitLoopStatement(self, ctx: LALGParser.LoopStatementContext):
        # loopStatement: WHILE LP expression RP statement;
        # DSVF (if false) and DSVS (always) instructions

        l1 = len(self.code)
        self.visit(ctx.expression())
        self.code.append("DSVF")
        l2 = len(self.code) - 1
        self.visit(ctx.statement())
        self.code.append(f"DSVS {l1}")
        self.code[l2] += f" {len(self.code)}"
        return self.code


    def visitRelationalOperator(self, ctx: LALGParser.RelationalOperatorContext):
        if ctx.EQUAL():
            self.code.append("CMIG")
        elif ctx.NOT_EQUAL():
            self.code.append("CMDG")
        elif ctx.GREATER_THAN():
            self.code.append("CMMA")
        elif ctx.GREATER_THAN_OR_EQUAL():
            self.code.append("CMAG")
        elif ctx.LESS_THAN():
            self.code.append("CMME")
        elif ctx.LESS_THAN_OR_EQUAL():
            self.code.append("CMEG")

    def visitExpression(self, ctx: LALGParser.ExpressionContext):
        simple_expressions = ctx.simpleExpression()
        assert isinstance(simple_expressions, list)
        self.visit(simple_expressions[0])
        if len(simple_expressions) > 1:
            self.visit(simple_expressions[1])
            self.visit(ctx.relationalOperator())

    def visitTerm(self, ctx: LALGParser.TermContext):
        factors = ctx.factor()
        assert isinstance(factors, list)
        for i in range(len(factors) - 1):
            self.visit(factors[i + 1])
            if ctx.MUL(i):
                self.code.append("MULT")
            elif ctx.AND(i):
                self.code.append("CONJ")
            elif ctx.INT_DIV(i):
                self.code.append("DIVI")
            elif ctx.DIV(i):
                self.code.append("DIVI")

        return super().visitTerm(ctx)

    def visitFactor(self, ctx: LALGParser.FactorContext):
        if ctx.NOT():
            self.code.append("NEGA")
            self.visit(ctx.factor())
        elif ctx.variable():
            self.visit(ctx.variable())
        elif ctx.expression():
            self.visit(ctx.expression())
        elif ctx.literal():
            self.visit(ctx.literal())
        elif ctx.number():
            self.visit(ctx.number())

    def visitSimpleExpression(self, ctx: LALGParser.SimpleExpressionContext):
        term_signal = ctx.termSignal()

        terms = ctx.term()
        assert isinstance(terms, list)
        self.visit(terms[0])
        if term_signal:
            self.visit(term_signal)

        for i in range(len(terms) - 1):
            self.visit(terms[i + 1])
            if ctx.SUM(i):
                self.code.append("SOMA")
            elif ctx.SUB(i):
                self.code.append("SUBT")
            elif ctx.OR(i):
                self.code.append("DISJ")

    def visitTermSignal(self, ctx: LALGParser.TermSignalContext):
        if ctx.SUB():
            self.code.append("INVR")

    def visitLiteral(self, ctx: LALGParser.LiteralContext):
        if ctx.LITERAL_FALSE():
            self.code.append("CRCT 0")
        elif ctx.LITERAL_TRUE():
            self.code.append("CRCT 1")

    def visitNumber(self, ctx: LALGParser.NumberContext):
        self.code.append(f"CRCT {ctx.getText()}")

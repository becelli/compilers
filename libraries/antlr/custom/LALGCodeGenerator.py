from __future__ import annotations
from typing import Literal, Optional
from libraries.antlr.LALGParser import LALGParser
from libraries.antlr.LALGParserVisitor import LALGParserVisitor
from libraries.antlr.custom.LALGErrorListener import LALGErrorListener
from dataclasses import dataclass
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
        self.conditional_statements = []

    def generate(self, tree: LALGParser.ProgramContext):
        self.visit(tree)
        # save the code to a file
        with open("code.txt", "w") as f:
            f.write("\n".join(self.code))

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
            variable = Integer if var_type == "int" else Boolean
            self.variables[name] = variable(name, address)
            self.code.append(f"AMEM 1")

        self.visitChildren(ctx)

    def visitAssignmentStatement(self, ctx: LALGParser.AssignmentStatementContext):
        name = ctx.variable().IDENTIFIER().getText()
        variable = self.variables[name]
        self.visit(ctx.expression())
        self.code.append(f"ARMZ {variable.address}")

    def visitIoProcedureCallStatement(
        self, ctx: LALGParser.IoProcedureCallStatementContext
    ):
        if ctx.READ_PROCEDURE():
            name = ctx.variable().IDENTIFIER().getText()
            variable = self.variables[name]
            self.code.append(f"LEIT")
            self.code.append(f"ARMZ {variable.address}")
        elif ctx.WRITE_PROCEDURE():
            self.visit(ctx.variable())
            self.code.append(f"IMPR")

    def visitVariable(self, ctx: LALGParser.VariableContext):
        name = ctx.IDENTIFIER().getText()
        variable = self.variables[name]
        self.code.append(f"CRVL {variable.address}")

    def visitConditionalStatement(self, ctx: LALGParser.ConditionalStatementContext):
        self.visit(ctx.expression())
        self.code.append("DSVF")
        self.conditional_statements.append(len(self.code) - 1)
        self.visit(ctx.statement(0))
        self.code.append("DSVS")
        self.code.append("NADA")
        if ctx.ELSE():
            self.conditional_statements.append(len(self.code) - 1)
            self.visit(ctx.statement(1))
            self.code.append("NADA")
        self.code[self.conditional_statements[0]] = f"DSVF {len(self.code)}"
        if len(self.conditional_statements) > 1:
            self.code[self.conditional_statements[1]] = f"DSVS {len(self.code)}"
        self.conditional_statements = []
        


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

    def visitTerm(self, ctx: LALGParser.TermContext):
        factors = ctx.factor()
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
        terms = ctx.term()
        self.visit(terms[0])
        for i in range(len(terms) - 1):
            self.visit(terms[i + 1])
            if ctx.SUM(i):
                self.code.append("SOMA")
            elif ctx.SUB(i):
                self.code.append("SUBT")
            elif ctx.OR(i):
                self.code.append("DISJ")

    def visitLiteral(self, ctx: LALGParser.LiteralContext):
        if ctx.LITERAL_FALSE():
            self.code.append("CRCT 0")
        elif ctx.LITERAL_TRUE():
            self.code.append("CRCT 1")

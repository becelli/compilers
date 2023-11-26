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

    def generate(self, tree: LALGParser.ProgramContext):
        self.visit(tree)
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
            variable = Integer if var_type == "int" else Boolean
            self.variables[name] = variable(name, address)
            self.code.append(f"AMEM 1")

        self.visitChildren(ctx)

    def visitAssignmentStatement(self, ctx: LALGParser.AssignmentStatementContext):
        name = ctx.variable().IDENTIFIER().getText()
        variable = self.variables[name]
        self.visit(ctx.expression())
        self.code.append(f"ARMZ {variable.address}")

    def visitIoProcedureCallStatement(self, ctx: LALGParser.ioProcedureCallStatementContext):
        if ctx.READ():
            name = ctx.variable().IDENTIFIER().getText()
            variable = self.variables[name]
            self.code.append(f"LEIT")
            self.code.append(f"ARMZ {variable.address}")
        elif ctx.WRITE():
            self.visit(ctx.expression())
            self.code.append(f"IMPR")
        
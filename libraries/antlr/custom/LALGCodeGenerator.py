from __future__ import annotations
from libraries.antlr.LALGParser import LALGParser
from libraries.antlr.LALGParserVisitor import LALGParserVisitor


class Variable:
    def __init__(self, name: str, address: int):
        self.name = name
        self.address = address


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
        identifiers = ctx.identifierList().IDENTIFIER()  # type: ignore
        for identifier in identifiers:
            name: str = identifier.getText()
            address = self.data_counter
            self.data_counter += 1
            self.variables[name] = Variable(name, address)
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
        additive_expressions = ctx.additiveExpression()
        assert isinstance(additive_expressions, list)
        self.visit(additive_expressions[0])
        length = len(additive_expressions)
        assert length <= 2
        if length == 2:
            self.visit(additive_expressions[1])
            self.visit(ctx.relationalOperator())

    def visitAdditiveExpression(self, ctx: LALGParser.AdditiveExpressionContext):
        multiplicative_expressions = ctx.multiplicativeExpression()
        assert isinstance(multiplicative_expressions, list)
        self.visit(multiplicative_expressions[0])
        length = len(multiplicative_expressions)
        for i in range(length - 1):
            self.visit(multiplicative_expressions[i + 1])
            self.visit(ctx.additiveOperator(i))

    def visitMultiplicativeExpression(
        self, ctx: LALGParser.MultiplicativeExpressionContext
    ):
        unary_expressions = ctx.unaryExpression()
        assert isinstance(unary_expressions, list)
        self.visit(unary_expressions[0])
        length = len(unary_expressions)
        for i in range(length - 1):
            self.visit(unary_expressions[i + 1])
            self.visit(ctx.multiplicativeOperator(i))

    def visitUnaryExpression(self, ctx: LALGParser.UnaryExpressionContext):
        self.visit(ctx.primaryExpression())
        if ctx.unaryOperator():
            self.visit(ctx.unaryOperator())

    def visitUnaryOperator(self, ctx: LALGParser.UnaryOperatorContext):
        if ctx.SUM():
            self.code.append("NADA")
        elif ctx.SUB():
            self.code.append("INVR")
        elif ctx.NOT():
            self.code.append("NEGA")

    def visitMultiplicativeOperator(
        self, ctx: LALGParser.MultiplicativeOperatorContext
    ):
        if ctx.MUL():
            self.code.append("MULT")
        elif ctx.DIV():
            self.code.append("DIVI")
        elif ctx.INT_DIV():
            self.code.append("DIVI")
        elif ctx.AND():
            self.code.append("CONJ")

    def visitAdditiveOperator(self, ctx: LALGParser.AdditiveOperatorContext):
        if ctx.SUM():
            self.code.append("SOMA")
        elif ctx.SUB():
            self.code.append("SUBT")
        elif ctx.OR():
            self.code.append("DISJ")

    def visitLiteral(self, ctx: LALGParser.LiteralContext):
        if ctx.LITERAL_FALSE():
            self.code.append("CRCT 0")
        elif ctx.LITERAL_TRUE():
            self.code.append("CRCT 1")

    def visitNumber(self, ctx: LALGParser.NumberContext):
        self.code.append(f"CRCT {ctx.getText()}")

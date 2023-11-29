# Generated from libraries/antlr/LALGParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LALGParser import LALGParser
else:
    from LALGParser import LALGParser

# This class defines a complete generic visitor for a parse tree produced by LALGParser.

class LALGParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LALGParser#program.
    def visitProgram(self, ctx:LALGParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#type.
    def visitType(self, ctx:LALGParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#block.
    def visitBlock(self, ctx:LALGParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#variableDeclarationSection.
    def visitVariableDeclarationSection(self, ctx:LALGParser.VariableDeclarationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:LALGParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#identifierList.
    def visitIdentifierList(self, ctx:LALGParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#subroutineDeclarationSection.
    def visitSubroutineDeclarationSection(self, ctx:LALGParser.SubroutineDeclarationSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#procedureDeclaration.
    def visitProcedureDeclaration(self, ctx:LALGParser.ProcedureDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#formalParameterList.
    def visitFormalParameterList(self, ctx:LALGParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#formalParameterSection.
    def visitFormalParameterSection(self, ctx:LALGParser.FormalParameterSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#compoundStatement.
    def visitCompoundStatement(self, ctx:LALGParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#statement.
    def visitStatement(self, ctx:LALGParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:LALGParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#procedureCallStatement.
    def visitProcedureCallStatement(self, ctx:LALGParser.ProcedureCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:LALGParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#loopStatement.
    def visitLoopStatement(self, ctx:LALGParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#expression.
    def visitExpression(self, ctx:LALGParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:LALGParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:LALGParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#unaryExpression.
    def visitUnaryExpression(self, ctx:LALGParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:LALGParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#additiveOperator.
    def visitAdditiveOperator(self, ctx:LALGParser.AdditiveOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#multiplicativeOperator.
    def visitMultiplicativeOperator(self, ctx:LALGParser.MultiplicativeOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#unaryOperator.
    def visitUnaryOperator(self, ctx:LALGParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#relationalOperator.
    def visitRelationalOperator(self, ctx:LALGParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#variable.
    def visitVariable(self, ctx:LALGParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#expressionList.
    def visitExpressionList(self, ctx:LALGParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#number.
    def visitNumber(self, ctx:LALGParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#literal.
    def visitLiteral(self, ctx:LALGParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LALGParser#ioProcedureCallStatement.
    def visitIoProcedureCallStatement(self, ctx:LALGParser.IoProcedureCallStatementContext):
        return self.visitChildren(ctx)



del LALGParser
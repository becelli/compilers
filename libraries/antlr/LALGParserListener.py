# Generated from libraries/antlr/LALGParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LALGParser import LALGParser
else:
    from LALGParser import LALGParser

# This class defines a complete listener for a parse tree produced by LALGParser.
class LALGParserListener(ParseTreeListener):

    # Enter a parse tree produced by LALGParser#program.
    def enterProgram(self, ctx:LALGParser.ProgramContext):
        pass

    # Exit a parse tree produced by LALGParser#program.
    def exitProgram(self, ctx:LALGParser.ProgramContext):
        pass


    # Enter a parse tree produced by LALGParser#type.
    def enterType(self, ctx:LALGParser.TypeContext):
        pass

    # Exit a parse tree produced by LALGParser#type.
    def exitType(self, ctx:LALGParser.TypeContext):
        pass


    # Enter a parse tree produced by LALGParser#block.
    def enterBlock(self, ctx:LALGParser.BlockContext):
        pass

    # Exit a parse tree produced by LALGParser#block.
    def exitBlock(self, ctx:LALGParser.BlockContext):
        pass


    # Enter a parse tree produced by LALGParser#variableDeclarationSection.
    def enterVariableDeclarationSection(self, ctx:LALGParser.VariableDeclarationSectionContext):
        pass

    # Exit a parse tree produced by LALGParser#variableDeclarationSection.
    def exitVariableDeclarationSection(self, ctx:LALGParser.VariableDeclarationSectionContext):
        pass


    # Enter a parse tree produced by LALGParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:LALGParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by LALGParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:LALGParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by LALGParser#identifierList.
    def enterIdentifierList(self, ctx:LALGParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by LALGParser#identifierList.
    def exitIdentifierList(self, ctx:LALGParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by LALGParser#subroutineDeclarationSection.
    def enterSubroutineDeclarationSection(self, ctx:LALGParser.SubroutineDeclarationSectionContext):
        pass

    # Exit a parse tree produced by LALGParser#subroutineDeclarationSection.
    def exitSubroutineDeclarationSection(self, ctx:LALGParser.SubroutineDeclarationSectionContext):
        pass


    # Enter a parse tree produced by LALGParser#procedureDeclaration.
    def enterProcedureDeclaration(self, ctx:LALGParser.ProcedureDeclarationContext):
        pass

    # Exit a parse tree produced by LALGParser#procedureDeclaration.
    def exitProcedureDeclaration(self, ctx:LALGParser.ProcedureDeclarationContext):
        pass


    # Enter a parse tree produced by LALGParser#formalParameterList.
    def enterFormalParameterList(self, ctx:LALGParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by LALGParser#formalParameterList.
    def exitFormalParameterList(self, ctx:LALGParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by LALGParser#formalParameterSection.
    def enterFormalParameterSection(self, ctx:LALGParser.FormalParameterSectionContext):
        pass

    # Exit a parse tree produced by LALGParser#formalParameterSection.
    def exitFormalParameterSection(self, ctx:LALGParser.FormalParameterSectionContext):
        pass


    # Enter a parse tree produced by LALGParser#compoundStatement.
    def enterCompoundStatement(self, ctx:LALGParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#compoundStatement.
    def exitCompoundStatement(self, ctx:LALGParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#statement.
    def enterStatement(self, ctx:LALGParser.StatementContext):
        pass

    # Exit a parse tree produced by LALGParser#statement.
    def exitStatement(self, ctx:LALGParser.StatementContext):
        pass


    # Enter a parse tree produced by LALGParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:LALGParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:LALGParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#procedureCallStatement.
    def enterProcedureCallStatement(self, ctx:LALGParser.ProcedureCallStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#procedureCallStatement.
    def exitProcedureCallStatement(self, ctx:LALGParser.ProcedureCallStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:LALGParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:LALGParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#loopStatement.
    def enterLoopStatement(self, ctx:LALGParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#loopStatement.
    def exitLoopStatement(self, ctx:LALGParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by LALGParser#expression.
    def enterExpression(self, ctx:LALGParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LALGParser#expression.
    def exitExpression(self, ctx:LALGParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LALGParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:LALGParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by LALGParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:LALGParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by LALGParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:LALGParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by LALGParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:LALGParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by LALGParser#unaryExpression.
    def enterUnaryExpression(self, ctx:LALGParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by LALGParser#unaryExpression.
    def exitUnaryExpression(self, ctx:LALGParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by LALGParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:LALGParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by LALGParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:LALGParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by LALGParser#additiveOperator.
    def enterAdditiveOperator(self, ctx:LALGParser.AdditiveOperatorContext):
        pass

    # Exit a parse tree produced by LALGParser#additiveOperator.
    def exitAdditiveOperator(self, ctx:LALGParser.AdditiveOperatorContext):
        pass


    # Enter a parse tree produced by LALGParser#multiplicativeOperator.
    def enterMultiplicativeOperator(self, ctx:LALGParser.MultiplicativeOperatorContext):
        pass

    # Exit a parse tree produced by LALGParser#multiplicativeOperator.
    def exitMultiplicativeOperator(self, ctx:LALGParser.MultiplicativeOperatorContext):
        pass


    # Enter a parse tree produced by LALGParser#unaryOperator.
    def enterUnaryOperator(self, ctx:LALGParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by LALGParser#unaryOperator.
    def exitUnaryOperator(self, ctx:LALGParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by LALGParser#relationalOperator.
    def enterRelationalOperator(self, ctx:LALGParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by LALGParser#relationalOperator.
    def exitRelationalOperator(self, ctx:LALGParser.RelationalOperatorContext):
        pass


    # Enter a parse tree produced by LALGParser#variable.
    def enterVariable(self, ctx:LALGParser.VariableContext):
        pass

    # Exit a parse tree produced by LALGParser#variable.
    def exitVariable(self, ctx:LALGParser.VariableContext):
        pass


    # Enter a parse tree produced by LALGParser#expressionList.
    def enterExpressionList(self, ctx:LALGParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by LALGParser#expressionList.
    def exitExpressionList(self, ctx:LALGParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by LALGParser#number.
    def enterNumber(self, ctx:LALGParser.NumberContext):
        pass

    # Exit a parse tree produced by LALGParser#number.
    def exitNumber(self, ctx:LALGParser.NumberContext):
        pass


    # Enter a parse tree produced by LALGParser#literal.
    def enterLiteral(self, ctx:LALGParser.LiteralContext):
        pass

    # Exit a parse tree produced by LALGParser#literal.
    def exitLiteral(self, ctx:LALGParser.LiteralContext):
        pass


    # Enter a parse tree produced by LALGParser#ioProcedureCallStatement.
    def enterIoProcedureCallStatement(self, ctx:LALGParser.IoProcedureCallStatementContext):
        pass

    # Exit a parse tree produced by LALGParser#ioProcedureCallStatement.
    def exitIoProcedureCallStatement(self, ctx:LALGParser.IoProcedureCallStatementContext):
        pass



del LALGParser
# Generated from libraries/antlr/LALGParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LALGParser import LALGParser
else:
    from LALGParser import LALGParser

# This class defines a complete listener for a parse tree produced by LALGParser.
class LALGParserListener(ParseTreeListener):

    # Enter a parse tree produced by LALGParser#number.
    def enterNumber(self, ctx:LALGParser.NumberContext):
        pass

    # Exit a parse tree produced by LALGParser#number.
    def exitNumber(self, ctx:LALGParser.NumberContext):
        pass


    # Enter a parse tree produced by LALGParser#relation_operator.
    def enterRelation_operator(self, ctx:LALGParser.Relation_operatorContext):
        pass

    # Exit a parse tree produced by LALGParser#relation_operator.
    def exitRelation_operator(self, ctx:LALGParser.Relation_operatorContext):
        pass


    # Enter a parse tree produced by LALGParser#factor.
    def enterFactor(self, ctx:LALGParser.FactorContext):
        pass

    # Exit a parse tree produced by LALGParser#factor.
    def exitFactor(self, ctx:LALGParser.FactorContext):
        pass


    # Enter a parse tree produced by LALGParser#term.
    def enterTerm(self, ctx:LALGParser.TermContext):
        pass

    # Exit a parse tree produced by LALGParser#term.
    def exitTerm(self, ctx:LALGParser.TermContext):
        pass


    # Enter a parse tree produced by LALGParser#simple_expression.
    def enterSimple_expression(self, ctx:LALGParser.Simple_expressionContext):
        pass

    # Exit a parse tree produced by LALGParser#simple_expression.
    def exitSimple_expression(self, ctx:LALGParser.Simple_expressionContext):
        pass


    # Enter a parse tree produced by LALGParser#expression.
    def enterExpression(self, ctx:LALGParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LALGParser#expression.
    def exitExpression(self, ctx:LALGParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LALGParser#variable.
    def enterVariable(self, ctx:LALGParser.VariableContext):
        pass

    # Exit a parse tree produced by LALGParser#variable.
    def exitVariable(self, ctx:LALGParser.VariableContext):
        pass



del LALGParser
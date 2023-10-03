# Generated from libraries/antlr/lalg_parser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .lalg_parser import lalg_parser
else:
    from lalg_parser import lalg_parser

# This class defines a complete listener for a parse tree produced by lalg_parser.
class lalg_parserListener(ParseTreeListener):

    # Enter a parse tree produced by lalg_parser#number.
    def enterNumber(self, ctx:lalg_parser.NumberContext):
        pass

    # Exit a parse tree produced by lalg_parser#number.
    def exitNumber(self, ctx:lalg_parser.NumberContext):
        pass


    # Enter a parse tree produced by lalg_parser#relation_operator.
    def enterRelation_operator(self, ctx:lalg_parser.Relation_operatorContext):
        pass

    # Exit a parse tree produced by lalg_parser#relation_operator.
    def exitRelation_operator(self, ctx:lalg_parser.Relation_operatorContext):
        pass


    # Enter a parse tree produced by lalg_parser#factor.
    def enterFactor(self, ctx:lalg_parser.FactorContext):
        pass

    # Exit a parse tree produced by lalg_parser#factor.
    def exitFactor(self, ctx:lalg_parser.FactorContext):
        pass


    # Enter a parse tree produced by lalg_parser#term.
    def enterTerm(self, ctx:lalg_parser.TermContext):
        pass

    # Exit a parse tree produced by lalg_parser#term.
    def exitTerm(self, ctx:lalg_parser.TermContext):
        pass


    # Enter a parse tree produced by lalg_parser#simple_expression.
    def enterSimple_expression(self, ctx:lalg_parser.Simple_expressionContext):
        pass

    # Exit a parse tree produced by lalg_parser#simple_expression.
    def exitSimple_expression(self, ctx:lalg_parser.Simple_expressionContext):
        pass


    # Enter a parse tree produced by lalg_parser#expression.
    def enterExpression(self, ctx:lalg_parser.ExpressionContext):
        pass

    # Exit a parse tree produced by lalg_parser#expression.
    def exitExpression(self, ctx:lalg_parser.ExpressionContext):
        pass


    # Enter a parse tree produced by lalg_parser#variable.
    def enterVariable(self, ctx:lalg_parser.VariableContext):
        pass

    # Exit a parse tree produced by lalg_parser#variable.
    def exitVariable(self, ctx:lalg_parser.VariableContext):
        pass



del lalg_parser
# Generated from LangParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangParserListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#numero.
    def enterNumero(self, ctx:LangParser.NumeroContext):
        pass

    # Exit a parse tree produced by LangParser#numero.
    def exitNumero(self, ctx:LangParser.NumeroContext):
        pass


    # Enter a parse tree produced by LangParser#relacao.
    def enterRelacao(self, ctx:LangParser.RelacaoContext):
        pass

    # Exit a parse tree produced by LangParser#relacao.
    def exitRelacao(self, ctx:LangParser.RelacaoContext):
        pass


    # Enter a parse tree produced by LangParser#termo.
    def enterTermo(self, ctx:LangParser.TermoContext):
        pass

    # Exit a parse tree produced by LangParser#termo.
    def exitTermo(self, ctx:LangParser.TermoContext):
        pass


    # Enter a parse tree produced by LangParser#expressaoSimples.
    def enterExpressaoSimples(self, ctx:LangParser.ExpressaoSimplesContext):
        pass

    # Exit a parse tree produced by LangParser#expressaoSimples.
    def exitExpressaoSimples(self, ctx:LangParser.ExpressaoSimplesContext):
        pass


    # Enter a parse tree produced by LangParser#expressao.
    def enterExpressao(self, ctx:LangParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LangParser#expressao.
    def exitExpressao(self, ctx:LangParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LangParser#fator.
    def enterFator(self, ctx:LangParser.FatorContext):
        pass

    # Exit a parse tree produced by LangParser#fator.
    def exitFator(self, ctx:LangParser.FatorContext):
        pass


    # Enter a parse tree produced by LangParser#variavel.
    def enterVariavel(self, ctx:LangParser.VariavelContext):
        pass

    # Exit a parse tree produced by LangParser#variavel.
    def exitVariavel(self, ctx:LangParser.VariavelContext):
        pass



del LangParser
# Generated from LangParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,59,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,22,8,2,10,2,12,2,25,9,2,1,3,3,
        3,28,8,3,1,3,1,3,1,3,5,3,33,8,3,10,3,12,3,36,9,3,1,4,1,4,1,4,1,4,
        3,4,42,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,52,8,5,1,6,1,6,1,
        6,3,6,57,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,5,1,0,41,42,1,0,34,39,3,
        0,20,20,23,23,25,25,2,0,22,22,26,26,3,0,19,19,22,22,26,26,59,0,14,
        1,0,0,0,2,16,1,0,0,0,4,18,1,0,0,0,6,27,1,0,0,0,8,37,1,0,0,0,10,51,
        1,0,0,0,12,56,1,0,0,0,14,15,7,0,0,0,15,1,1,0,0,0,16,17,7,1,0,0,17,
        3,1,0,0,0,18,23,3,10,5,0,19,20,7,2,0,0,20,22,3,10,5,0,21,19,1,0,
        0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,5,1,0,0,0,25,23,
        1,0,0,0,26,28,7,3,0,0,27,26,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,
        29,34,3,4,2,0,30,31,7,4,0,0,31,33,3,4,2,0,32,30,1,0,0,0,33,36,1,
        0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,7,1,0,0,0,36,34,1,0,0,0,37,
        41,3,6,3,0,38,39,3,2,1,0,39,40,3,6,3,0,40,42,1,0,0,0,41,38,1,0,0,
        0,41,42,1,0,0,0,42,9,1,0,0,0,43,52,3,12,6,0,44,52,3,0,0,0,45,46,
        5,27,0,0,46,47,3,8,4,0,47,48,5,28,0,0,48,52,1,0,0,0,49,50,5,21,0,
        0,50,52,3,10,5,0,51,43,1,0,0,0,51,44,1,0,0,0,51,45,1,0,0,0,51,49,
        1,0,0,0,52,11,1,0,0,0,53,57,5,40,0,0,54,55,5,40,0,0,55,57,3,8,4,
        0,56,53,1,0,0,0,56,54,1,0,0,0,57,13,1,0,0,0,6,23,27,34,41,51,56
    ]

class LangParser ( Parser ):

    grammarFileName = "LangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'procedure'", "';'", "':='", 
                     "':'", "','", "'var'", "'int'", "'boolean'", "'read'", 
                     "'write'", "'true'", "'false'", "'begin'", "'end'", 
                     "'if'", "'then'", "'else'", "'or'", "'and'", "'not'", 
                     "'+'", "'*'", "'/'", "'div'", "'-'", "'('", "')'", 
                     "'['", "']'", "'while'", "'do'", "'.'", "'='", "'<>'", 
                     "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "PROCEDURE", "SEMICOLON", 
                      "ATTRIB", "COLON", "COMMA", "VAR", "TYPE_INT", "TYPE_BOOL", 
                      "PROC_READ", "PROC_WRITE", "CONST_TRUE", "CONST_FALSE", 
                      "BEGIN", "END", "IF", "THEN", "ELSE", "OR", "AND", 
                      "NOT", "SUM", "MUL", "DIV", "INT_DIV", "SUB", "LP", 
                      "RP", "LB", "RB", "WHILE", "DO", "DOT", "EQUAL", "DIFF", 
                      "LT", "GT", "LTE", "GTE", "IDENTIFICADOR", "INT", 
                      "REAL", "COMMENT", "MULTILINE_COMMENT", "WS", "INVALID_TOKEN", 
                      "INVALID" ]

    RULE_numero = 0
    RULE_relacao = 1
    RULE_termo = 2
    RULE_expressaoSimples = 3
    RULE_expressao = 4
    RULE_fator = 5
    RULE_variavel = 6

    ruleNames =  [ "numero", "relacao", "termo", "expressaoSimples", "expressao", 
                   "fator", "variavel" ]

    EOF = Token.EOF
    PROGRAM=1
    PROCEDURE=2
    SEMICOLON=3
    ATTRIB=4
    COLON=5
    COMMA=6
    VAR=7
    TYPE_INT=8
    TYPE_BOOL=9
    PROC_READ=10
    PROC_WRITE=11
    CONST_TRUE=12
    CONST_FALSE=13
    BEGIN=14
    END=15
    IF=16
    THEN=17
    ELSE=18
    OR=19
    AND=20
    NOT=21
    SUM=22
    MUL=23
    DIV=24
    INT_DIV=25
    SUB=26
    LP=27
    RP=28
    LB=29
    RB=30
    WHILE=31
    DO=32
    DOT=33
    EQUAL=34
    DIFF=35
    LT=36
    GT=37
    LTE=38
    GTE=39
    IDENTIFICADOR=40
    INT=41
    REAL=42
    COMMENT=43
    MULTILINE_COMMENT=44
    WS=45
    INVALID_TOKEN=46
    INVALID=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LangParser.INT, 0)

        def REAL(self):
            return self.getToken(LangParser.REAL, 0)

        def getRuleIndex(self):
            return LangParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)




    def numero(self):

        localctx = LangParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(LangParser.EQUAL, 0)

        def DIFF(self):
            return self.getToken(LangParser.DIFF, 0)

        def LT(self):
            return self.getToken(LangParser.LT, 0)

        def LTE(self):
            return self.getToken(LangParser.LTE, 0)

        def GT(self):
            return self.getToken(LangParser.GT, 0)

        def GTE(self):
            return self.getToken(LangParser.GTE, 0)

        def getRuleIndex(self):
            return LangParser.RULE_relacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacao" ):
                listener.enterRelacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacao" ):
                listener.exitRelacao(self)




    def relacao(self):

        localctx = LangParser.RelacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_relacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.FatorContext)
            else:
                return self.getTypedRuleContext(LangParser.FatorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.MUL)
            else:
                return self.getToken(LangParser.MUL, i)

        def INT_DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.INT_DIV)
            else:
                return self.getToken(LangParser.INT_DIV, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.AND)
            else:
                return self.getToken(LangParser.AND, i)

        def getRuleIndex(self):
            return LangParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = LangParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.fator()
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 19
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 42991616) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 20
                    self.fator() 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoSimplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.TermoContext)
            else:
                return self.getTypedRuleContext(LangParser.TermoContext,i)


        def SUM(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.SUM)
            else:
                return self.getToken(LangParser.SUM, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.SUB)
            else:
                return self.getToken(LangParser.SUB, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.OR)
            else:
                return self.getToken(LangParser.OR, i)

        def getRuleIndex(self):
            return LangParser.RULE_expressaoSimples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoSimples" ):
                listener.enterExpressaoSimples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoSimples" ):
                listener.exitExpressaoSimples(self)




    def expressaoSimples(self):

        localctx = LangParser.ExpressaoSimplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expressaoSimples)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==26:
                self.state = 26
                _la = self._input.LA(1)
                if not(_la==22 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 29
            self.termo()
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 71827456) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 31
                    self.termo() 
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoSimples(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExpressaoSimplesContext)
            else:
                return self.getTypedRuleContext(LangParser.ExpressaoSimplesContext,i)


        def relacao(self):
            return self.getTypedRuleContext(LangParser.RelacaoContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)




    def expressao(self):

        localctx = LangParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.expressaoSimples()
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 38
                self.relacao()
                self.state = 39
                self.expressaoSimples()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variavel(self):
            return self.getTypedRuleContext(LangParser.VariavelContext,0)


        def numero(self):
            return self.getTypedRuleContext(LangParser.NumeroContext,0)


        def LP(self):
            return self.getToken(LangParser.LP, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangParser.ExpressaoContext,0)


        def RP(self):
            return self.getToken(LangParser.RP, 0)

        def NOT(self):
            return self.getToken(LangParser.NOT, 0)

        def fator(self):
            return self.getTypedRuleContext(LangParser.FatorContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)




    def fator(self):

        localctx = LangParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.state = 43
                self.variavel()
                pass
            elif token in [41, 42]:
                self.state = 44
                self.numero()
                pass
            elif token in [27]:
                self.state = 45
                self.match(LangParser.LP)
                self.state = 46
                self.expressao()
                self.state = 47
                self.match(LangParser.RP)
                pass
            elif token in [21]:
                self.state = 49
                self.match(LangParser.NOT)
                self.state = 50
                self.fator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(LangParser.IDENTIFICADOR, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_variavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariavel" ):
                listener.enterVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariavel" ):
                listener.exitVariavel(self)




    def variavel(self):

        localctx = LangParser.VariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 53
                self.match(LangParser.IDENTIFICADOR)
                pass

            elif la_ == 2:
                self.state = 54
                self.match(LangParser.IDENTIFICADOR)
                self.state = 55
                self.expressao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






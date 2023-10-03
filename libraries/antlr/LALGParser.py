# Generated from libraries/antlr/LALGParser.g4 by ANTLR 4.13.1
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
        6,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,27,8,2,1,3,
        1,3,1,3,5,3,32,8,3,10,3,12,3,35,9,3,1,4,3,4,38,8,4,1,4,1,4,1,4,5,
        4,43,8,4,10,4,12,4,46,9,4,1,5,1,5,1,5,1,5,3,5,52,8,5,1,6,1,6,1,6,
        3,6,57,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,5,1,0,41,42,1,0,26,31,3,0,
        20,20,22,22,24,24,1,0,18,19,2,0,18,19,23,23,59,0,14,1,0,0,0,2,16,
        1,0,0,0,4,26,1,0,0,0,6,28,1,0,0,0,8,37,1,0,0,0,10,47,1,0,0,0,12,
        56,1,0,0,0,14,15,7,0,0,0,15,1,1,0,0,0,16,17,7,1,0,0,17,3,1,0,0,0,
        18,27,3,12,6,0,19,27,3,0,0,0,20,21,5,36,0,0,21,22,3,10,5,0,22,23,
        5,37,0,0,23,27,1,0,0,0,24,25,5,25,0,0,25,27,3,4,2,0,26,18,1,0,0,
        0,26,19,1,0,0,0,26,20,1,0,0,0,26,24,1,0,0,0,27,5,1,0,0,0,28,33,3,
        4,2,0,29,30,7,2,0,0,30,32,3,4,2,0,31,29,1,0,0,0,32,35,1,0,0,0,33,
        31,1,0,0,0,33,34,1,0,0,0,34,7,1,0,0,0,35,33,1,0,0,0,36,38,7,3,0,
        0,37,36,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,44,3,6,3,0,40,41,
        7,4,0,0,41,43,3,6,3,0,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,
        44,45,1,0,0,0,45,9,1,0,0,0,46,44,1,0,0,0,47,51,3,8,4,0,48,49,3,2,
        1,0,49,50,3,8,4,0,50,52,1,0,0,0,51,48,1,0,0,0,51,52,1,0,0,0,52,11,
        1,0,0,0,53,57,5,40,0,0,54,55,5,40,0,0,55,57,3,10,5,0,56,53,1,0,0,
        0,56,54,1,0,0,0,57,13,1,0,0,0,6,26,33,37,44,51,56
    ]

class LALGParser ( Parser ):

    grammarFileName = "LALGParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'procedure'", "'var'", "'int'", 
                     "'boolean'", "'begin'", "'end'", "'if'", "'then'", 
                     "'else'", "'while'", "'do'", "'read'", "'write'", "'true'", 
                     "'false'", "':='", "'+'", "'-'", "'*'", "'/'", "'div'", 
                     "'or'", "'and'", "'not'", "'='", "'<>'", "'<'", "'>'", 
                     "'<='", "'>='", "';'", "':'", "','", "'.'", "'('", 
                     "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "PROCEDURE", "VAR", "TYPE_INT", 
                      "TYPE_BOOL", "BEGIN", "END", "IF", "THEN", "ELSE", 
                      "WHILE", "DO", "PROC_READ", "PROC_WRITE", "CONST_TRUE", 
                      "CONST_FALSE", "ATTRIB", "SUM", "SUB", "MUL", "DIV", 
                      "INT_DIV", "OR", "AND", "NOT", "EQUAL", "DIFF", "LT", 
                      "GT", "LTE", "GTE", "SEMICOLON", "COLON", "COMMA", 
                      "DOT", "LP", "RP", "LB", "RB", "IDENTIFIER", "INT", 
                      "REAL", "COMMENT", "MULTILINE_COMMENT", "WS", "INVALID_TOKEN", 
                      "INVALID" ]

    RULE_number = 0
    RULE_relation_operator = 1
    RULE_factor = 2
    RULE_term = 3
    RULE_simple_expression = 4
    RULE_expression = 5
    RULE_variable = 6

    ruleNames =  [ "number", "relation_operator", "factor", "term", "simple_expression", 
                   "expression", "variable" ]

    EOF = Token.EOF
    PROGRAM=1
    PROCEDURE=2
    VAR=3
    TYPE_INT=4
    TYPE_BOOL=5
    BEGIN=6
    END=7
    IF=8
    THEN=9
    ELSE=10
    WHILE=11
    DO=12
    PROC_READ=13
    PROC_WRITE=14
    CONST_TRUE=15
    CONST_FALSE=16
    ATTRIB=17
    SUM=18
    SUB=19
    MUL=20
    DIV=21
    INT_DIV=22
    OR=23
    AND=24
    NOT=25
    EQUAL=26
    DIFF=27
    LT=28
    GT=29
    LTE=30
    GTE=31
    SEMICOLON=32
    COLON=33
    COMMA=34
    DOT=35
    LP=36
    RP=37
    LB=38
    RB=39
    IDENTIFIER=40
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




    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LALGParser.INT, 0)

        def REAL(self):
            return self.getToken(LALGParser.REAL, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = LALGParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_number)
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


    class Relation_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(LALGParser.EQUAL, 0)

        def DIFF(self):
            return self.getToken(LALGParser.DIFF, 0)

        def LT(self):
            return self.getToken(LALGParser.LT, 0)

        def LTE(self):
            return self.getToken(LALGParser.LTE, 0)

        def GT(self):
            return self.getToken(LALGParser.GT, 0)

        def GTE(self):
            return self.getToken(LALGParser.GTE, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_relation_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation_operator" ):
                listener.enterRelation_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation_operator" ):
                listener.exitRelation_operator(self)




    def relation_operator(self):

        localctx = LALGParser.Relation_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_relation_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(LALGParser.VariableContext,0)


        def number(self):
            return self.getTypedRuleContext(LALGParser.NumberContext,0)


        def LP(self):
            return self.getToken(LALGParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(LALGParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(LALGParser.RP, 0)

        def NOT(self):
            return self.getToken(LALGParser.NOT, 0)

        def factor(self):
            return self.getTypedRuleContext(LALGParser.FactorContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = LALGParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.variable()
                pass
            elif token in [41, 42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.number()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.match(LALGParser.LP)
                self.state = 21
                self.expression()
                self.state = 22
                self.match(LALGParser.RP)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(LALGParser.NOT)
                self.state = 25
                self.factor()
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


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.FactorContext)
            else:
                return self.getTypedRuleContext(LALGParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.MUL)
            else:
                return self.getToken(LALGParser.MUL, i)

        def INT_DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.INT_DIV)
            else:
                return self.getToken(LALGParser.INT_DIV, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.AND)
            else:
                return self.getToken(LALGParser.AND, i)

        def getRuleIndex(self):
            return LALGParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = LALGParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.factor()
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 29
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 22020096) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 30
                    self.factor() 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.TermContext)
            else:
                return self.getTypedRuleContext(LALGParser.TermContext,i)


        def SUM(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.SUM)
            else:
                return self.getToken(LALGParser.SUM, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.SUB)
            else:
                return self.getToken(LALGParser.SUB, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.OR)
            else:
                return self.getToken(LALGParser.OR, i)

        def getRuleIndex(self):
            return LALGParser.RULE_simple_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_expression" ):
                listener.enterSimple_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_expression" ):
                listener.exitSimple_expression(self)




    def simple_expression(self):

        localctx = LALGParser.Simple_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simple_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18 or _la==19:
                self.state = 36
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 39
            self.term()
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 40
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9175040) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 41
                    self.term() 
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.Simple_expressionContext)
            else:
                return self.getTypedRuleContext(LALGParser.Simple_expressionContext,i)


        def relation_operator(self):
            return self.getTypedRuleContext(LALGParser.Relation_operatorContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = LALGParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.simple_expression()
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 48
                self.relation_operator()
                self.state = 49
                self.simple_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LALGParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LALGParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = LALGParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(LALGParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(LALGParser.IDENTIFIER)
                self.state = 55
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






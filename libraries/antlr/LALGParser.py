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
        4,1,47,225,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,3,2,63,8,2,1,2,3,2,66,8,2,1,2,1,2,
        1,3,1,3,1,3,5,3,73,8,3,10,3,12,3,76,9,3,1,3,1,3,1,4,1,4,1,4,1,5,
        1,5,1,5,5,5,86,8,5,10,5,12,5,89,9,5,1,6,1,6,1,6,5,6,94,8,6,10,6,
        12,6,97,9,6,1,7,1,7,1,7,3,7,102,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,
        5,8,111,8,8,10,8,12,8,114,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,
        10,1,10,1,10,5,10,127,8,10,10,10,12,10,130,9,10,1,10,1,10,1,11,1,
        11,1,11,1,11,1,11,1,11,3,11,140,8,11,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,13,3,13,151,8,13,1,14,1,14,1,14,1,14,1,14,1,14,3,
        14,159,8,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,170,
        8,16,1,17,1,17,1,18,3,18,175,8,18,1,18,1,18,1,18,5,18,180,8,18,10,
        18,12,18,183,9,18,1,19,1,19,1,19,5,19,188,8,19,10,19,12,19,191,9,
        19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,202,8,20,1,
        21,1,21,3,21,206,8,21,1,22,1,22,1,22,5,22,211,8,22,10,22,12,22,214,
        9,22,1,23,1,23,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,0,0,26,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,0,8,1,0,4,5,1,0,26,31,1,0,18,19,2,0,18,19,23,23,2,0,20,22,
        24,24,1,0,41,42,1,0,15,16,1,0,13,14,223,0,52,1,0,0,0,2,59,1,0,0,
        0,4,62,1,0,0,0,6,69,1,0,0,0,8,79,1,0,0,0,10,82,1,0,0,0,12,95,1,0,
        0,0,14,98,1,0,0,0,16,106,1,0,0,0,18,117,1,0,0,0,20,122,1,0,0,0,22,
        139,1,0,0,0,24,141,1,0,0,0,26,145,1,0,0,0,28,152,1,0,0,0,30,160,
        1,0,0,0,32,165,1,0,0,0,34,171,1,0,0,0,36,174,1,0,0,0,38,184,1,0,
        0,0,40,201,1,0,0,0,42,203,1,0,0,0,44,207,1,0,0,0,46,215,1,0,0,0,
        48,217,1,0,0,0,50,219,1,0,0,0,52,53,5,1,0,0,53,54,5,40,0,0,54,55,
        5,32,0,0,55,56,3,4,2,0,56,57,5,35,0,0,57,58,5,0,0,1,58,1,1,0,0,0,
        59,60,7,0,0,0,60,3,1,0,0,0,61,63,3,6,3,0,62,61,1,0,0,0,62,63,1,0,
        0,0,63,65,1,0,0,0,64,66,3,12,6,0,65,64,1,0,0,0,65,66,1,0,0,0,66,
        67,1,0,0,0,67,68,3,20,10,0,68,5,1,0,0,0,69,74,3,8,4,0,70,71,5,32,
        0,0,71,73,3,8,4,0,72,70,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,
        1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,5,32,0,0,78,7,1,0,0,0,
        79,80,3,2,1,0,80,81,3,10,5,0,81,9,1,0,0,0,82,87,5,40,0,0,83,84,5,
        34,0,0,84,86,5,40,0,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,
        87,88,1,0,0,0,88,11,1,0,0,0,89,87,1,0,0,0,90,91,3,14,7,0,91,92,5,
        32,0,0,92,94,1,0,0,0,93,90,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,
        96,1,0,0,0,96,13,1,0,0,0,97,95,1,0,0,0,98,99,5,2,0,0,99,101,5,40,
        0,0,100,102,3,16,8,0,101,100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,
        0,0,103,104,5,32,0,0,104,105,3,4,2,0,105,15,1,0,0,0,106,107,5,36,
        0,0,107,112,3,18,9,0,108,109,5,32,0,0,109,111,3,18,9,0,110,108,1,
        0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,1,
        0,0,0,114,112,1,0,0,0,115,116,5,37,0,0,116,17,1,0,0,0,117,118,5,
        3,0,0,118,119,3,10,5,0,119,120,5,33,0,0,120,121,3,2,1,0,121,19,1,
        0,0,0,122,123,5,6,0,0,123,128,3,22,11,0,124,125,5,32,0,0,125,127,
        3,22,11,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,5,7,0,0,132,21,1,
        0,0,0,133,140,3,24,12,0,134,140,3,26,13,0,135,140,3,50,25,0,136,
        140,3,20,10,0,137,140,3,28,14,0,138,140,3,30,15,0,139,133,1,0,0,
        0,139,134,1,0,0,0,139,135,1,0,0,0,139,136,1,0,0,0,139,137,1,0,0,
        0,139,138,1,0,0,0,140,23,1,0,0,0,141,142,3,42,21,0,142,143,5,17,
        0,0,143,144,3,32,16,0,144,25,1,0,0,0,145,150,5,40,0,0,146,147,5,
        36,0,0,147,148,3,44,22,0,148,149,5,37,0,0,149,151,1,0,0,0,150,146,
        1,0,0,0,150,151,1,0,0,0,151,27,1,0,0,0,152,153,5,8,0,0,153,154,3,
        32,16,0,154,155,5,9,0,0,155,158,3,22,11,0,156,157,5,10,0,0,157,159,
        3,22,11,0,158,156,1,0,0,0,158,159,1,0,0,0,159,29,1,0,0,0,160,161,
        5,11,0,0,161,162,3,32,16,0,162,163,5,12,0,0,163,164,3,22,11,0,164,
        31,1,0,0,0,165,169,3,36,18,0,166,167,3,34,17,0,167,168,3,36,18,0,
        168,170,1,0,0,0,169,166,1,0,0,0,169,170,1,0,0,0,170,33,1,0,0,0,171,
        172,7,1,0,0,172,35,1,0,0,0,173,175,7,2,0,0,174,173,1,0,0,0,174,175,
        1,0,0,0,175,176,1,0,0,0,176,181,3,38,19,0,177,178,7,3,0,0,178,180,
        3,38,19,0,179,177,1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,
        1,0,0,0,182,37,1,0,0,0,183,181,1,0,0,0,184,189,3,40,20,0,185,186,
        7,4,0,0,186,188,3,40,20,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,39,1,0,0,0,191,189,1,0,0,0,192,202,3,
        42,21,0,193,202,3,46,23,0,194,202,3,48,24,0,195,196,5,36,0,0,196,
        197,3,32,16,0,197,198,5,37,0,0,198,202,1,0,0,0,199,200,5,25,0,0,
        200,202,3,40,20,0,201,192,1,0,0,0,201,193,1,0,0,0,201,194,1,0,0,
        0,201,195,1,0,0,0,201,199,1,0,0,0,202,41,1,0,0,0,203,205,5,40,0,
        0,204,206,3,32,16,0,205,204,1,0,0,0,205,206,1,0,0,0,206,43,1,0,0,
        0,207,212,3,32,16,0,208,209,5,34,0,0,209,211,3,32,16,0,210,208,1,
        0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,45,1,0,
        0,0,214,212,1,0,0,0,215,216,7,5,0,0,216,47,1,0,0,0,217,218,7,6,0,
        0,218,49,1,0,0,0,219,220,7,7,0,0,220,221,5,36,0,0,221,222,3,42,21,
        0,222,223,5,37,0,0,223,51,1,0,0,0,18,62,65,74,87,95,101,112,128,
        139,150,158,169,174,181,189,201,205,212
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
                      "WHILE", "DO", "READ_PROCEDURE", "WRITE_PROCEDURE", 
                      "LITERAL_TRUE", "LITERAL_FALSE", "ASSIGNMENT", "SUM", 
                      "SUB", "MUL", "DIV", "INT_DIV", "OR", "AND", "NOT", 
                      "EQUAL", "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", 
                      "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", "SEMICOLON", 
                      "COLON", "COMMA", "DOT", "LP", "RP", "LB", "RB", "IDENTIFIER", 
                      "INT", "REAL", "COMMENT", "MULTILINE_COMMENT", "WS", 
                      "INVALID_TOKEN", "INVALID" ]

    RULE_program = 0
    RULE_type = 1
    RULE_block = 2
    RULE_variableDeclarationSection = 3
    RULE_variableDeclaration = 4
    RULE_identifierList = 5
    RULE_subroutineDeclarationSection = 6
    RULE_procedureDeclaration = 7
    RULE_formalParameterList = 8
    RULE_formalParameterSection = 9
    RULE_compoundStatement = 10
    RULE_statement = 11
    RULE_assignmentStatement = 12
    RULE_procedureCallStatement = 13
    RULE_conditionalStatement = 14
    RULE_loopStatement = 15
    RULE_expression = 16
    RULE_relationalOperator = 17
    RULE_simpleExpression = 18
    RULE_term = 19
    RULE_factor = 20
    RULE_variable = 21
    RULE_expressionList = 22
    RULE_number = 23
    RULE_literal = 24
    RULE_ioProcedureCallStatement = 25

    ruleNames =  [ "program", "type", "block", "variableDeclarationSection", 
                   "variableDeclaration", "identifierList", "subroutineDeclarationSection", 
                   "procedureDeclaration", "formalParameterList", "formalParameterSection", 
                   "compoundStatement", "statement", "assignmentStatement", 
                   "procedureCallStatement", "conditionalStatement", "loopStatement", 
                   "expression", "relationalOperator", "simpleExpression", 
                   "term", "factor", "variable", "expressionList", "number", 
                   "literal", "ioProcedureCallStatement" ]

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
    READ_PROCEDURE=13
    WRITE_PROCEDURE=14
    LITERAL_TRUE=15
    LITERAL_FALSE=16
    ASSIGNMENT=17
    SUM=18
    SUB=19
    MUL=20
    DIV=21
    INT_DIV=22
    OR=23
    AND=24
    NOT=25
    EQUAL=26
    NOT_EQUAL=27
    LESS_THAN=28
    GREATER_THAN=29
    LESS_THAN_OR_EQUAL=30
    GREATER_THAN_OR_EQUAL=31
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




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(LALGParser.PROGRAM, 0)

        def IDENTIFIER(self):
            return self.getToken(LALGParser.IDENTIFIER, 0)

        def SEMICOLON(self):
            return self.getToken(LALGParser.SEMICOLON, 0)

        def block(self):
            return self.getTypedRuleContext(LALGParser.BlockContext,0)


        def DOT(self):
            return self.getToken(LALGParser.DOT, 0)

        def EOF(self):
            return self.getToken(LALGParser.EOF, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = LALGParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(LALGParser.PROGRAM)
            self.state = 53
            self.match(LALGParser.IDENTIFIER)
            self.state = 54
            self.match(LALGParser.SEMICOLON)
            self.state = 55
            self.block()
            self.state = 56
            self.match(LALGParser.DOT)
            self.state = 57
            self.match(LALGParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_BOOL(self):
            return self.getToken(LALGParser.TYPE_BOOL, 0)

        def TYPE_INT(self):
            return self.getToken(LALGParser.TYPE_INT, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = LALGParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compoundStatement(self):
            return self.getTypedRuleContext(LALGParser.CompoundStatementContext,0)


        def variableDeclarationSection(self):
            return self.getTypedRuleContext(LALGParser.VariableDeclarationSectionContext,0)


        def subroutineDeclarationSection(self):
            return self.getTypedRuleContext(LALGParser.SubroutineDeclarationSectionContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = LALGParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4 or _la==5:
                self.state = 61
                self.variableDeclarationSection()


            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 64
                self.subroutineDeclarationSection()


            self.state = 67
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(LALGParser.VariableDeclarationContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.SEMICOLON)
            else:
                return self.getToken(LALGParser.SEMICOLON, i)

        def getRuleIndex(self):
            return LALGParser.RULE_variableDeclarationSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationSection" ):
                listener.enterVariableDeclarationSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationSection" ):
                listener.exitVariableDeclarationSection(self)




    def variableDeclarationSection(self):

        localctx = LALGParser.VariableDeclarationSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclarationSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.variableDeclaration()
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 70
                    self.match(LALGParser.SEMICOLON)
                    self.state = 71
                    self.variableDeclaration() 
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 77
            self.match(LALGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(LALGParser.TypeContext,0)


        def identifierList(self):
            return self.getTypedRuleContext(LALGParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = LALGParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.type_()
            self.state = 80
            self.identifierList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.IDENTIFIER)
            else:
                return self.getToken(LALGParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.COMMA)
            else:
                return self.getToken(LALGParser.COMMA, i)

        def getRuleIndex(self):
            return LALGParser.RULE_identifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierList" ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierList" ):
                listener.exitIdentifierList(self)




    def identifierList(self):

        localctx = LALGParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(LALGParser.IDENTIFIER)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 83
                self.match(LALGParser.COMMA)
                self.state = 84
                self.match(LALGParser.IDENTIFIER)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubroutineDeclarationSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def procedureDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.ProcedureDeclarationContext)
            else:
                return self.getTypedRuleContext(LALGParser.ProcedureDeclarationContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.SEMICOLON)
            else:
                return self.getToken(LALGParser.SEMICOLON, i)

        def getRuleIndex(self):
            return LALGParser.RULE_subroutineDeclarationSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubroutineDeclarationSection" ):
                listener.enterSubroutineDeclarationSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubroutineDeclarationSection" ):
                listener.exitSubroutineDeclarationSection(self)




    def subroutineDeclarationSection(self):

        localctx = LALGParser.SubroutineDeclarationSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subroutineDeclarationSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 90
                self.procedureDeclaration()
                self.state = 91
                self.match(LALGParser.SEMICOLON)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE(self):
            return self.getToken(LALGParser.PROCEDURE, 0)

        def IDENTIFIER(self):
            return self.getToken(LALGParser.IDENTIFIER, 0)

        def SEMICOLON(self):
            return self.getToken(LALGParser.SEMICOLON, 0)

        def block(self):
            return self.getTypedRuleContext(LALGParser.BlockContext,0)


        def formalParameterList(self):
            return self.getTypedRuleContext(LALGParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_procedureDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedureDeclaration" ):
                listener.enterProcedureDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedureDeclaration" ):
                listener.exitProcedureDeclaration(self)




    def procedureDeclaration(self):

        localctx = LALGParser.ProcedureDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_procedureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(LALGParser.PROCEDURE)
            self.state = 99
            self.match(LALGParser.IDENTIFIER)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 100
                self.formalParameterList()


            self.state = 103
            self.match(LALGParser.SEMICOLON)
            self.state = 104
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(LALGParser.LP, 0)

        def formalParameterSection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.FormalParameterSectionContext)
            else:
                return self.getTypedRuleContext(LALGParser.FormalParameterSectionContext,i)


        def RP(self):
            return self.getToken(LALGParser.RP, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.SEMICOLON)
            else:
                return self.getToken(LALGParser.SEMICOLON, i)

        def getRuleIndex(self):
            return LALGParser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterList" ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterList" ):
                listener.exitFormalParameterList(self)




    def formalParameterList(self):

        localctx = LALGParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(LALGParser.LP)
            self.state = 107
            self.formalParameterSection()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 108
                self.match(LALGParser.SEMICOLON)
                self.state = 109
                self.formalParameterSection()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(LALGParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LALGParser.VAR, 0)

        def identifierList(self):
            return self.getTypedRuleContext(LALGParser.IdentifierListContext,0)


        def COLON(self):
            return self.getToken(LALGParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(LALGParser.TypeContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_formalParameterSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterSection" ):
                listener.enterFormalParameterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterSection" ):
                listener.exitFormalParameterSection(self)




    def formalParameterSection(self):

        localctx = LALGParser.FormalParameterSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_formalParameterSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(LALGParser.VAR)
            self.state = 118
            self.identifierList()
            self.state = 119
            self.match(LALGParser.COLON)
            self.state = 120
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(LALGParser.BEGIN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.StatementContext)
            else:
                return self.getTypedRuleContext(LALGParser.StatementContext,i)


        def END(self):
            return self.getToken(LALGParser.END, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.SEMICOLON)
            else:
                return self.getToken(LALGParser.SEMICOLON, i)

        def getRuleIndex(self):
            return LALGParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)




    def compoundStatement(self):

        localctx = LALGParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(LALGParser.BEGIN)
            self.state = 123
            self.statement()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 124
                self.match(LALGParser.SEMICOLON)
                self.state = 125
                self.statement()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(LALGParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(LALGParser.AssignmentStatementContext,0)


        def procedureCallStatement(self):
            return self.getTypedRuleContext(LALGParser.ProcedureCallStatementContext,0)


        def ioProcedureCallStatement(self):
            return self.getTypedRuleContext(LALGParser.IoProcedureCallStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(LALGParser.CompoundStatementContext,0)


        def conditionalStatement(self):
            return self.getTypedRuleContext(LALGParser.ConditionalStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(LALGParser.LoopStatementContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = LALGParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.procedureCallStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.ioProcedureCallStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.compoundStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.conditionalStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.loopStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(LALGParser.VariableContext,0)


        def ASSIGNMENT(self):
            return self.getToken(LALGParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(LALGParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)




    def assignmentStatement(self):

        localctx = LALGParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.variable()
            self.state = 142
            self.match(LALGParser.ASSIGNMENT)
            self.state = 143
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureCallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LALGParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(LALGParser.LP, 0)

        def expressionList(self):
            return self.getTypedRuleContext(LALGParser.ExpressionListContext,0)


        def RP(self):
            return self.getToken(LALGParser.RP, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_procedureCallStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedureCallStatement" ):
                listener.enterProcedureCallStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedureCallStatement" ):
                listener.exitProcedureCallStatement(self)




    def procedureCallStatement(self):

        localctx = LALGParser.ProcedureCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_procedureCallStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(LALGParser.IDENTIFIER)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 146
                self.match(LALGParser.LP)
                self.state = 147
                self.expressionList()
                self.state = 148
                self.match(LALGParser.RP)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LALGParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(LALGParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(LALGParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.StatementContext)
            else:
                return self.getTypedRuleContext(LALGParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(LALGParser.ELSE, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_conditionalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalStatement" ):
                listener.enterConditionalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalStatement" ):
                listener.exitConditionalStatement(self)




    def conditionalStatement(self):

        localctx = LALGParser.ConditionalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_conditionalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(LALGParser.IF)
            self.state = 153
            self.expression()
            self.state = 154
            self.match(LALGParser.THEN)
            self.state = 155
            self.statement()
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 156
                self.match(LALGParser.ELSE)
                self.state = 157
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LALGParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(LALGParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(LALGParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(LALGParser.StatementContext,0)


        def getRuleIndex(self):
            return LALGParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)




    def loopStatement(self):

        localctx = LALGParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(LALGParser.WHILE)
            self.state = 161
            self.expression()
            self.state = 162
            self.match(LALGParser.DO)
            self.state = 163
            self.statement()
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

        def simpleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.SimpleExpressionContext)
            else:
                return self.getTypedRuleContext(LALGParser.SimpleExpressionContext,i)


        def relationalOperator(self):
            return self.getTypedRuleContext(LALGParser.RelationalOperatorContext,0)


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
        self.enterRule(localctx, 32, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.simpleExpression()
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 166
                self.relationalOperator()
                self.state = 167
                self.simpleExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(LALGParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(LALGParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(LALGParser.LESS_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(LALGParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(LALGParser.GREATER_THAN_OR_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(LALGParser.GREATER_THAN, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_relationalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalOperator" ):
                listener.enterRelationalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalOperator" ):
                listener.exitRelationalOperator(self)




    def relationalOperator(self):

        localctx = LALGParser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
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


    class SimpleExpressionContext(ParserRuleContext):
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
            return LALGParser.RULE_simpleExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpression" ):
                listener.enterSimpleExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpression" ):
                listener.exitSimpleExpression(self)




    def simpleExpression(self):

        localctx = LALGParser.SimpleExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_simpleExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18 or _la==19:
                self.state = 173
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 176
            self.term()
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 177
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9175040) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 178
                    self.term() 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.DIV)
            else:
                return self.getToken(LALGParser.DIV, i)

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
        self.enterRule(localctx, 38, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.factor()
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 185
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24117248) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 186
                    self.factor() 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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


        def literal(self):
            return self.getTypedRuleContext(LALGParser.LiteralContext,0)


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
        self.enterRule(localctx, 40, self.RULE_factor)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.variable()
                pass
            elif token in [41, 42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.number()
                pass
            elif token in [15, 16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.literal()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.match(LALGParser.LP)
                self.state = 196
                self.expression()
                self.state = 197
                self.match(LALGParser.RP)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 199
                self.match(LALGParser.NOT)
                self.state = 200
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
        self.enterRule(localctx, 42, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(LALGParser.IDENTIFIER)
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 204
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LALGParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LALGParser.COMMA)
            else:
                return self.getToken(LALGParser.COMMA, i)

        def getRuleIndex(self):
            return LALGParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = LALGParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.expression()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 208
                self.match(LALGParser.COMMA)
                self.state = 209
                self.expression()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 46, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL_TRUE(self):
            return self.getToken(LALGParser.LITERAL_TRUE, 0)

        def LITERAL_FALSE(self):
            return self.getToken(LALGParser.LITERAL_FALSE, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = LALGParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
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


    class IoProcedureCallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(LALGParser.LP, 0)

        def variable(self):
            return self.getTypedRuleContext(LALGParser.VariableContext,0)


        def RP(self):
            return self.getToken(LALGParser.RP, 0)

        def READ_PROCEDURE(self):
            return self.getToken(LALGParser.READ_PROCEDURE, 0)

        def WRITE_PROCEDURE(self):
            return self.getToken(LALGParser.WRITE_PROCEDURE, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_ioProcedureCallStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIoProcedureCallStatement" ):
                listener.enterIoProcedureCallStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIoProcedureCallStatement" ):
                listener.exitIoProcedureCallStatement(self)




    def ioProcedureCallStatement(self):

        localctx = LALGParser.IoProcedureCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_ioProcedureCallStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 220
            self.match(LALGParser.LP)
            self.state = 221
            self.variable()
            self.state = 222
            self.match(LALGParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






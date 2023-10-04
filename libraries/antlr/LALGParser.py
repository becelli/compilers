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
        4,
        1,
        47,
        45,
        2,
        0,
        7,
        0,
        2,
        1,
        7,
        1,
        2,
        2,
        7,
        2,
        2,
        3,
        7,
        3,
        2,
        4,
        7,
        4,
        2,
        5,
        7,
        5,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        2,
        1,
        2,
        5,
        2,
        25,
        8,
        2,
        10,
        2,
        12,
        2,
        28,
        9,
        2,
        1,
        2,
        1,
        2,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        4,
        1,
        4,
        1,
        5,
        1,
        5,
        1,
        5,
        5,
        5,
        40,
        8,
        5,
        10,
        5,
        12,
        5,
        43,
        9,
        5,
        1,
        5,
        0,
        0,
        6,
        0,
        2,
        4,
        6,
        8,
        10,
        0,
        1,
        1,
        0,
        4,
        5,
        40,
        0,
        12,
        1,
        0,
        0,
        0,
        2,
        19,
        1,
        0,
        0,
        0,
        4,
        21,
        1,
        0,
        0,
        0,
        6,
        31,
        1,
        0,
        0,
        0,
        8,
        34,
        1,
        0,
        0,
        0,
        10,
        36,
        1,
        0,
        0,
        0,
        12,
        13,
        5,
        1,
        0,
        0,
        13,
        14,
        5,
        40,
        0,
        0,
        14,
        15,
        5,
        32,
        0,
        0,
        15,
        16,
        3,
        2,
        1,
        0,
        16,
        17,
        5,
        35,
        0,
        0,
        17,
        18,
        5,
        0,
        0,
        1,
        18,
        1,
        1,
        0,
        0,
        0,
        19,
        20,
        3,
        4,
        2,
        0,
        20,
        3,
        1,
        0,
        0,
        0,
        21,
        26,
        3,
        6,
        3,
        0,
        22,
        23,
        5,
        32,
        0,
        0,
        23,
        25,
        3,
        6,
        3,
        0,
        24,
        22,
        1,
        0,
        0,
        0,
        25,
        28,
        1,
        0,
        0,
        0,
        26,
        24,
        1,
        0,
        0,
        0,
        26,
        27,
        1,
        0,
        0,
        0,
        27,
        29,
        1,
        0,
        0,
        0,
        28,
        26,
        1,
        0,
        0,
        0,
        29,
        30,
        5,
        32,
        0,
        0,
        30,
        5,
        1,
        0,
        0,
        0,
        31,
        32,
        3,
        8,
        4,
        0,
        32,
        33,
        3,
        10,
        5,
        0,
        33,
        7,
        1,
        0,
        0,
        0,
        34,
        35,
        7,
        0,
        0,
        0,
        35,
        9,
        1,
        0,
        0,
        0,
        36,
        41,
        5,
        40,
        0,
        0,
        37,
        38,
        5,
        34,
        0,
        0,
        38,
        40,
        5,
        40,
        0,
        0,
        39,
        37,
        1,
        0,
        0,
        0,
        40,
        43,
        1,
        0,
        0,
        0,
        41,
        39,
        1,
        0,
        0,
        0,
        41,
        42,
        1,
        0,
        0,
        0,
        42,
        11,
        1,
        0,
        0,
        0,
        43,
        41,
        1,
        0,
        0,
        0,
        2,
        26,
        41,
    ]


class LALGParser(Parser):
    grammarFileName = "LALGParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "'program'",
        "'procedure'",
        "'var'",
        "'int'",
        "'boolean'",
        "'begin'",
        "'end'",
        "'if'",
        "'then'",
        "'else'",
        "'while'",
        "'do'",
        "'read'",
        "'write'",
        "'true'",
        "'false'",
        "':='",
        "'+'",
        "'-'",
        "'*'",
        "'/'",
        "'div'",
        "'or'",
        "'and'",
        "'not'",
        "'='",
        "'<>'",
        "'<'",
        "'>'",
        "'<='",
        "'>='",
        "';'",
        "':'",
        "','",
        "'.'",
        "'('",
        "')'",
        "'['",
        "']'",
    ]

    symbolicNames = [
        "<INVALID>",
        "PROGRAM",
        "PROCEDURE",
        "VAR",
        "TYPE_INT",
        "TYPE_BOOL",
        "BEGIN",
        "END",
        "IF",
        "THEN",
        "ELSE",
        "WHILE",
        "DO",
        "PROC_READ",
        "PROC_WRITE",
        "CONST_TRUE",
        "CONST_FALSE",
        "ATTRIB",
        "SUM",
        "SUB",
        "MUL",
        "DIV",
        "INT_DIV",
        "OR",
        "AND",
        "NOT",
        "EQUAL",
        "DIFF",
        "LT",
        "GT",
        "LTE",
        "GTE",
        "SEMICOLON",
        "COLON",
        "COMMA",
        "DOT",
        "LP",
        "RP",
        "LB",
        "RB",
        "IDENTIFIER",
        "INT",
        "REAL",
        "COMMENT",
        "MULTILINE_COMMENT",
        "WS",
        "INVALID_TOKEN",
        "INVALID",
    ]

    RULE_program = 0
    RULE_block = 1
    RULE_variableDeclarationSection = 2
    RULE_variableDeclaration = 3
    RULE_type = 4
    RULE_identifierList = 5

    ruleNames = [
        "program",
        "block",
        "variableDeclarationSection",
        "variableDeclaration",
        "type",
        "identifierList",
    ]

    EOF = Token.EOF
    PROGRAM = 1
    PROCEDURE = 2
    VAR = 3
    TYPE_INT = 4
    TYPE_BOOL = 5
    BEGIN = 6
    END = 7
    IF = 8
    THEN = 9
    ELSE = 10
    WHILE = 11
    DO = 12
    PROC_READ = 13
    PROC_WRITE = 14
    CONST_TRUE = 15
    CONST_FALSE = 16
    ATTRIB = 17
    SUM = 18
    SUB = 19
    MUL = 20
    DIV = 21
    INT_DIV = 22
    OR = 23
    AND = 24
    NOT = 25
    EQUAL = 26
    DIFF = 27
    LT = 28
    GT = 29
    LTE = 30
    GTE = 31
    SEMICOLON = 32
    COLON = 33
    COMMA = 34
    DOT = 35
    LP = 36
    RP = 37
    LB = 38
    RB = 39
    IDENTIFIER = 40
    INT = 41
    REAL = 42
    COMMENT = 43
    MULTILINE_COMMENT = 44
    WS = 45
    INVALID_TOKEN = 46
    INVALID = 47

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class ProgramContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(LALGParser.PROGRAM, 0)

        def IDENTIFIER(self):
            return self.getToken(LALGParser.IDENTIFIER, 0)

        def SEMICOLON(self):
            return self.getToken(LALGParser.SEMICOLON, 0)

        def block(self):
            return self.getTypedRuleContext(LALGParser.BlockContext, 0)

        def DOT(self):
            return self.getToken(LALGParser.DOT, 0)

        def EOF(self):
            return self.getToken(LALGParser.EOF, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_program

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)

    def program(self):
        localctx = LALGParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(LALGParser.PROGRAM)
            self.state = 13
            self.match(LALGParser.IDENTIFIER)
            self.state = 14
            self.match(LALGParser.SEMICOLON)
            self.state = 15
            self.block()
            self.state = 16
            self.match(LALGParser.DOT)
            self.state = 17
            self.match(LALGParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarationSection(self):
            return self.getTypedRuleContext(
                LALGParser.VariableDeclarationSectionContext, 0
            )

        def getRuleIndex(self):
            return LALGParser.RULE_block

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBlock"):
                listener.enterBlock(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBlock"):
                listener.exitBlock(self)

    def block(self):
        localctx = LALGParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.variableDeclarationSection()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationSectionContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(LALGParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(
                    LALGParser.VariableDeclarationContext, i
                )

        def SEMICOLON(self, i: int = None):
            if i is None:
                return self.getTokens(LALGParser.SEMICOLON)
            else:
                return self.getToken(LALGParser.SEMICOLON, i)

        def getRuleIndex(self):
            return LALGParser.RULE_variableDeclarationSection

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVariableDeclarationSection"):
                listener.enterVariableDeclarationSection(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVariableDeclarationSection"):
                listener.exitVariableDeclarationSection(self)

    def variableDeclarationSection(self):
        localctx = LALGParser.VariableDeclarationSectionContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 4, self.RULE_variableDeclarationSection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.variableDeclaration()
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 0, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 22
                    self.match(LALGParser.SEMICOLON)
                    self.state = 23
                    self.variableDeclaration()
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 0, self._ctx)

            self.state = 29
            self.match(LALGParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(LALGParser.TypeContext, 0)

        def identifierList(self):
            return self.getTypedRuleContext(LALGParser.IdentifierListContext, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_variableDeclaration

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVariableDeclaration"):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVariableDeclaration"):
                listener.exitVariableDeclaration(self)

    def variableDeclaration(self):
        localctx = LALGParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.type_()
            self.state = 32
            self.identifierList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_BOOL(self):
            return self.getToken(LALGParser.TYPE_BOOL, 0)

        def TYPE_INT(self):
            return self.getToken(LALGParser.TYPE_INT, 0)

        def getRuleIndex(self):
            return LALGParser.RULE_type

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterType"):
                listener.enterType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitType"):
                listener.exitType(self)

    def type_(self):
        localctx = LALGParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not (_la == 4 or _la == 5):
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

    class IdentifierListContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i: int = None):
            if i is None:
                return self.getTokens(LALGParser.IDENTIFIER)
            else:
                return self.getToken(LALGParser.IDENTIFIER, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(LALGParser.COMMA)
            else:
                return self.getToken(LALGParser.COMMA, i)

        def getRuleIndex(self):
            return LALGParser.RULE_identifierList

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIdentifierList"):
                listener.enterIdentifierList(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIdentifierList"):
                listener.exitIdentifierList(self)

    def identifierList(self):
        localctx = LALGParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifierList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(LALGParser.IDENTIFIER)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 34:
                self.state = 37
                self.match(LALGParser.COMMA)
                self.state = 38
                self.match(LALGParser.IDENTIFIER)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

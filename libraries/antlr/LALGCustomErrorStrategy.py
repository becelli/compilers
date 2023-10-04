from antlr4 import Parser, Token
from antlr4.Parser import Parser
from antlr4.Token import Token
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.Errors import RecognitionException
from libraries.antlr.LALGParser import LALGParser


class LALGCustomErrorStrategy(DefaultErrorStrategy):
    def recover(self, recognizer: Parser, exception: RecognitionException):
        super().recover(recognizer, exception)

        inputStream = recognizer.getInputStream()
        startIndex = int(inputStream.index)
        while inputStream.LA(1) != Token.EOF:
            currentTokenType = inputStream.LA(1)
            if currentTokenType in self.startTokens:
                break
            else:
                recognizer.consume()

        if inputStream.LA(1) == Token.EOF:
            inputStream.seek(startIndex)

    @property
    def startTokens(self) -> set:
        return {
            LALGParser.PROGRAM,
            LALGParser.PROCEDURE,
            LALGParser.VAR,
            LALGParser.BEGIN,
            LALGParser.IF,
            LALGParser.WHILE,
            LALGParser.END,
            LALGParser.DO,
            LALGParser.THEN,
            LALGParser.ELSE,
            Token.EOF,
        }

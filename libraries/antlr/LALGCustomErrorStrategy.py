from re import I

from antlr4 import Parser, Token
from antlr4.Lexer import LexerNoViableAltException
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.Errors import (
    FailedPredicateException,
    InputMismatchException,
    NoViableAltException,
    RecognitionException,
)

class LALGCustomErrorStrategy(DefaultErrorStrategy):
    def reportError(self, recognizer: Parser, exception: RecognitionException):
        if self.inErrorRecoveryMode(recognizer):
            return
            
        self.beginErrorCondition(recognizer)
        match exception:
            case LexerNoViableAltException():
                self.reportLexerError(recognizer, exception)
            case NoViableAltException():
                self.reportNoViableAlternative(recognizer, exception)
            case InputMismatchException():
                self.reportInputMismatch(recognizer, exception)
            case FailedPredicateException():
                self.reportFailedPredicate(recognizer, exception)
            case _:
                print(f"Unknown recognition error: {exception}")
                token = recognizer.getCurrentToken()
                expected = self.getExpectedTokensString(recognizer, exception)
                msg = f"Error on line {token.line}, column {token.column}: unexpected token {token.text}, expected {expected}.\n{exception.message}"
                recognizer.notifyErrorListeners(msg, token, exception)

    def reportLexerError(self, recognizer: Parser, exception: LexerNoViableAltException):
        line, column = exception.startIndex, exception.startIndex + 1
        currentToken = recognizer.getCurrentToken()
        inputVal = self.getInputTokenValue(recognizer, exception)
        formattedInputVal = self.escapeWSAndQuote(inputVal)
        msg = f"Error on line {line}, column {column}: unrecognized input {formattedInputVal}."
        recognizer.notifyErrorListeners(msg, currentToken, exception)

    def reportInputMismatch(self, recognizer: Parser, exception: InputMismatchException):
        line, column = exception.offendingToken.line, exception.offendingToken.column
        errDisplay = self.getTokenErrorDisplay(exception.offendingToken)[1:-1]
        expected = self.getExpectedTokensString(recognizer, exception)
        msg = f"Error on line {line}, column {column}: unrecognized input {errDisplay}, expected {expected}."
        recognizer.notifyErrorListeners(msg, exception.offendingToken, exception)

    def reportNoViableAlternative(self, recognizer: Parser, exception: NoViableAltException):
        line, column = exception.offendingToken.line, exception.offendingToken.column
        inputVal = self.getInputTokenValue(recognizer, exception)
        formattedInputVal = self.escapeWSAndQuote(inputVal)
        msg = f"Error on line {line}, column {column}: unrecognized input {formattedInputVal}."
        recognizer.notifyErrorListeners(msg, exception.offendingToken, exception)

    def reportFailedPredicate(self, recognizer, exception: FailedPredicateException):
        line, column = exception.offendingToken.line, exception.offendingToken.column
        ruleName = recognizer.ruleNames[recognizer._ctx.getRuleIndex()]
        msg = f"Error on line {line}, column {column}, rule {ruleName}: {exception.message}"
        recognizer.notifyErrorListeners(msg, exception.offendingToken, exception)

    def getExpectedTokensString(self, recognizer: Parser, exception: RecognitionException):
        expectedTokens = exception.getExpectedTokens()
        if expectedTokens is None:
            return "<unknown token>"

        return expectedTokens.toString(recognizer.literalNames, recognizer.symbolicNames)  # type: ignore

    def getInputTokenValue(self, recognizer, exception):
        tokens = recognizer.getTokenStream()
        if tokens is not None:
            return "<EOF>" if exception.startToken.type == Token.EOF else tokens.getText(exception.startToken, exception.offendingToken)
        return "<unknown token>"
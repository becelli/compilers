from PyQt6.QtWidgets import QTextEdit
from antlr4.error.ErrorListener import ErrorListener as AntlrErrorListener


class LALGErrorListener(AntlrErrorListener):
    def __init__(self, errorOutput: QTextEdit) -> None:
        super().__init__()
        self.errorOutput = errorOutput

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errorOutput.append(f"Syntax error on line {line}, column {column}: {msg}")

    def lexerError(self, line, column, msg):
        self.errorOutput.append(f"Lexer error on line {line}, column {column}: {msg}")

    def reportAmbiguity(
        self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs
    ):
        pass
        # self.errorOutput.append(
        #     f"Ambiguity detected between tokens at positions {startIndex} and {stopIndex}. "
        #     f"Alternative interpretations: {ambigAlts}. Exact match: {exact}"
        # )

    def reportAttemptingFullContext(
        self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs
    ):
        pass
        # self.errorOutput.append(
        #     f"Attempting full context parsing due to conflict between tokens at positions "
        #     f"{startIndex} and {stopIndex}. Conflicting interpretations: {conflictingAlts}"
        # )

    def reportContextSensitivity(
        self, recognizer, dfa, startIndex, stopIndex, prediction, configs
    ):
        pass
        # self.errorOutput.append(
        #     f"Context sensitivity detected when predicting token type {prediction} between "
        #     f"positions {startIndex} and {stopIndex}"
        # )

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

    def semanticError(self, line, column, msg):
        self.errorOutput.append(f"Semantic error on line {line}, column {column}: {msg}")

    def log(self, message):
        self.errorOutput.append(message)
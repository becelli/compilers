from antlr4.error.ErrorListener import ErrorListener as AntlrErrorListener

class LALGErrorListener(AntlrErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Error on line {line}, column {column}: {msg}")

    def getErrorMessage(self):
        return ''.join(self.errors) if self.errors else ''

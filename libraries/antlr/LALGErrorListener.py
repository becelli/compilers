from antlr4.error.ErrorListener import ErrorListener as AntlrErrorListener

class LALGErrorListener(AntlrErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Error on line {line}, column {column}: {msg}")

    def lexicalError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Error on line {line}, column {column}: {msg}")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
    
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

    def getErrorMessage(self):
        return '\n'.join(self.errors) if self.errors else ''

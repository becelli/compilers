from antlr4.error.ErrorListener import ErrorListener as AntlrErrorListener


class LALGErrorListener(AntlrErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Syntax error on line {line}, column {column}: {msg}")

    def lexerError(self, line, column, msg):
        self.errors.append(f"Lexer error on line {line}, column {column}: {msg}")

    def reportAmbiguity(
        self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs
    ):
        self.errors.append(
            f"Ambiguity detected between tokens at positions {startIndex} and {stopIndex}. "
            f"Alternative interpretations: {ambigAlts}. Exact match: {exact}"
        )

    def reportAttemptingFullContext(
        self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs
    ):
        self.errors.append(
            f"Attempting full context parsing due to conflict between tokens at positions "
            f"{startIndex} and {stopIndex}. Conflicting interpretations: {conflictingAlts}"
        )

    def reportContextSensitivity(
        self, recognizer, dfa, startIndex, stopIndex, prediction, configs
    ):
        self.errors.append(
            f"Context sensitivity detected when predicting token type {prediction} between "
            f"positions {startIndex} and {stopIndex}"
        )

    def getErrorMessage(self):
        return "\n".join(self.errors) if self.errors else ""

from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, charPositionInLine, msg, e):
        raise Exception(f"Error at {line}:{charPositionInLine} -> {msg}")

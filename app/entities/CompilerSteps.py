from enum import Enum


class CompilerSteps(Enum):
    LEXER = "lexer"
    SYNTAX = "syntax"
    SEMANTIC = "semantic"

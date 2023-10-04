# Generated from libraries/antlr/LALGParser.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .LALGParser import LALGParser
else:
    from LALGParser import LALGParser


# This class defines a complete listener for a parse tree produced by LALGParser.
class LALGParserListener(ParseTreeListener):
    # Enter a parse tree produced by LALGParser#program.
    def enterProgram(self, ctx: LALGParser.ProgramContext):
        pass

    # Exit a parse tree produced by LALGParser#program.
    def exitProgram(self, ctx: LALGParser.ProgramContext):
        pass

    # Enter a parse tree produced by LALGParser#block.
    def enterBlock(self, ctx: LALGParser.BlockContext):
        pass

    # Exit a parse tree produced by LALGParser#block.
    def exitBlock(self, ctx: LALGParser.BlockContext):
        pass

    # Enter a parse tree produced by LALGParser#variableDeclarationSection.
    def enterVariableDeclarationSection(
        self, ctx: LALGParser.VariableDeclarationSectionContext
    ):
        pass

    # Exit a parse tree produced by LALGParser#variableDeclarationSection.
    def exitVariableDeclarationSection(
        self, ctx: LALGParser.VariableDeclarationSectionContext
    ):
        pass

    # Enter a parse tree produced by LALGParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx: LALGParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by LALGParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx: LALGParser.VariableDeclarationContext):
        pass

    # Enter a parse tree produced by LALGParser#type.
    def enterType(self, ctx: LALGParser.TypeContext):
        pass

    # Exit a parse tree produced by LALGParser#type.
    def exitType(self, ctx: LALGParser.TypeContext):
        pass

    # Enter a parse tree produced by LALGParser#identifierList.
    def enterIdentifierList(self, ctx: LALGParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by LALGParser#identifierList.
    def exitIdentifierList(self, ctx: LALGParser.IdentifierListContext):
        pass


del LALGParser

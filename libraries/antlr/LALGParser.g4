parser grammar LALGParser;
options {
	tokenVocab = LALGLexer;
}

program: PROGRAM IDENTIFIER SEMICOLON block DOT;

block: variableDeclarationSection;

variableDeclarationSection:
	variableDeclaration (SEMICOLON variableDeclaration)* SEMICOLON EOF;

variableDeclaration: type identifierList;

type: (TYPE_BOOL | TYPE_INT);

identifierList: IDENTIFIER (COMMA IDENTIFIER)*;


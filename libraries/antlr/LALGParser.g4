parser grammar LALGParser;
options {
	tokenVocab = LALGLexer;
}

program: PROGRAM IDENTIFIER SEMICOLON block DOT EOF;

block: variableDeclarationSection;

variableDeclarationSection: variableDeclaration (SEMICOLON variableDeclaration)* SEMICOLON;

variableDeclaration: type identifierList;

type: (TYPE_BOOL | TYPE_INT);

identifierList: IDENTIFIER (COMMA IDENTIFIER)*;


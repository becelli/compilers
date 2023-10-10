parser grammar LALGParser;
options {
	tokenVocab = LALGLexer;
}

// Declaration
program: PROGRAM IDENTIFIER SEMICOLON block DOT EOF;

block:
	variableDeclarationSection subroutineDeclarationSection compoundStatement;

variableDeclarationSection:
	variableDeclaration (SEMICOLON variableDeclaration)* SEMICOLON;

variableDeclaration: type identifierList;

type: (TYPE_BOOL | TYPE_INT);

identifierList: IDENTIFIER (COMMA IDENTIFIER)*;

subroutineDeclarationSection: (procedureDeclaration SEMICOLON)*;

procedureDeclaration: PROCEDURE IDENTIFIER formalParameterList? SEMICOLON block;

formalParameterList: LP formalParameterSection (SEMICOLON formalParameterSection)* RP;

formalParameterSection: VAR identifierList COLON IDENTIFIER;

// Commands
compoundStatement: BEGIN statement (SEMICOLON statement)* END;

statement:
	assignmentStatement
	| procedureCallStatement
	| compoundStatement
	| conditionalStatement
	| loopStatement;

assignmentStatement: variable ASSIGNMENT expression;

procedureCallStatement: IDENTIFIER expressionList?;

conditionalStatement: IF expression THEN statement (ELSE statement)?;

loopStatement: WHILE expression DO statement;

// Expressions

expression: simpleExpression (relationalOperator simpleExpression)?;

relationalOperator: EQ | NE | LT | LTE | GTE | GT;

simpleExpression: (SUM | SUB)? term ((SUM | SUB | OR) term)*;

term: factor ((MUL | DIV | AND) factor)*;

factor:
	variable
	| number
	| LP expression RP
	| NOT factor;

variable: IDENTIFIER expression?;

expressionList: expression (COMMA expression)*;

number: INT | REAL;
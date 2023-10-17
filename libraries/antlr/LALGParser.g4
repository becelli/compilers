parser grammar LALGParser;
options {
	tokenVocab = LALGLexer;
}

// Declaration
program: PROGRAM IDENTIFIER SEMICOLON block DOT EOF;

type: (TYPE_BOOL | TYPE_INT);

block:
	variableDeclarationSection? subroutineDeclarationSection? compoundStatement;

// Variable declaration
variableDeclarationSection:
	variableDeclaration (SEMICOLON variableDeclaration)* SEMICOLON;

variableDeclaration: type identifierList;

// add semicolon to this?
identifierList: IDENTIFIER (COMMA IDENTIFIER)*;

// Subroutine declaration
subroutineDeclarationSection: (procedureDeclaration SEMICOLON)*;

procedureDeclaration:
	PROCEDURE IDENTIFIER formalParameterList? SEMICOLON block;

formalParameterList:
	LP formalParameterSection (SEMICOLON formalParameterSection)* RP;

formalParameterSection: VAR identifierList COLON type;

// Commands
compoundStatement: BEGIN statement (SEMICOLON statement)* END;

statement:
	assignmentStatement
	| procedureCallStatement
	| ioProcedureCallStatement
	| compoundStatement
	| conditionalStatement
	| loopStatement;

assignmentStatement: variable ASSIGNMENT expression;

procedureCallStatement: IDENTIFIER (LP expressionList RP)?;

conditionalStatement:
	IF expression THEN statement (ELSE statement)?;

loopStatement: WHILE expression DO statement;

// Expressions

expression:
	simpleExpression (relationalOperator simpleExpression)?;

relationalOperator:
	EQUAL
	| NOT_EQUAL
	| LESS_THAN
	| LESS_THAN_OR_EQUAL
	| GREATER_THAN_OR_EQUAL
	| GREATER_THAN;

simpleExpression: (SUM | SUB)? term ((SUM | SUB | OR) term)*;

term: factor ((MUL | DIV | INT_DIV | AND) factor)*;

factor:
	variable
	| number
	| literal
	| LP expression RP
	| NOT factor;

variable: IDENTIFIER expression?;

expressionList: expression (COMMA expression)*;

number: INT | REAL;

literal: LITERAL_TRUE | LITERAL_FALSE;

ioProcedureCallStatement: (READ_PROCEDURE | WRITE_PROCEDURE) LP variable RP;


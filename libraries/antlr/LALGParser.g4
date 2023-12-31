parser grammar LALGParser;
options {
	tokenVocab = LALGLexer;
}

// Declaration
program: PROGRAM IDENTIFIER SEMICOLON block DOT EOF;

type: (TYPE_BOOL | TYPE_INT);

// subroutineDeclarationSection could be empty, so even though it should be optional here, it is
// being declared as a obligatory. This happens because if we don't do that, ANTLR4 will not be able
// to identify if: 1 - The rule is present, but empty 2 - The rule is not present at all error
// message: rule block contains an optional block with at least one alternative that can match an
// empty string
block:
	variableDeclarationSection? subroutineDeclarationSection compoundStatement;

// Variable declaration
variableDeclarationSection:
	variableDeclaration (SEMICOLON variableDeclaration)* SEMICOLON;

variableDeclaration: type identifierList;

identifierList: IDENTIFIER (COMMA IDENTIFIER)*;

// Subroutine declaration
subroutineDeclarationSection: (procedureDeclaration SEMICOLON)*;

procedureDeclaration:
	PROCEDURE IDENTIFIER formalParameterList? SEMICOLON block;

formalParameterList:
	LP formalParameterSection (SEMICOLON formalParameterSection)* RP;

formalParameterSection: VAR? identifierList COLON type;

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

conditionalStatement: IF expression statement (ELSE statement)?;

loopStatement: WHILE LP expression RP statement;

expression:
	additiveExpression (relationalOperator additiveExpression)?;

additiveExpression:
	multiplicativeExpression (
		additiveOperator multiplicativeExpression
	)*;

multiplicativeExpression:
	unaryExpression (multiplicativeOperator unaryExpression)*;

unaryExpression: unaryOperator? primaryExpression;

primaryExpression:
	variable
	| number
	| literal
	| LP expression RP;

additiveOperator: SUM | SUB | OR;

multiplicativeOperator: MUL | DIV | INT_DIV | AND;

unaryOperator: SUM | SUB | NOT;

relationalOperator:
	EQUAL
	| NOT_EQUAL
	| LESS_THAN
	| LESS_THAN_OR_EQUAL
	| GREATER_THAN_OR_EQUAL
	| GREATER_THAN;

variable: IDENTIFIER;

expressionList: expression (COMMA expression)*;

number: INT | REAL;

literal: LITERAL_TRUE | LITERAL_FALSE;

ioProcedureCallStatement: (READ_PROCEDURE | WRITE_PROCEDURE) LP variable (
		COMMA variable
	)* RP;
lexer grammar LALGLexer;

// Keywords
PROGRAM: 'program';
PROCEDURE: 'procedure';
VAR: 'var';
TYPE_INT: 'int';
TYPE_BOOL: 'boolean';
BEGIN: 'begin';
END: 'end';
IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';
DO: 'do';
READ_PROCEDURE: 'read';
WRITE_PROCEDURE: 'write';
LITERAL_TRUE: 'true';
LITERAL_FALSE: 'false';

// Operators
ASSIGNMENT: ':=';
SUM: '+';
SUB: '-';
MUL: '*';
DIV: '/';
INT_DIV: 'div';
OR: 'or';
AND: 'and';
NOT: 'not';

// Relational operators
EQUAL: '=';
NOT_EQUAL: '<>';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';

// Punctuation
SEMICOLON: ';';
COLON: ':';
COMMA: ',';
DOT: '.';
LP: '(';
RP: ')';
LB: '[';
RB: ']';

// Identifier
fragment LETTER: '_' | [A-Z] | [a-z];
fragment DIGIT: [0-9];
// IDENTIFIER: LETTER (LETTER | DIGIT)*;

IDENTIFIER: LETTER (LETTER | DIGIT)*;

// Numbers
INT: DIGIT+;
REAL: DIGIT+ '.' DIGIT+;

// Comments and whitespace
COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '{' .*? '}' -> skip;
WS: [ \t\n\r\f]+ -> skip;

// Invalid token
INVALID_TOKEN: INVALID+?;
INVALID: .;
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
PROC_READ: 'read';
PROC_WRITE: 'write';
CONST_TRUE: 'true';
CONST_FALSE: 'false';

// Operators
ATTRIB: ':=';
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
DIFF: '<>';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

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
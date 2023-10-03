// Base ANTLR para o analisador léxico
// Calculadora
// Autores:
// Daniel Serezane
// Gabriel Nozawa
lexer grammar LangLexer;

// Regras da LALG

// Palavras reservadas
PROGRAM: 'program';
PROCEDURE: 'procedure';
SEMICOLON: ';';
ATTRIB: ':=';
COLON: ':';
COMMA: ',';
VAR: 'var';
TYPE_INT: 'int';
TYPE_BOOL: 'boolean';
PROC_READ: 'read';
PROC_WRITE: 'write';
CONST_TRUE: 'true';
CONST_FALSE: 'false';
BEGIN: 'begin';
END: 'end';
IF: 'if';
THEN: 'then';
ELSE: 'else';
OR: 'or';
AND: 'and';
NOT: 'not';
SUM: '+';
MUL: '*';
DIV: '/';
INT_DIV: 'div';
SUB: '-';
LP: '(';
RP: ')';
LB: '[';
RB: ']';
WHILE: 'while';
DO: 'do';
DOT: '.';
// Relações
EQUAL: '=';
DIFF: '<>';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

fragment LETRA: '_'|[A-Z]|[a-z];
fragment DIGITO: [0-9];
IDENTIFICADOR: (LETRA)(LETRA|DIGITO)*;


INT: [0-9]+;
REAL: [0-9]+'.'[0-9]+;

COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '{' .*? '}' -> skip;
//COMMENT_MULTILINE: '{'(~'}')*'}' ;

WS: [ \t\n\r\f]+ -> skip ;

INVALID_TOKEN: INVALID+? ;
INVALID: . ;
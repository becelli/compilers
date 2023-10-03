parser grammar lalg_parser;
options {
	tokenVocab = lalg_lexer;
}

number: INT | REAL;

relation_operator: EQUAL | DIFF | LT | LTE | GT | GTE;

factor: variable | number | LP expression RP | NOT factor;

term: factor ( ( MUL | INT_DIV | AND) factor)*;

simple_expression: ( SUM | SUB)? term ( ( SUM | SUB | OR) term)*;

expression:
	simple_expression (relation_operator simple_expression)?;

variable: IDENTIFIER | IDENTIFIER expression;
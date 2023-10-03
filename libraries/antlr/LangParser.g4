parser grammar LangParser;
options { tokenVocab=LangLexer; }

numero: (INT | REAL);

relacao:
    ( EQUAL | DIFF | LT | LTE | GT | GTE ) ;

termo:
    fator ( ( MUL | INT_DIV | AND ) fator )* ;

expressaoSimples:
    ( SUM | SUB )? termo ( ( SUM | SUB | OR ) termo )* ;

expressao:
    expressaoSimples (relacao expressaoSimples)? ;

fator:
    ( variavel | numero | ( LP expressao RP ) | ( NOT fator ) ) ;

variavel:
    ( IDENTIFICADOR | ( IDENTIFICADOR expressao ) );
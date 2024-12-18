grammar scheme;

root : expr+ EOF                                           
     ;

expr : OP                                              # op
     | NUM                                             # numero
     | ID                                              # identificador
     | STRING                                          # text
     | '\''? '(' expr* ')'                             # llamada
     ;

// Reglas para números
NUM : ('+' | '-')? [0-9]+;
OP : ('*' | '/' | '+' | '-' | '>' | '<' | '>=' | '<=' | '=' | '<>');
ID : [a-zA-Z][a-zA-Z0-9]*;
STRING : '"' (~[\r\n"] | '""')* '"';
WS : [ \t\r\n]+ -> skip;



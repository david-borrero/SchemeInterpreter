grammar scheme;

root : expr+ EOF                                           
     ;

expr : OP                                              # op
     | NUM                                             # numero
     | ID                                              # identificador
     | STRING                                          # text
     | TRUE                                            # true
     | FALSE                                           # false
     | '\''? '(' expr* ')'                             # llamada
     ;

// Reglas para números
NUM : ('+' | '-')? [0-9]+;
OP : ('*' | '/' | 'mod' | '+' | '-' | '>' | '<' | '>=' | '<=' | '=' | '<>');
ID: [a-zA-Z] [a-zA-Z0-9?\-]*;
STRING : '"' (~[\r\n"] | '""')* '"';
TRUE : '#t';
FALSE : '#f';

WS : [ \t\r\n]+ -> skip;
COMMENT : ';' ~[\r\n]* -> skip;


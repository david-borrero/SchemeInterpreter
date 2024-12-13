grammar scheme;

root : expr+ EOF                                           
     ;

expr : OP                                              # op
     | NUM                                             # numero
     | ID                                              # identificador
     | '\''? '(' expr* ')'                             # llamada
     ;

// Reglas para números
NUM : ('+' | '-')? [0-9]+;

OP : ('*' | '/' | '+' | '-' | '>' | '<' | '>=' | '<=' | '=' | '<>');

// Reglas para identificadores
ID : [a-zA-Z][a-zA-Z0-9]*;

// Ignorar espacios en blanco
WS : [ \t\r\n]+ -> skip;



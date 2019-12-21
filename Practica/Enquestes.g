grammar Enquestes;

chatbot: (conversation)+ enquesta END;

enquesta: (PARAULA) DP ENQUESTA (IDItem)+;

conversation: (preg | resp | item | alternativa);

preg: (IDPregunta) DP PREGUNTA (PARAULA)+ INTERROGANT;

resp: (IDResposta) DP RESPOSTA opcio+;

opcio: NUM DP (PARAULA)+ PIC;

item: (IDItem) DP ITEM IDPregunta IMPLICA IDResposta;

alternativa: (IDAlternativa) DP ALTERNATIVA IDItem CO alternatives CC;
 
alternatives: PO NUM COMA IDItem PC (COMA alternatives|);

PO : '(';
PC : ')';
CO : '[';
CC : ']';
COMA : ',';
DP : ':';
PIC : ';';
INTERROGANT : '?';
IMPLICA : '->';
PREGUNTA :'PREGUNTA';
RESPOSTA : 'RESPOSTA';
CONVERSATION : 'CONVERSATION';
ALTERNATIVA : 'ALTERNATIVA';
ENQUESTA : 'ENQUESTA';
ITEM : 'ITEM';
END : 'END';
NUM : [0-9]+ ;
IDItem : 'I'[0-9]+;
IDPregunta : 'P'[0-9]+;
IDResposta : 'R'[0-9]+;
IDAlternativa : 'A'[0-9]+;
PARAULA : [a-zA-Z]+;

WS : [ \t\r\n\f]+ -> skip;

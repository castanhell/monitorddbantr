lexer grammar monitorddblexer;

fragment QUOTE : '"';
fragment NUMBER : [0-9];
fragment HYPHEN : '-';
fragment DOWNCASECHARACTER : [a-z];
fragment CHARACTER : [a-zA-Z];
fragment ALPHANUMERIC : [0-9a-zA-Z];
fragment YEAROPEN : '-y[';

COMMA : ','; 
COLUMN : ':'; 
KEYOPEN : '{';
KEYCLOSE : '}';


DYNAMODB : QUOTE 'DynamoDB' QUOTE;
EC2 : QUOTE 'EC2' QUOTE;

//DynamoDB
TABLES  : QUOTE 'Tables' QUOTE;
TABLE  : QUOTE 'Table' QUOTE;
TABLENAME : QUOTE 'TableName' QUOTE;
MONTHOPEN : '-m[' -> pushMode(MONTH);

//General purpose
REGIONPATTERN : QUOTE DOWNCASECHARACTER+ HYPHEN DOWNCASECHARACTER+ HYPHEN NUMBER QUOTE;
ALPHANUMERICTOKENBEGIN : QUOTE (ALPHANUMERIC)+; 
ALPHANUMERICTOKENEND : (ALPHANUMERIC)* QUOTE; 

WS : [ \t\n\r]+ -> skip;

//Modes

mode MONTH;

MONTHNUMBER : HYPHEN? (NUMBER | '11' ); 
MONTHCLOSE : ']' -> popMode;

mode YEAR;

MONTHNUMBER : HYPHEN? (NUMBER | '11' ); 
YEAR : ']' -> popMode;

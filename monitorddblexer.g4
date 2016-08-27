lexer grammar monitorddblexer;

fragment QUOTE : '"';
fragment NUMBER : [0-9];
fragment HYPHEN : '-';
fragment DOWNCASECHARACTER : [a-z];
fragment CHARACTER : [a-zA-Z];
fragment ALPHANUMERIC : [0-9a-zA-Z];

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
YEAROPEN : '-y[' -> pushMode(YEAR);
ADJUSTMENTS : QUOTE 'Adjustments' QUOTE;
ADJUSTMENT : QUOTE 'Adjustment' QUOTE;
METHOD : QUOTE 'Method' QUOTE;
METHODNAME : QUOTE ('scheduled' | 'requested') QUOTE;
CHANGETIME : QUOTE 'ChangeTime' QUOTE;
UNITS : QUOTE 'Units' QUOTE;
UNITNUMBER : QUOTE NUMBER+ ('r' | 'rw' | 'w' ) QUOTE;

//General purpose
HOUR : '"' (( [0-1] [0-9] | '2' [0-3] ) ':' [0-5] [0-9]) '"';
REGIONPATTERN : QUOTE DOWNCASECHARACTER+ HYPHEN DOWNCASECHARACTER+ HYPHEN NUMBER QUOTE;
HYPHEN_NUMERIC : (HYPHEN NUMBER+)+;
ALPHANUMERICTOKENBEGIN : QUOTE (ALPHANUMERIC)+; 
ALPHANUMERICTOKENEND : (ALPHANUMERIC)* QUOTE; 

WS : [ \t\n\r]+ -> skip;

//Modes

mode MONTH;

MONTHNUMBER : HYPHEN? (NUMBER | '11' ); 
MONTHCLOSE : ']' -> popMode;

mode YEAR;

YEARNUMBER : ( '0' | '-' [1-5] ); 
YEARCLOSE : ']' -> popMode;

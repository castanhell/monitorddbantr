parser grammar monitorddbparser;

options { tokenVocab=monitorddblexer; }

root : KEYOPEN region (COMMA region)* KEYCLOSE; 
region : REGIONPATTERN COLUMN product (COMMA product)*;
product : KEYOPEN dynamodb dynamodbBlock KEYCLOSE
	| KEYOPEN ec2 ec2Block KEYCLOSE
	;
ec2 : EC2;
ec2Block : ;
dynamodb : DYNAMODB COLUMN;
dynamodbBlock: KEYOPEN tables KEYCLOSE;
tables: TABLES COLUMN KEYOPEN table (COMMA table)* KEYCLOSE;
table: TABLE COLUMN KEYOPEN tableBlock KEYCLOSE;
tableBlock : TABLENAME COLUMN tablenamePatern ;
tablenamePatern : plainTablename | monthTablename | yearTablename;
plainTablename: ;
monthTablename: ALPHANUMERICTOKENBEGIN MONTHOPEN month MONTHCLOSE ALPHANUMERICTOKENEND;
month: MONTHNUMBER;
yearTablename: ;

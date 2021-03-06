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
tableBlock : TABLENAME COLUMN tablenamePatern COMMA adjustments;
//table
tablenamePatern : plainTablename | monthTablename | yearTablename | monthYearTablename | yearMonthTablename;
plainTablename: ALPHANUMERICTOKENBEGIN (HYPHEN_NUMERIC)* ALPHANUMERICTOKENEND;
monthTablename: ALPHANUMERICTOKENBEGIN MONTHOPEN month MONTHCLOSE ALPHANUMERICTOKENEND;
month: MONTHNUMBER;
yearTablename: ALPHANUMERICTOKENBEGIN YEAROPEN year YEARCLOSE ALPHANUMERICTOKENEND;
year: YEARNUMBER;
monthYearTablename: ALPHANUMERICTOKENBEGIN MONTHOPEN month MONTHCLOSE YEAROPEN year YEARCLOSE ALPHANUMERICTOKENEND;
yearMonthTablename: ALPHANUMERICTOKENBEGIN YEAROPEN year YEARCLOSE MONTHOPEN month MONTHCLOSE ALPHANUMERICTOKENEND;
//adjustements
adjustments : ADJUSTMENTS COLUMN KEYOPEN adjustment (COMMA adjustment)* KEYCLOSE;
adjustment : ADJUSTMENT COLUMN KEYOPEN adjustmentBlock KEYCLOSE; 
adjustmentBlock : METHOD COLUMN method COMMA CHANGETIME COLUMN changetime COMMA UNITS COLUMN units ;// COMMA CHANGETIME HOURCOLUMN changetime;  
method : METHODNAME;
changetime : HOUR ;
units : UNITNUMBER ;

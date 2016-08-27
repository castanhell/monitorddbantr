# Generated from monitorddbparser.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\22u\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4")
        buf.write(u"\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\7\2%\n\2")
        buf.write(u"\f\2\16\2(\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3\61\n")
        buf.write(u"\3\f\3\16\3\64\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\5\4@\n\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write(u"\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7\tS\n\t\f\t\16\tV\13")
        buf.write(u"\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write(u"\3\f\3\f\3\f\5\fg\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\17\3\17\3\20\3\20\3\20\2\2\21\2\4\6\b\n\f\16")
        buf.write(u"\20\22\24\26\30\32\34\36\2\2k\2 \3\2\2\2\4+\3\2\2\2\6")
        buf.write(u"?\3\2\2\2\bA\3\2\2\2\nC\3\2\2\2\fE\3\2\2\2\16H\3\2\2")
        buf.write(u"\2\20L\3\2\2\2\22Y\3\2\2\2\24_\3\2\2\2\26f\3\2\2\2\30")
        buf.write(u"h\3\2\2\2\32j\3\2\2\2\34p\3\2\2\2\36r\3\2\2\2 !\7\5\2")
        buf.write(u"\2!&\5\4\3\2\"#\7\3\2\2#%\5\4\3\2$\"\3\2\2\2%(\3\2\2")
        buf.write(u"\2&$\3\2\2\2&\'\3\2\2\2\')\3\2\2\2(&\3\2\2\2)*\7\6\2")
        buf.write(u"\2*\3\3\2\2\2+,\7\r\2\2,-\7\4\2\2-\62\5\6\4\2./\7\3\2")
        buf.write(u"\2/\61\5\6\4\2\60.\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2")
        buf.write(u"\2\62\63\3\2\2\2\63\5\3\2\2\2\64\62\3\2\2\2\65\66\7\5")
        buf.write(u"\2\2\66\67\5\f\7\2\678\5\16\b\289\7\6\2\29@\3\2\2\2:")
        buf.write(u";\7\5\2\2;<\5\b\5\2<=\5\n\6\2=>\7\6\2\2>@\3\2\2\2?\65")
        buf.write(u"\3\2\2\2?:\3\2\2\2@\7\3\2\2\2AB\7\b\2\2B\t\3\2\2\2CD")
        buf.write(u"\3\2\2\2D\13\3\2\2\2EF\7\7\2\2FG\7\4\2\2G\r\3\2\2\2H")
        buf.write(u"I\7\5\2\2IJ\5\20\t\2JK\7\6\2\2K\17\3\2\2\2LM\7\t\2\2")
        buf.write(u"MN\7\4\2\2NO\7\5\2\2OT\5\22\n\2PQ\7\3\2\2QS\5\22\n\2")
        buf.write(u"RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VT")
        buf.write(u"\3\2\2\2WX\7\6\2\2X\21\3\2\2\2YZ\7\n\2\2Z[\7\4\2\2[\\")
        buf.write(u"\7\5\2\2\\]\5\24\13\2]^\7\6\2\2^\23\3\2\2\2_`\7\13\2")
        buf.write(u"\2`a\7\4\2\2ab\5\26\f\2b\25\3\2\2\2cg\5\30\r\2dg\5\32")
        buf.write(u"\16\2eg\5\36\20\2fc\3\2\2\2fd\3\2\2\2fe\3\2\2\2g\27\3")
        buf.write(u"\2\2\2hi\3\2\2\2i\31\3\2\2\2jk\7\16\2\2kl\7\f\2\2lm\5")
        buf.write(u"\34\17\2mn\7\22\2\2no\7\17\2\2o\33\3\2\2\2pq\7\21\2\2")
        buf.write(u"q\35\3\2\2\2rs\3\2\2\2s\37\3\2\2\2\7&\62?Tf")
        return buf.getvalue()


class monitorddbparser ( Parser ):

    grammarFileName = "monitorddbparser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"','", u"':'", u"'{'", u"'}'", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'-m['", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"']'" ]

    symbolicNames = [ u"<INVALID>", u"COMMA", u"COLUMN", u"KEYOPEN", u"KEYCLOSE", 
                      u"DYNAMODB", u"EC2", u"TABLES", u"TABLE", u"TABLENAME", 
                      u"MONTHOPEN", u"REGIONPATTERN", u"ALPHANUMERICTOKENBEGIN", 
                      u"ALPHANUMERICTOKENEND", u"WS", u"MONTHNUMBER", u"MONTHCLOSE" ]

    RULE_root = 0
    RULE_region = 1
    RULE_product = 2
    RULE_ec2 = 3
    RULE_ec2Block = 4
    RULE_dynamodb = 5
    RULE_dynamodbBlock = 6
    RULE_tables = 7
    RULE_table = 8
    RULE_tableBlock = 9
    RULE_tablenamePatern = 10
    RULE_plainTablename = 11
    RULE_monthTablename = 12
    RULE_month = 13
    RULE_yearTablename = 14

    ruleNames =  [ u"root", u"region", u"product", u"ec2", u"ec2Block", 
                   u"dynamodb", u"dynamodbBlock", u"tables", u"table", u"tableBlock", 
                   u"tablenamePatern", u"plainTablename", u"monthTablename", 
                   u"month", u"yearTablename" ]

    EOF = Token.EOF
    COMMA=1
    COLUMN=2
    KEYOPEN=3
    KEYCLOSE=4
    DYNAMODB=5
    EC2=6
    TABLES=7
    TABLE=8
    TABLENAME=9
    MONTHOPEN=10
    REGIONPATTERN=11
    ALPHANUMERICTOKENBEGIN=12
    ALPHANUMERICTOKENEND=13
    WS=14
    MONTHNUMBER=15
    MONTHCLOSE=16

    def __init__(self, input):
        super(monitorddbparser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.RootContext, self).__init__(parent, invokingState)
            self.parser = parser

        def KEYOPEN(self):
            return self.getToken(monitorddbparser.KEYOPEN, 0)

        def region(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(monitorddbparser.RegionContext)
            else:
                return self.getTypedRuleContext(monitorddbparser.RegionContext,i)


        def KEYCLOSE(self):
            return self.getToken(monitorddbparser.KEYCLOSE, 0)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(monitorddbparser.COMMA)
            else:
                return self.getToken(monitorddbparser.COMMA, i)

        def getRuleIndex(self):
            return monitorddbparser.RULE_root

        def enterRule(self, listener):
            if hasattr(listener, "enterRoot"):
                listener.enterRoot(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRoot"):
                listener.exitRoot(self)




    def root(self):

        localctx = monitorddbparser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(monitorddbparser.KEYOPEN)
            self.state = 31
            self.region()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==monitorddbparser.COMMA:
                self.state = 32
                self.match(monitorddbparser.COMMA)
                self.state = 33
                self.region()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(monitorddbparser.KEYCLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.RegionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def REGIONPATTERN(self):
            return self.getToken(monitorddbparser.REGIONPATTERN, 0)

        def COLUMN(self):
            return self.getToken(monitorddbparser.COLUMN, 0)

        def product(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(monitorddbparser.ProductContext)
            else:
                return self.getTypedRuleContext(monitorddbparser.ProductContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(monitorddbparser.COMMA)
            else:
                return self.getToken(monitorddbparser.COMMA, i)

        def getRuleIndex(self):
            return monitorddbparser.RULE_region

        def enterRule(self, listener):
            if hasattr(listener, "enterRegion"):
                listener.enterRegion(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRegion"):
                listener.exitRegion(self)




    def region(self):

        localctx = monitorddbparser.RegionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_region)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(monitorddbparser.REGIONPATTERN)
            self.state = 42
            self.match(monitorddbparser.COLUMN)
            self.state = 43
            self.product()
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 44
                    self.match(monitorddbparser.COMMA)
                    self.state = 45
                    self.product() 
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProductContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.ProductContext, self).__init__(parent, invokingState)
            self.parser = parser

        def KEYOPEN(self):
            return self.getToken(monitorddbparser.KEYOPEN, 0)

        def dynamodb(self):
            return self.getTypedRuleContext(monitorddbparser.DynamodbContext,0)


        def dynamodbBlock(self):
            return self.getTypedRuleContext(monitorddbparser.DynamodbBlockContext,0)


        def KEYCLOSE(self):
            return self.getToken(monitorddbparser.KEYCLOSE, 0)

        def ec2(self):
            return self.getTypedRuleContext(monitorddbparser.Ec2Context,0)


        def ec2Block(self):
            return self.getTypedRuleContext(monitorddbparser.Ec2BlockContext,0)


        def getRuleIndex(self):
            return monitorddbparser.RULE_product

        def enterRule(self, listener):
            if hasattr(listener, "enterProduct"):
                listener.enterProduct(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProduct"):
                listener.exitProduct(self)




    def product(self):

        localctx = monitorddbparser.ProductContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_product)
        try:
            self.state = 61
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(monitorddbparser.KEYOPEN)
                self.state = 52
                self.dynamodb()
                self.state = 53
                self.dynamodbBlock()
                self.state = 54
                self.match(monitorddbparser.KEYCLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(monitorddbparser.KEYOPEN)
                self.state = 57
                self.ec2()
                self.state = 58
                self.ec2Block()
                self.state = 59
                self.match(monitorddbparser.KEYCLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ec2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.Ec2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def EC2(self):
            return self.getToken(monitorddbparser.EC2, 0)

        def getRuleIndex(self):
            return monitorddbparser.RULE_ec2

        def enterRule(self, listener):
            if hasattr(listener, "enterEc2"):
                listener.enterEc2(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEc2"):
                listener.exitEc2(self)




    def ec2(self):

        localctx = monitorddbparser.Ec2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ec2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(monitorddbparser.EC2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ec2BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.Ec2BlockContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return monitorddbparser.RULE_ec2Block

        def enterRule(self, listener):
            if hasattr(listener, "enterEc2Block"):
                listener.enterEc2Block(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitEc2Block"):
                listener.exitEc2Block(self)




    def ec2Block(self):

        localctx = monitorddbparser.Ec2BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ec2Block)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DynamodbContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.DynamodbContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DYNAMODB(self):
            return self.getToken(monitorddbparser.DYNAMODB, 0)

        def COLUMN(self):
            return self.getToken(monitorddbparser.COLUMN, 0)

        def getRuleIndex(self):
            return monitorddbparser.RULE_dynamodb

        def enterRule(self, listener):
            if hasattr(listener, "enterDynamodb"):
                listener.enterDynamodb(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDynamodb"):
                listener.exitDynamodb(self)




    def dynamodb(self):

        localctx = monitorddbparser.DynamodbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dynamodb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(monitorddbparser.DYNAMODB)
            self.state = 68
            self.match(monitorddbparser.COLUMN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DynamodbBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.DynamodbBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def KEYOPEN(self):
            return self.getToken(monitorddbparser.KEYOPEN, 0)

        def tables(self):
            return self.getTypedRuleContext(monitorddbparser.TablesContext,0)


        def KEYCLOSE(self):
            return self.getToken(monitorddbparser.KEYCLOSE, 0)

        def getRuleIndex(self):
            return monitorddbparser.RULE_dynamodbBlock

        def enterRule(self, listener):
            if hasattr(listener, "enterDynamodbBlock"):
                listener.enterDynamodbBlock(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDynamodbBlock"):
                listener.exitDynamodbBlock(self)




    def dynamodbBlock(self):

        localctx = monitorddbparser.DynamodbBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dynamodbBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(monitorddbparser.KEYOPEN)
            self.state = 71
            self.tables()
            self.state = 72
            self.match(monitorddbparser.KEYCLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TablesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.TablesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TABLES(self):
            return self.getToken(monitorddbparser.TABLES, 0)

        def COLUMN(self):
            return self.getToken(monitorddbparser.COLUMN, 0)

        def KEYOPEN(self):
            return self.getToken(monitorddbparser.KEYOPEN, 0)

        def table(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(monitorddbparser.TableContext)
            else:
                return self.getTypedRuleContext(monitorddbparser.TableContext,i)


        def KEYCLOSE(self):
            return self.getToken(monitorddbparser.KEYCLOSE, 0)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(monitorddbparser.COMMA)
            else:
                return self.getToken(monitorddbparser.COMMA, i)

        def getRuleIndex(self):
            return monitorddbparser.RULE_tables

        def enterRule(self, listener):
            if hasattr(listener, "enterTables"):
                listener.enterTables(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTables"):
                listener.exitTables(self)




    def tables(self):

        localctx = monitorddbparser.TablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(monitorddbparser.TABLES)
            self.state = 75
            self.match(monitorddbparser.COLUMN)
            self.state = 76
            self.match(monitorddbparser.KEYOPEN)
            self.state = 77
            self.table()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==monitorddbparser.COMMA:
                self.state = 78
                self.match(monitorddbparser.COMMA)
                self.state = 79
                self.table()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(monitorddbparser.KEYCLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.TableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TABLE(self):
            return self.getToken(monitorddbparser.TABLE, 0)

        def COLUMN(self):
            return self.getToken(monitorddbparser.COLUMN, 0)

        def KEYOPEN(self):
            return self.getToken(monitorddbparser.KEYOPEN, 0)

        def tableBlock(self):
            return self.getTypedRuleContext(monitorddbparser.TableBlockContext,0)


        def KEYCLOSE(self):
            return self.getToken(monitorddbparser.KEYCLOSE, 0)

        def getRuleIndex(self):
            return monitorddbparser.RULE_table

        def enterRule(self, listener):
            if hasattr(listener, "enterTable"):
                listener.enterTable(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTable"):
                listener.exitTable(self)




    def table(self):

        localctx = monitorddbparser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(monitorddbparser.TABLE)
            self.state = 88
            self.match(monitorddbparser.COLUMN)
            self.state = 89
            self.match(monitorddbparser.KEYOPEN)
            self.state = 90
            self.tableBlock()
            self.state = 91
            self.match(monitorddbparser.KEYCLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TableBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.TableBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TABLENAME(self):
            return self.getToken(monitorddbparser.TABLENAME, 0)

        def COLUMN(self):
            return self.getToken(monitorddbparser.COLUMN, 0)

        def tablenamePatern(self):
            return self.getTypedRuleContext(monitorddbparser.TablenamePaternContext,0)


        def getRuleIndex(self):
            return monitorddbparser.RULE_tableBlock

        def enterRule(self, listener):
            if hasattr(listener, "enterTableBlock"):
                listener.enterTableBlock(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTableBlock"):
                listener.exitTableBlock(self)




    def tableBlock(self):

        localctx = monitorddbparser.TableBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tableBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(monitorddbparser.TABLENAME)
            self.state = 94
            self.match(monitorddbparser.COLUMN)
            self.state = 95
            self.tablenamePatern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TablenamePaternContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.TablenamePaternContext, self).__init__(parent, invokingState)
            self.parser = parser

        def plainTablename(self):
            return self.getTypedRuleContext(monitorddbparser.PlainTablenameContext,0)


        def monthTablename(self):
            return self.getTypedRuleContext(monitorddbparser.MonthTablenameContext,0)


        def yearTablename(self):
            return self.getTypedRuleContext(monitorddbparser.YearTablenameContext,0)


        def getRuleIndex(self):
            return monitorddbparser.RULE_tablenamePatern

        def enterRule(self, listener):
            if hasattr(listener, "enterTablenamePatern"):
                listener.enterTablenamePatern(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTablenamePatern"):
                listener.exitTablenamePatern(self)




    def tablenamePatern(self):

        localctx = monitorddbparser.TablenamePaternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tablenamePatern)
        try:
            self.state = 100
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.plainTablename()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.monthTablename()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.yearTablename()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PlainTablenameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.PlainTablenameContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return monitorddbparser.RULE_plainTablename

        def enterRule(self, listener):
            if hasattr(listener, "enterPlainTablename"):
                listener.enterPlainTablename(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPlainTablename"):
                listener.exitPlainTablename(self)




    def plainTablename(self):

        localctx = monitorddbparser.PlainTablenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_plainTablename)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MonthTablenameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.MonthTablenameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ALPHANUMERICTOKENBEGIN(self):
            return self.getToken(monitorddbparser.ALPHANUMERICTOKENBEGIN, 0)

        def MONTHOPEN(self):
            return self.getToken(monitorddbparser.MONTHOPEN, 0)

        def month(self):
            return self.getTypedRuleContext(monitorddbparser.MonthContext,0)


        def MONTHCLOSE(self):
            return self.getToken(monitorddbparser.MONTHCLOSE, 0)

        def ALPHANUMERICTOKENEND(self):
            return self.getToken(monitorddbparser.ALPHANUMERICTOKENEND, 0)

        def getRuleIndex(self):
            return monitorddbparser.RULE_monthTablename

        def enterRule(self, listener):
            if hasattr(listener, "enterMonthTablename"):
                listener.enterMonthTablename(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMonthTablename"):
                listener.exitMonthTablename(self)




    def monthTablename(self):

        localctx = monitorddbparser.MonthTablenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_monthTablename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(monitorddbparser.ALPHANUMERICTOKENBEGIN)
            self.state = 105
            self.match(monitorddbparser.MONTHOPEN)
            self.state = 106
            self.month()
            self.state = 107
            self.match(monitorddbparser.MONTHCLOSE)
            self.state = 108
            self.match(monitorddbparser.ALPHANUMERICTOKENEND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MonthContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.MonthContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MONTHNUMBER(self):
            return self.getToken(monitorddbparser.MONTHNUMBER, 0)

        def getRuleIndex(self):
            return monitorddbparser.RULE_month

        def enterRule(self, listener):
            if hasattr(listener, "enterMonth"):
                listener.enterMonth(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMonth"):
                listener.exitMonth(self)




    def month(self):

        localctx = monitorddbparser.MonthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_month)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(monitorddbparser.MONTHNUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class YearTablenameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(monitorddbparser.YearTablenameContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return monitorddbparser.RULE_yearTablename

        def enterRule(self, listener):
            if hasattr(listener, "enterYearTablename"):
                listener.enterYearTablename(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitYearTablename"):
                listener.exitYearTablename(self)




    def yearTablename(self):

        localctx = monitorddbparser.YearTablenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_yearTablename)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






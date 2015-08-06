# Generated from java-escape by ANTLR 4.4
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ksp_craftListener import ksp_craftListener
else:
    from ksp_craftListener import ksp_craftListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\35\u00a4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\7\2\66\n\2\f\2\16\29\13\2\3\2\3\2\3\3\3")
        buf.write(u"\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write(u"\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f|\n\f\f\f")
        buf.write(u"\16\f\177\13\f\3\f\3\f\3\f\7\f\u0084\n\f\f\f\16\f\u0087")
        buf.write(u"\13\f\3\f\3\f\3\f\3\f\7\f\u008d\n\f\f\f\16\f\u0090\13")
        buf.write(u"\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3")
        buf.write(u"\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\2\2\21\2\4\6\b")
        buf.write(u"\n\f\16\20\22\24\26\30\32\34\36\2\2\u0098\2 \3\2\2\2")
        buf.write(u"\4<\3\2\2\2\6>\3\2\2\2\b@\3\2\2\2\nB\3\2\2\2\fD\3\2\2")
        buf.write(u"\2\16F\3\2\2\2\20H\3\2\2\2\22J\3\2\2\2\24L\3\2\2\2\26")
        buf.write(u"N\3\2\2\2\30\u0093\3\2\2\2\32\u0097\3\2\2\2\34\u009b")
        buf.write(u"\3\2\2\2\36\u009f\3\2\2\2 !\7\20\2\2!\"\7\22\2\2\"#\5")
        buf.write(u"\4\3\2#$\3\2\2\2$%\7\32\2\2%&\7\22\2\2&\'\5\b\5\2\'(")
        buf.write(u"\3\2\2\2()\7\b\2\2)*\7\22\2\2*+\5\n\6\2+,\3\2\2\2,-\7")
        buf.write(u"\26\2\2-.\7\22\2\2./\5\f\7\2/\60\3\2\2\2\60\61\7\13\2")
        buf.write(u"\2\61\62\7\22\2\2\62\63\5\16\b\2\63\67\3\2\2\2\64\66")
        buf.write(u"\5\26\f\2\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\67")
        buf.write(u"8\3\2\2\28:\3\2\2\29\67\3\2\2\2:;\7\2\2\3;\3\3\2\2\2")
        buf.write(u"<=\7\34\2\2=\5\3\2\2\2>?\7\34\2\2?\7\3\2\2\2@A\7\34\2")
        buf.write(u"\2A\t\3\2\2\2BC\7\34\2\2C\13\3\2\2\2DE\7\34\2\2E\r\3")
        buf.write(u"\2\2\2FG\7\34\2\2G\17\3\2\2\2HI\7\34\2\2I\21\3\2\2\2")
        buf.write(u"JK\7\34\2\2K\23\3\2\2\2LM\7\34\2\2M\25\3\2\2\2NO\7\21")
        buf.write(u"\2\2OP\7\t\2\2PQ\7\6\2\2QR\7\22\2\2RS\5\20\t\2ST\3\2")
        buf.write(u"\2\2TU\7\30\2\2UV\7\22\2\2VW\5\6\4\2WX\3\2\2\2XY\7\4")
        buf.write(u"\2\2YZ\7\22\2\2Z[\5\6\4\2[\\\3\2\2\2\\]\7\5\2\2]^\7\22")
        buf.write(u"\2\2^_\5\6\4\2_`\3\2\2\2`a\7\31\2\2ab\7\22\2\2bc\5\6")
        buf.write(u"\4\2cd\3\2\2\2de\7\r\2\2ef\7\22\2\2fg\5\6\4\2gh\3\2\2")
        buf.write(u"\2hi\7\7\2\2ij\7\22\2\2jk\5\6\4\2kl\3\2\2\2lm\7\27\2")
        buf.write(u"\2mn\7\22\2\2no\5\6\4\2op\3\2\2\2pq\7\16\2\2qr\7\22\2")
        buf.write(u"\2rs\5\6\4\2st\3\2\2\2tu\7\3\2\2uv\7\22\2\2vw\5\6\4\2")
        buf.write(u"w}\3\2\2\2xy\7\n\2\2yz\7\22\2\2z|\5\22\n\2{x\3\2\2\2")
        buf.write(u"|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0085\3\2\2\2\177")
        buf.write(u"}\3\2\2\2\u0080\u0081\7\24\2\2\u0081\u0082\7\22\2\2\u0082")
        buf.write(u"\u0084\5\24\13\2\u0083\u0080\3\2\2\2\u0084\u0087\3\2")
        buf.write(u"\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0088")
        buf.write(u"\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\5\30\r\2\u0089")
        buf.write(u"\u008a\5\32\16\2\u008a\u008e\5\34\17\2\u008b\u008d\5")
        buf.write(u"\36\20\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e")
        buf.write(u"\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2")
        buf.write(u"\2\u0090\u008e\3\2\2\2\u0091\u0092\7\17\2\2\u0092\27")
        buf.write(u"\3\2\2\2\u0093\u0094\7\33\2\2\u0094\u0095\7\t\2\2\u0095")
        buf.write(u"\u0096\7\17\2\2\u0096\31\3\2\2\2\u0097\u0098\7\23\2\2")
        buf.write(u"\u0098\u0099\7\t\2\2\u0099\u009a\7\17\2\2\u009a\33\3")
        buf.write(u"\2\2\2\u009b\u009c\7\f\2\2\u009c\u009d\7\t\2\2\u009d")
        buf.write(u"\u009e\7\17\2\2\u009e\35\3\2\2\2\u009f\u00a0\7\25\2\2")
        buf.write(u"\u00a0\u00a1\7\t\2\2\u00a1\u00a2\7\17\2\2\u00a2\37\3")
        buf.write(u"\2\2\2\6\67}\u0085\u008e")
        return buf.getvalue()
		

class ksp_craftParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__24=1
    T__23=2
    T__22=3
    T__21=4
    T__20=5
    T__19=6
    T__18=7
    T__17=8
    T__16=9
    T__15=10
    T__14=11
    T__13=12
    T__12=13
    T__11=14
    T__10=15
    T__9=16
    T__8=17
    T__7=18
    T__6=19
    T__5=20
    T__4=21
    T__3=22
    T__2=23
    T__1=24
    T__0=25
    ID=26
    WS=27

    tokenNames = [ u"<INVALID>", u"'symMethod'", u"'pos'", u"'attPos'", 
                   u"'part'", u"'attRot'", u"'description'", u"'{'", u"'link'", 
                   u"'size'", u"'PARTDATA'", u"'rot'", u"'mir'", u"'}'", 
                   u"'ship'", u"'PART'", u"'='", u"'ACTIONS'", u"'attN'", 
                   u"'MODULE'", u"'type'", u"'attRot0'", u"'partName'", 
                   u"'attPos0'", u"'version'", u"'EVENTS'", u"ID", u"WS" ]

    RULE_start = 0
    RULE_ship = 1
    RULE_partname = 2
    RULE_version = 3
    RULE_description = 4
    RULE_kind = 5
    RULE_size = 6
    RULE_uuid = 7
    RULE_link_uuid = 8
    RULE_attn_uuid = 9
    RULE_part = 10
    RULE_events = 11
    RULE_actions = 12
    RULE_partdata = 13
    RULE_module = 14

    ruleNames =  [ u"start", u"ship", u"partname", u"version", u"description", 
                   u"kind", u"size", u"uuid", u"link_uuid", u"attn_uuid", 
                   u"part", u"events", u"actions", u"partdata", u"module" ]

    def __init__(self, input):
        super(ksp_craftParser, self).__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.StartContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ksp_craftParser.EOF, 0)

        def description(self):
            return self.getTypedRuleContext(ksp_craftParser.DescriptionContext,0)


        def version(self):
            return self.getTypedRuleContext(ksp_craftParser.VersionContext,0)


        def size(self):
            return self.getTypedRuleContext(ksp_craftParser.SizeContext,0)


        def kind(self):
            return self.getTypedRuleContext(ksp_craftParser.KindContext,0)


        def part(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ksp_craftParser.PartContext)
            else:
                return self.getTypedRuleContext(ksp_craftParser.PartContext,i)


        def ship(self):
            return self.getTypedRuleContext(ksp_craftParser.ShipContext,0)


        def getRuleIndex(self):
            return ksp_craftParser.RULE_start

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterStart(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitStart(self)




    def start(self):

        localctx = ksp_craftParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(self.T__11)
            self.state = 31
            self.match(self.T__9)
            self.state = 32 
            self.ship()

            self.state = 34
            self.match(self.T__1)
            self.state = 35
            self.match(self.T__9)
            self.state = 36 
            self.version()

            self.state = 38
            self.match(self.T__19)
            self.state = 39
            self.match(self.T__9)
            self.state = 40 
            self.description()

            self.state = 42
            self.match(self.T__5)
            self.state = 43
            self.match(self.T__9)
            self.state = 44 
            self.kind()

            self.state = 46
            self.match(self.T__16)
            self.state = 47
            self.match(self.T__9)
            self.state = 48 
            self.size()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ksp_craftParser.T__10:
                self.state = 50 
                self.part()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(self.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ShipContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.ShipContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ksp_craftParser.ID, 0)

        def getRuleIndex(self):
            return ksp_craftParser.RULE_ship

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterShip(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitShip(self)




    def ship(self):

        localctx = ksp_craftParser.ShipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ship)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PartnameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.PartnameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ksp_craftParser.ID, 0)

        def getRuleIndex(self):
            return ksp_craftParser.RULE_partname

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterPartname(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitPartname(self)




    def partname(self):

        localctx = ksp_craftParser.PartnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_partname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VersionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.VersionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ksp_craftParser.ID, 0)

        def getRuleIndex(self):
            return ksp_craftParser.RULE_version

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterVersion(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitVersion(self)




    def version(self):

        localctx = ksp_craftParser.VersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_version)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DescriptionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.DescriptionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ksp_craftParser.ID, 0)

        def getRuleIndex(self):
            return ksp_craftParser.RULE_description

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterDescription(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitDescription(self)




    def description(self):

        localctx = ksp_craftParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KindContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.KindContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ksp_craftParser.ID, 0)

        def getRuleIndex(self):
            return ksp_craftParser.RULE_kind

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterKind(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitKind(self)




    def kind(self):

        localctx = ksp_craftParser.KindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_kind)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SizeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.SizeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ksp_craftParser.ID, 0)

        def getRuleIndex(self):
            return ksp_craftParser.RULE_size

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterSize(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitSize(self)




    def size(self):

        localctx = ksp_craftParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UuidContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.UuidContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ksp_craftParser.ID, 0)

        def getRuleIndex(self):
            return ksp_craftParser.RULE_uuid

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterUuid(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitUuid(self)




    def uuid(self):

        localctx = ksp_craftParser.UuidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_uuid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Link_uuidContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.Link_uuidContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ksp_craftParser.ID, 0)

        def getRuleIndex(self):
            return ksp_craftParser.RULE_link_uuid

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterLink_uuid(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitLink_uuid(self)




    def link_uuid(self):

        localctx = ksp_craftParser.Link_uuidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_link_uuid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attn_uuidContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.Attn_uuidContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ksp_craftParser.ID, 0)

        def getRuleIndex(self):
            return ksp_craftParser.RULE_attn_uuid

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterAttn_uuid(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitAttn_uuid(self)




    def attn_uuid(self):

        localctx = ksp_craftParser.Attn_uuidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attn_uuid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PartContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.PartContext, self).__init__(parent, invokingState)
            self.parser = parser

        def events(self):
            return self.getTypedRuleContext(ksp_craftParser.EventsContext,0)


        def module(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ksp_craftParser.ModuleContext)
            else:
                return self.getTypedRuleContext(ksp_craftParser.ModuleContext,i)


        def uuid(self):
            return self.getTypedRuleContext(ksp_craftParser.UuidContext,0)


        def partname(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ksp_craftParser.PartnameContext)
            else:
                return self.getTypedRuleContext(ksp_craftParser.PartnameContext,i)


        def link_uuid(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ksp_craftParser.Link_uuidContext)
            else:
                return self.getTypedRuleContext(ksp_craftParser.Link_uuidContext,i)


        def partdata(self):
            return self.getTypedRuleContext(ksp_craftParser.PartdataContext,0)


        def attn_uuid(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ksp_craftParser.Attn_uuidContext)
            else:
                return self.getTypedRuleContext(ksp_craftParser.Attn_uuidContext,i)


        def actions(self):
            return self.getTypedRuleContext(ksp_craftParser.ActionsContext,0)


        def getRuleIndex(self):
            return ksp_craftParser.RULE_part

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterPart(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitPart(self)




    def part(self):

        localctx = ksp_craftParser.PartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(self.T__10)
            self.state = 77
            self.match(self.T__18)

            self.state = 78
            self.match(self.T__21)
            self.state = 79
            self.match(self.T__9)
            self.state = 80 
            self.uuid()

            self.state = 82
            self.match(self.T__3)
            self.state = 83
            self.match(self.T__9)
            self.state = 84 
            self.partname()

            self.state = 86
            self.match(self.T__23)
            self.state = 87
            self.match(self.T__9)
            self.state = 88 
            self.partname()

            self.state = 90
            self.match(self.T__22)
            self.state = 91
            self.match(self.T__9)
            self.state = 92 
            self.partname()

            self.state = 94
            self.match(self.T__2)
            self.state = 95
            self.match(self.T__9)
            self.state = 96 
            self.partname()

            self.state = 98
            self.match(self.T__14)
            self.state = 99
            self.match(self.T__9)
            self.state = 100 
            self.partname()

            self.state = 102
            self.match(self.T__20)
            self.state = 103
            self.match(self.T__9)
            self.state = 104 
            self.partname()

            self.state = 106
            self.match(self.T__4)
            self.state = 107
            self.match(self.T__9)
            self.state = 108 
            self.partname()

            self.state = 110
            self.match(self.T__13)
            self.state = 111
            self.match(self.T__9)
            self.state = 112 
            self.partname()

            self.state = 114
            self.match(self.T__24)
            self.state = 115
            self.match(self.T__9)
            self.state = 116 
            self.partname()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ksp_craftParser.T__17:
                self.state = 118
                self.match(self.T__17)
                self.state = 119
                self.match(self.T__9)
                self.state = 120 
                self.link_uuid()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ksp_craftParser.T__7:
                self.state = 126
                self.match(self.T__7)
                self.state = 127
                self.match(self.T__9)
                self.state = 128 
                self.attn_uuid()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134 
            self.events()

            self.state = 135 
            self.actions()

            self.state = 136 
            self.partdata()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ksp_craftParser.T__6:
                self.state = 137 
                self.module()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(self.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.EventsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ksp_craftParser.RULE_events

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterEvents(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitEvents(self)




    def events(self):

        localctx = ksp_craftParser.EventsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_events)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(self.T__0)
            self.state = 146
            self.match(self.T__18)
            self.state = 147
            self.match(self.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.ActionsContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ksp_craftParser.RULE_actions

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterActions(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitActions(self)




    def actions(self):

        localctx = ksp_craftParser.ActionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_actions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(self.T__8)
            self.state = 150
            self.match(self.T__18)
            self.state = 151
            self.match(self.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PartdataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.PartdataContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ksp_craftParser.RULE_partdata

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterPartdata(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitPartdata(self)




    def partdata(self):

        localctx = ksp_craftParser.PartdataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_partdata)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(self.T__15)
            self.state = 154
            self.match(self.T__18)
            self.state = 155
            self.match(self.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ksp_craftParser.ModuleContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ksp_craftParser.RULE_module

        def enterRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.enterModule(self)

        def exitRule(self, listener):
            if isinstance( listener, ksp_craftListener ):
                listener.exitModule(self)




    def module(self):

        localctx = ksp_craftParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(self.T__6)
            self.state = 158
            self.match(self.T__18)
            self.state = 159
            self.match(self.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





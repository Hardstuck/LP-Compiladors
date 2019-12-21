# Generated from Enquestes.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\6\3!\n\3\r\3\16\3\"\3\4\3\4\3\4")
        buf.write("\3\4\5\4)\n\4\3\5\3\5\3\5\3\5\6\5/\n\5\r\5\16\5\60\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\6\69\n\6\r\6\16\6:\3\7\3\7\3\7\6")
        buf.write("\7@\n\7\r\7\16\7A\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\n]\n\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2")
        buf.write("\2\2^\2\25\3\2\2\2\4\34\3\2\2\2\6(\3\2\2\2\b*\3\2\2\2")
        buf.write("\n\64\3\2\2\2\f<\3\2\2\2\16E\3\2\2\2\20L\3\2\2\2\22T\3")
        buf.write("\2\2\2\24\26\5\6\4\2\25\24\3\2\2\2\26\27\3\2\2\2\27\25")
        buf.write("\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\32\5\4\3\2\32")
        buf.write("\33\7\22\2\2\33\3\3\2\2\2\34\35\7\30\2\2\35\36\7\b\2\2")
        buf.write("\36 \7\20\2\2\37!\7\24\2\2 \37\3\2\2\2!\"\3\2\2\2\" \3")
        buf.write("\2\2\2\"#\3\2\2\2#\5\3\2\2\2$)\5\b\5\2%)\5\n\6\2&)\5\16")
        buf.write("\b\2\')\5\20\t\2($\3\2\2\2(%\3\2\2\2(&\3\2\2\2(\'\3\2")
        buf.write("\2\2)\7\3\2\2\2*+\7\25\2\2+,\7\b\2\2,.\7\f\2\2-/\7\30")
        buf.write("\2\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("\62\3\2\2\2\62\63\7\n\2\2\63\t\3\2\2\2\64\65\7\26\2\2")
        buf.write("\65\66\7\b\2\2\668\7\r\2\2\679\5\f\7\28\67\3\2\2\29:\3")
        buf.write("\2\2\2:8\3\2\2\2:;\3\2\2\2;\13\3\2\2\2<=\7\23\2\2=?\7")
        buf.write("\b\2\2>@\7\30\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2")
        buf.write("\2\2BC\3\2\2\2CD\7\t\2\2D\r\3\2\2\2EF\7\24\2\2FG\7\b\2")
        buf.write("\2GH\7\21\2\2HI\7\25\2\2IJ\7\13\2\2JK\7\26\2\2K\17\3\2")
        buf.write("\2\2LM\7\27\2\2MN\7\b\2\2NO\7\17\2\2OP\7\24\2\2PQ\7\5")
        buf.write("\2\2QR\5\22\n\2RS\7\6\2\2S\21\3\2\2\2TU\7\3\2\2UV\7\23")
        buf.write("\2\2VW\7\7\2\2WX\7\24\2\2X\\\7\4\2\2YZ\7\7\2\2Z]\5\22")
        buf.write("\n\2[]\3\2\2\2\\Y\3\2\2\2\\[\3\2\2\2]\23\3\2\2\2\t\27")
        buf.write("\"(\60:A\\")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "','", "':'", 
                     "';'", "'?'", "'->'", "'PREGUNTA'", "'RESPOSTA'", "'CONVERSATION'", 
                     "'ALTERNATIVA'", "'ENQUESTA'", "'ITEM'", "'END'" ]

    symbolicNames = [ "<INVALID>", "PO", "PC", "CO", "CC", "COMA", "DP", 
                      "PIC", "INTERROGANT", "IMPLICA", "PREGUNTA", "RESPOSTA", 
                      "CONVERSATION", "ALTERNATIVA", "ENQUESTA", "ITEM", 
                      "END", "NUM", "IDItem", "IDPregunta", "IDResposta", 
                      "IDAlternativa", "PARAULA", "WS" ]

    RULE_chatbot = 0
    RULE_enquesta = 1
    RULE_conversation = 2
    RULE_preg = 3
    RULE_resp = 4
    RULE_opcio = 5
    RULE_item = 6
    RULE_alternativa = 7
    RULE_alternatives = 8

    ruleNames =  [ "chatbot", "enquesta", "conversation", "preg", "resp", 
                   "opcio", "item", "alternativa", "alternatives" ]

    EOF = Token.EOF
    PO=1
    PC=2
    CO=3
    CC=4
    COMA=5
    DP=6
    PIC=7
    INTERROGANT=8
    IMPLICA=9
    PREGUNTA=10
    RESPOSTA=11
    CONVERSATION=12
    ALTERNATIVA=13
    ENQUESTA=14
    ITEM=15
    END=16
    NUM=17
    IDItem=18
    IDPregunta=19
    IDResposta=20
    IDAlternativa=21
    PARAULA=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ChatbotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enquesta(self):
            return self.getTypedRuleContext(EnquestesParser.EnquestaContext,0)


        def END(self):
            return self.getToken(EnquestesParser.END, 0)

        def conversation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ConversationContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ConversationContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_chatbot

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChatbot" ):
                return visitor.visitChatbot(self)
            else:
                return visitor.visitChildren(self)




    def chatbot(self):

        localctx = EnquestesParser.ChatbotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chatbot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.conversation()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << EnquestesParser.IDItem) | (1 << EnquestesParser.IDPregunta) | (1 << EnquestesParser.IDResposta) | (1 << EnquestesParser.IDAlternativa))) != 0)):
                    break

            self.state = 23
            self.enquesta()
            self.state = 24
            self.match(EnquestesParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnquestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DP(self):
            return self.getToken(EnquestesParser.DP, 0)

        def ENQUESTA(self):
            return self.getToken(EnquestesParser.ENQUESTA, 0)

        def PARAULA(self):
            return self.getToken(EnquestesParser.PARAULA, 0)

        def IDItem(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.IDItem)
            else:
                return self.getToken(EnquestesParser.IDItem, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_enquesta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnquesta" ):
                return visitor.visitEnquesta(self)
            else:
                return visitor.visitChildren(self)




    def enquesta(self):

        localctx = EnquestesParser.EnquestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_enquesta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(EnquestesParser.PARAULA)
            self.state = 27
            self.match(EnquestesParser.DP)
            self.state = 28
            self.match(EnquestesParser.ENQUESTA)
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self.match(EnquestesParser.IDItem)
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.IDItem):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConversationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preg(self):
            return self.getTypedRuleContext(EnquestesParser.PregContext,0)


        def resp(self):
            return self.getTypedRuleContext(EnquestesParser.RespContext,0)


        def item(self):
            return self.getTypedRuleContext(EnquestesParser.ItemContext,0)


        def alternativa(self):
            return self.getTypedRuleContext(EnquestesParser.AlternativaContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_conversation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConversation" ):
                return visitor.visitConversation(self)
            else:
                return visitor.visitChildren(self)




    def conversation(self):

        localctx = EnquestesParser.ConversationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conversation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EnquestesParser.IDPregunta]:
                self.state = 34
                self.preg()
                pass
            elif token in [EnquestesParser.IDResposta]:
                self.state = 35
                self.resp()
                pass
            elif token in [EnquestesParser.IDItem]:
                self.state = 36
                self.item()
                pass
            elif token in [EnquestesParser.IDAlternativa]:
                self.state = 37
                self.alternativa()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PregContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DP(self):
            return self.getToken(EnquestesParser.DP, 0)

        def PREGUNTA(self):
            return self.getToken(EnquestesParser.PREGUNTA, 0)

        def INTERROGANT(self):
            return self.getToken(EnquestesParser.INTERROGANT, 0)

        def IDPregunta(self):
            return self.getToken(EnquestesParser.IDPregunta, 0)

        def PARAULA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PARAULA)
            else:
                return self.getToken(EnquestesParser.PARAULA, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_preg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreg" ):
                return visitor.visitPreg(self)
            else:
                return visitor.visitChildren(self)




    def preg(self):

        localctx = EnquestesParser.PregContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_preg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(EnquestesParser.IDPregunta)
            self.state = 41
            self.match(EnquestesParser.DP)
            self.state = 42
            self.match(EnquestesParser.PREGUNTA)
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                self.match(EnquestesParser.PARAULA)
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.PARAULA):
                    break

            self.state = 48
            self.match(EnquestesParser.INTERROGANT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RespContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DP(self):
            return self.getToken(EnquestesParser.DP, 0)

        def RESPOSTA(self):
            return self.getToken(EnquestesParser.RESPOSTA, 0)

        def IDResposta(self):
            return self.getToken(EnquestesParser.IDResposta, 0)

        def opcio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpcioContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpcioContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_resp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResp" ):
                return visitor.visitResp(self)
            else:
                return visitor.visitChildren(self)




    def resp(self):

        localctx = EnquestesParser.RespContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_resp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(EnquestesParser.IDResposta)
            self.state = 51
            self.match(EnquestesParser.DP)
            self.state = 52
            self.match(EnquestesParser.RESPOSTA)
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.opcio()
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.NUM):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpcioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def DP(self):
            return self.getToken(EnquestesParser.DP, 0)

        def PIC(self):
            return self.getToken(EnquestesParser.PIC, 0)

        def PARAULA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.PARAULA)
            else:
                return self.getToken(EnquestesParser.PARAULA, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_opcio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcio" ):
                return visitor.visitOpcio(self)
            else:
                return visitor.visitChildren(self)




    def opcio(self):

        localctx = EnquestesParser.OpcioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_opcio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(EnquestesParser.NUM)
            self.state = 59
            self.match(EnquestesParser.DP)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.match(EnquestesParser.PARAULA)
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.PARAULA):
                    break

            self.state = 65
            self.match(EnquestesParser.PIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DP(self):
            return self.getToken(EnquestesParser.DP, 0)

        def ITEM(self):
            return self.getToken(EnquestesParser.ITEM, 0)

        def IDPregunta(self):
            return self.getToken(EnquestesParser.IDPregunta, 0)

        def IMPLICA(self):
            return self.getToken(EnquestesParser.IMPLICA, 0)

        def IDResposta(self):
            return self.getToken(EnquestesParser.IDResposta, 0)

        def IDItem(self):
            return self.getToken(EnquestesParser.IDItem, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(EnquestesParser.IDItem)
            self.state = 68
            self.match(EnquestesParser.DP)
            self.state = 69
            self.match(EnquestesParser.ITEM)
            self.state = 70
            self.match(EnquestesParser.IDPregunta)
            self.state = 71
            self.match(EnquestesParser.IMPLICA)
            self.state = 72
            self.match(EnquestesParser.IDResposta)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternativaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DP(self):
            return self.getToken(EnquestesParser.DP, 0)

        def ALTERNATIVA(self):
            return self.getToken(EnquestesParser.ALTERNATIVA, 0)

        def IDItem(self):
            return self.getToken(EnquestesParser.IDItem, 0)

        def CO(self):
            return self.getToken(EnquestesParser.CO, 0)

        def alternatives(self):
            return self.getTypedRuleContext(EnquestesParser.AlternativesContext,0)


        def CC(self):
            return self.getToken(EnquestesParser.CC, 0)

        def IDAlternativa(self):
            return self.getToken(EnquestesParser.IDAlternativa, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_alternativa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternativa" ):
                return visitor.visitAlternativa(self)
            else:
                return visitor.visitChildren(self)




    def alternativa(self):

        localctx = EnquestesParser.AlternativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_alternativa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(EnquestesParser.IDAlternativa)
            self.state = 75
            self.match(EnquestesParser.DP)
            self.state = 76
            self.match(EnquestesParser.ALTERNATIVA)
            self.state = 77
            self.match(EnquestesParser.IDItem)
            self.state = 78
            self.match(EnquestesParser.CO)
            self.state = 79
            self.alternatives()
            self.state = 80
            self.match(EnquestesParser.CC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternativesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PO(self):
            return self.getToken(EnquestesParser.PO, 0)

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.COMA)
            else:
                return self.getToken(EnquestesParser.COMA, i)

        def IDItem(self):
            return self.getToken(EnquestesParser.IDItem, 0)

        def PC(self):
            return self.getToken(EnquestesParser.PC, 0)

        def alternatives(self):
            return self.getTypedRuleContext(EnquestesParser.AlternativesContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_alternatives

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternatives" ):
                return visitor.visitAlternatives(self)
            else:
                return visitor.visitChildren(self)




    def alternatives(self):

        localctx = EnquestesParser.AlternativesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_alternatives)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(EnquestesParser.PO)
            self.state = 83
            self.match(EnquestesParser.NUM)
            self.state = 84
            self.match(EnquestesParser.COMA)
            self.state = 85
            self.match(EnquestesParser.IDItem)
            self.state = 86
            self.match(EnquestesParser.PC)
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [EnquestesParser.COMA]:
                self.state = 87
                self.match(EnquestesParser.COMA)
                self.state = 88
                self.alternatives()
                pass
            elif token in [EnquestesParser.CC]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






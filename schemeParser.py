# Generated from scheme.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,31,2,0,7,0,2,1,7,1,1,0,4,0,6,8,0,11,0,12,0,7,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,19,8,1,1,1,1,1,5,1,23,8,1,10,1,12,1,
        26,9,1,1,1,3,1,29,8,1,1,1,0,0,2,0,2,0,0,37,0,5,1,0,0,0,2,28,1,0,
        0,0,4,6,3,2,1,0,5,4,1,0,0,0,6,7,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,
        8,9,1,0,0,0,9,10,5,0,0,1,10,1,1,0,0,0,11,29,5,5,0,0,12,29,5,4,0,
        0,13,29,5,6,0,0,14,29,5,7,0,0,15,29,5,8,0,0,16,29,5,9,0,0,17,19,
        5,1,0,0,18,17,1,0,0,0,18,19,1,0,0,0,19,20,1,0,0,0,20,24,5,2,0,0,
        21,23,3,2,1,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,
        0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,29,5,3,0,0,28,11,1,0,0,0,28,
        12,1,0,0,0,28,13,1,0,0,0,28,14,1,0,0,0,28,15,1,0,0,0,28,16,1,0,0,
        0,28,18,1,0,0,0,29,3,1,0,0,0,4,7,18,24,28
    ]

class schemeParser ( Parser ):

    grammarFileName = "scheme.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'''", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'#t'", "'#f'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "OP", "ID", "STRING", "TRUE", "FALSE", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NUM=4
    OP=5
    ID=6
    STRING=7
    TRUE=8
    FALSE=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(schemeParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(schemeParser.ExprContext)
            else:
                return self.getTypedRuleContext(schemeParser.ExprContext,i)


        def getRuleIndex(self):
            return schemeParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = schemeParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.expr()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1014) != 0)):
                    break

            self.state = 9
            self.match(schemeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return schemeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP(self):
            return self.getToken(schemeParser.OP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(schemeParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class LlamadaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(schemeParser.ExprContext)
            else:
                return self.getTypedRuleContext(schemeParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(schemeParser.TRUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(schemeParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class TextContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(schemeParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)


    class IdentificadorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(schemeParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentificador" ):
                return visitor.visitIdentificador(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = schemeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = schemeParser.OpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(schemeParser.OP)
                pass
            elif token in [4]:
                localctx = schemeParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(schemeParser.NUM)
                pass
            elif token in [6]:
                localctx = schemeParser.IdentificadorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                self.match(schemeParser.ID)
                pass
            elif token in [7]:
                localctx = schemeParser.TextContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 14
                self.match(schemeParser.STRING)
                pass
            elif token in [8]:
                localctx = schemeParser.TrueContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 15
                self.match(schemeParser.TRUE)
                pass
            elif token in [9]:
                localctx = schemeParser.FalseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 16
                self.match(schemeParser.FALSE)
                pass
            elif token in [1, 2]:
                localctx = schemeParser.LlamadaContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 17
                    self.match(schemeParser.T__0)


                self.state = 20
                self.match(schemeParser.T__1)
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1014) != 0):
                    self.state = 21
                    self.expr()
                    self.state = 26
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 27
                self.match(schemeParser.T__2)
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






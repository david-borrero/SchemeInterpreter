#!/usr/bin/env python3
# Generated from scheme.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,76,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,3,3,29,
        8,3,1,3,4,3,32,8,3,11,3,12,3,33,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,44,8,4,1,5,1,5,5,5,48,8,5,10,5,12,5,51,9,5,1,6,1,6,1,6,1,6,5,
        6,57,8,6,10,6,12,6,60,9,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,4,
        9,71,8,9,11,9,12,9,72,1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,1,0,7,2,0,43,43,45,45,1,0,48,57,5,0,42,43,45,45,
        47,47,60,60,62,62,2,0,65,90,97,122,5,0,45,45,48,57,63,63,65,90,97,
        122,3,0,10,10,13,13,34,34,3,0,9,10,13,13,32,32,85,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,23,
        1,0,0,0,5,25,1,0,0,0,7,28,1,0,0,0,9,43,1,0,0,0,11,45,1,0,0,0,13,
        52,1,0,0,0,15,63,1,0,0,0,17,66,1,0,0,0,19,70,1,0,0,0,21,22,5,39,
        0,0,22,2,1,0,0,0,23,24,5,40,0,0,24,4,1,0,0,0,25,26,5,41,0,0,26,6,
        1,0,0,0,27,29,7,0,0,0,28,27,1,0,0,0,28,29,1,0,0,0,29,31,1,0,0,0,
        30,32,7,1,0,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,
        0,0,0,34,8,1,0,0,0,35,44,7,2,0,0,36,37,5,62,0,0,37,44,5,61,0,0,38,
        39,5,60,0,0,39,44,5,61,0,0,40,44,5,61,0,0,41,42,5,60,0,0,42,44,5,
        62,0,0,43,35,1,0,0,0,43,36,1,0,0,0,43,38,1,0,0,0,43,40,1,0,0,0,43,
        41,1,0,0,0,44,10,1,0,0,0,45,49,7,3,0,0,46,48,7,4,0,0,47,46,1,0,0,
        0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,12,1,0,0,0,51,49,
        1,0,0,0,52,58,5,34,0,0,53,57,8,5,0,0,54,55,5,34,0,0,55,57,5,34,0,
        0,56,53,1,0,0,0,56,54,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,
        1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,62,5,34,0,0,62,14,1,0,0,0,
        63,64,5,35,0,0,64,65,5,116,0,0,65,16,1,0,0,0,66,67,5,35,0,0,67,68,
        5,102,0,0,68,18,1,0,0,0,69,71,7,6,0,0,70,69,1,0,0,0,71,72,1,0,0,
        0,72,70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,6,9,0,0,75,20,
        1,0,0,0,8,0,28,33,43,49,56,58,72,1,6,0,0
    ]

class schemeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    NUM = 4
    OP = 5
    ID = 6
    STRING = 7
    TRUE = 8
    FALSE = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'''", "'('", "')'", "'#t'", "'#f'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "OP", "ID", "STRING", "TRUE", "FALSE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "NUM", "OP", "ID", "STRING", "TRUE", 
                  "FALSE", "WS" ]

    grammarFileName = "scheme.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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





# Generated from scheme.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .schemeParser import schemeParser
else:
    from schemeParser import schemeParser

# This class defines a complete generic visitor for a parse tree produced by schemeParser.

class schemeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by schemeParser#root.
    def visitRoot(self, ctx:schemeParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#op.
    def visitOp(self, ctx:schemeParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#numero.
    def visitNumero(self, ctx:schemeParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#identificador.
    def visitIdentificador(self, ctx:schemeParser.IdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#text.
    def visitText(self, ctx:schemeParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#true.
    def visitTrue(self, ctx:schemeParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#false.
    def visitFalse(self, ctx:schemeParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#llamada.
    def visitLlamada(self, ctx:schemeParser.LlamadaContext):
        return self.visitChildren(ctx)



del schemeParser# Ejemplo de uso
from antlr4 import *

from schemeLexer import schemeLexer
from schemeParser import schemeParser
from schemeVisitor import schemeVisitor

from functools import reduce

#TODO: Mirar per que falla el cond

class EvalVisitor(schemeVisitor):
    def __init__(self):
        #TODO: Separar les ops en sumes... i comparacions 

        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y,
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '>=': lambda x, y: x >= y,
            '<=': lambda x, y: x <= y,
            '=': lambda x, y: x == y,
            '<>': lambda x, y: x != y
        }
        self.global_variables = {}
        self.variables = {}
        self.funcions = {}
        self.call_stack = []

    def push_context(self):
        # Añade un nuevo marco de variables locales
        self.call_stack.append({})

    def pop_context(self):
        # Elimina el marco superior
        if self.call_stack:
            self.call_stack.pop()

    def current_context(self):
        # Devuelve el contexto actual (local más global)
        if self.call_stack:
            return {**self.variables, **self.call_stack[-1]}
        return self.variables

    def update_context(self, var, value):
        # Actualiza una variable en el contexto actual
        if self.call_stack:
            self.call_stack[-1][var] = value
        else:
            self.variables[var] = value

    def visitRoot(self, ctx):
        results = []
        for child in ctx.getChildren():
            result = self.visit(child)
            if result is not None:
                results.append(result)
        return results
    
    def visitLlamada(self, ctx):
        [comita, name, *args, _] = ctx.getChildren()
        name = name.getText()
        
        if comita.getText() == '\'':
            # Lista
            args = [self.visit(arg) for arg in args]
            return args


        if name == 'define':
            first_arg = args[0]
            
            if first_arg.getChildCount() > 0 and first_arg.getChild(0).getText() == '(':
                # Caso de definición de función
                [_, func_name, *params, __] = first_arg.getChildren()

                func_name = func_name.getText()
                params = [p.getText() for p in params]

                [_, *body] = args

                # Guardar la función como (parámetros, cuerpo)
                self.funcions[func_name] = (params, body)

            else:
                # Definición de variable
                [identificador, valor] = args

                if valor.getChildCount() > 0 and valor.getChild(0).getText() == '\'':
                    # lista
                    [_, _, *valores, __] = valor.getChildren()
                    valores = [self.visit(v) for v in valores]
                    self.global_variables[identificador.getText()] = valores

                else:
                    valor = self.visit(valor)
                    self.global_variables[identificador.getText()] = valor

            return None
        
        elif name == 'let':
            # Crear un nuevo contexto para las variables locales
            self.push_context()

            [variables, *body] = args
            [_, *variables, __] = variables.getChildren()

            for var in variables:
                [_, identificador, valor, _] = var.getChildren()
            
                valor = self.visit(valor)
                self.update_context(identificador.getText(), valor)
            
            for expr in body:
                result = self.visit(expr)

            # Restaurar el contexto anterior
            self.pop_context()

            return result
        
        elif name == 'read':
            # Leer un valor de la consola
            valor = InputStream(input())
            lexer = schemeLexer(valor)
            token_stream = CommonTokenStream(lexer)
            parser = schemeParser(token_stream)
            tree = parser.root()
            return self.visit(tree)[0]
        
        elif name == 'if':
            # Evaluar el `if`
            if len(args) != 3:
                raise Exception("La expresión `if` requiere 3 argumentos: condición, verdadero, falso")

            condicion = self.visit(args[0])
            if condicion:  # Evaluar la condición
                return self.visit(args[1])  # Expresión si verdadero
            else:
                return self.visit(args[2])  # Expresión si falso
            
        elif name == 'cond':
            # Evaluar el `cond`
            for arg in args:
                [_, condicion, expresion, _] = arg.getChildren()

                if condicion.getText() == 'else':
                    return self.visit(expresion)

                if self.visit(condicion):
                    return self.visit(expresion)
            
        elif name == 'car':
            # Devuelve el primer elemento de una lista
            [lista] = args
            lista = self.visit(lista)
            return lista[0]
        
        elif name == 'cdr':
            # Devuelve todos los elementos de una lista excepto el primero
            [lista] = args
            lista = self.visit(lista)
            return lista[1:]

        elif name == 'cons':
            # Agrega un elemento al principio de una lista
            [elemento, lista] = args
            elemento = self.visit(elemento)
            lista = self.visit(lista)
            return [elemento] + lista

        elif name == 'null?':
            # Comprueba si una lista está vacía
            [lista] = args
            lista = self.visit(lista)
            return len(lista) == 0
        
        elif name == 'display':
            # Mostrar un valor en la consola
            [valor] = args
            
            valor = self.visit(valor)

            if valor == False:
                print('#f')
            elif valor == True:
                print('#t')
            else:
                print(valor)

            return None

        elif name == 'newline':
            # Imprimir una nueva línea
            print()
            return None
        
        elif name == 'and':
            # Evaluar una serie de expresiones lógicas con `and`
            for arg in args:
                if not self.visit(arg):
                    return False
            return True
        
        elif name == 'or':
            # Evaluar una serie de expresiones lógicas con `or`
            
            for arg in args:
                if self.visit(arg):
                    return True
            return False
        
        elif name == 'not':
            # Negar una expresión lógica
            if len(args) != 1:
                raise Exception("La funció `not` requereix 1 argument")

            [arg] = args
            return not self.visit(arg)

        elif name in self.funcions:
            # Llamada a una función definida por el usuario
            params, body = self.funcions[name]

            args = [self.visit(arg) for arg in args]

            if len(params) != len(args):
                raise Exception(f"La función '{name}' esperaba {len(params)} argumentos, pero recibió {len(args)}.")

            # Crear un nuevo contexto para la llamada
            self.push_context()

            # Asignar los argumentos a los parámetros en el nuevo contexto
            for param, arg in zip(params, args):
                self.update_context(param, arg)

            # Evaluar el cuerpo de la función
            for expr in body:
                result = self.visit(expr)

            # Restaurar el contexto anterior
            self.pop_context()

            return result
        
        elif name in self.current_context():
            func = self.current_context()[name]
            args = [self.visit(arg) for arg in args]

            if isinstance(func, tuple):
                # Es una función definida por el usuario
                params, body = func

                if len(params) != len(args):
                    raise Exception(f"La función '{name}' esperaba {len(params)} argumentos, pero recibió {len(args)}.")

                # Crear un nuevo contexto para la función
                self.push_context()

                # Asocia parámetros con argumentos
                for param, arg in zip(params, args):
                    self.update_context(param, arg)

                # Evalúa el cuerpo de la función
                for expr in body:
                    result = self.visit(expr)

                # Restaura el contexto
                self.pop_context()

                return result
            elif callable(func):
                # Es una función Python incorporada o pasada como argumento
                return func(*args)
            else:
                raise Exception(f"El nombre '{name}' no es una función válida.")

        elif name in self.operators:
            # Evaluar operadores
            op = self.operators[name]
            args = [self.visit(arg) for arg in args]
            return reduce(op, args)

        else:
            raise Exception(f"Nombre no reconocido: {name}")

    
    def visitNumero(self, ctx):
        return int(ctx.getText())
    
    def visitText(self, ctx):
        return ctx.getText()[1:-1]
    
    def visitIdentificador(self, ctx):
        name = ctx.getText()
        if name in self.funcions:
            # Si el identificador está en funciones, devuelve la función
            return self.funcions[name]
        elif name in self.current_context():
            return self.current_context()[name]
        elif name in self.global_variables:
            return self.global_variables[name]
        else:
            raise Exception(f"Variable no definida: {name}")
        
    def visitTrue(self, ctx):
        return True

    def visitFalse(self, ctx):
        return False




input_stream = FileStream('./entrada.scm')
lexer = schemeLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = schemeParser(token_stream)
tree = parser.root()

# print(tree.toStringTree(recog=parser))

evaluator = EvalVisitor()
evaluator.visit(tree)

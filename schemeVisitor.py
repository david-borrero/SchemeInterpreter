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



del schemeParser
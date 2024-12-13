# Ejemplo de uso
from antlr4 import *

from schemeLexer import schemeLexer
from schemeParser import schemeParser
from schemeVisitor import schemeVisitor

from functools import reduce

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
        self.variables = {}
        self.funcions = {}
        self.parametres = {}

    # a partir de schemeVisitor i scheme.g4

    def visitRoot(self, ctx):
        results = []
        for child in ctx.getChildren():
            result = self.visit(child)
            if result is not None:
                results.append(result)
        return results
    
    def visitLlamada(self, ctx):
        [_, name, *args, _] = ctx.getChildren()
        name = name.getText()
        
        if name == 'define':
            [_, identificador, valor, __] = args
            identificador = identificador.getText()
            valor = self.visit(valor)
            self.variables[identificador] = valor
            return valor
        
        elif name in self.operators:
            op = self.operators[name]
            args = [self.visit(arg) for arg in args]
            return reduce(op, args)

    
    def visitNumero(self, ctx):
        return int(ctx.getText())
    
    def visitIdentificador(self, ctx):
        return self.variables[ctx.getText()]



input_stream = StdinStream()
lexer = schemeLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = schemeParser(token_stream)
tree = parser.root()

# print(tree.toStringTree(recog=parser))

evaluator = EvalVisitor()
result = evaluator.visit(tree)

print(result)


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
            return {**self.global_variables, **self.call_stack[-1]}
        return self.global_variables

    def update_context(self, var, value):
        # Actualiza una variable en el contexto actual
        if self.call_stack:
            self.call_stack[-1][var] = value
        else:
            self.global_variables[var] = value

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
            first_arg = args[0]
            
            if first_arg.getChildCount() > 0 and first_arg.getChild(0).getText() == '(':
                # Caso de definición de función
                [_, func_name, *params, __] = first_arg.getChildren()
                func_name = func_name.getText()
                params = [p.getText() for p in params]
                body = args[1]

                # Guardar la función como (parámetros, cuerpo)
                self.funcions[func_name] = (params, body)
            else:
                # Definición de variable
                [_, identificador, valor, __] = args
                identificador = identificador.getText()
                valor = self.visit(valor)
                self.global_variables[identificador] = valor

            return None
        
        elif name == 'if':
            # Evaluar el `if`
            if len(args) != 3:
                raise Exception("La expresión `if` requiere 3 argumentos: condición, verdadero, falso")

            condicion = self.visit(args[0])
            if condicion:  # Evaluar la condición
                return self.visit(args[1])  # Expresión si verdadero
            else:
                return self.visit(args[2])  # Expresión si falso

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
            result = self.visit(body)

            # Restaurar el contexto anterior
            self.pop_context()

            return result

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
        if name in self.current_context():
            return self.current_context()[name]
        else:
            raise Exception(f"Variable no definida: {name}")



input_stream = StdinStream()
lexer = schemeLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = schemeParser(token_stream)
tree = parser.root()

# print(tree.toStringTree(recog=parser))

evaluator = EvalVisitor()
result = evaluator.visit(tree)

print(result)


# Ejemplo de uso
from antlr4 import *

from schemeLexer import schemeLexer
from schemeParser import schemeParser
from schemeVisitor import schemeVisitor

from functools import reduce

#TODO: Mirar perque falla el let amb el read

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
            
            for arg in args:
                print(arg.getText())

            [variables, *body] = args
            [_, *variables, __] = variables.getChildren()

            
            for var in variables:
                [_, identificador, valor, _] = var.getChildren()
            
                print(valor.getText())
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
            return valor
        
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
                condicion = self.visit(condicion)
                if condicion:
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
        
        elif name == 'and':
            # Evaluar una serie de expresiones lógicas con `and`
            for arg in args:
                if not self.visit(arg):
                    return False
            return True

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
        elif name in self.global_variables:
            return self.global_variables[name]
        else:
            raise Exception(f"Variable no definida: {name}")
        
    def visitTrue(self, ctx):
        return True

    def visitFalse(self, ctx):
        return False




input_stream = StdinStream()
lexer = schemeLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = schemeParser(token_stream)
tree = parser.root()

# print(tree.toStringTree(recog=parser))

evaluator = EvalVisitor()
result = evaluator.visit(tree)

print(result)


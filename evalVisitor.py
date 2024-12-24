# eval_visitor.py
from schemeVisitor import schemeVisitor
from functools import reduce

from antlr4 import CommonTokenStream

class EvalVisitor(schemeVisitor):
    def __init__(self):
        self.operators = self.initialize_operators()
        self.global_variables = {}
        self.variables = {}
        self.funcions = {}
        self.call_stack = []

    def initialize_operators(self):
        return {
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

    def push_context(self):
        self.call_stack.append({})

    def pop_context(self):
        if self.call_stack:
            self.call_stack.pop()

    def current_context(self):
        if self.call_stack:
            return {**self.variables, **self.call_stack[-1]}
        return self.variables

    def update_context(self, var, value):
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
            return self.handle_list(args)

        if name == 'define':
            return self.handle_define(args)

        if name == 'let':
            return self.handle_let(args)

        if name == 'read':
            return self.handle_read()

        if name == 'if':
            return self.handle_if(args)

        if name == 'cond':
            return self.handle_cond(args)

        if name in ['car', 'cdr', 'cons', 'null?']:
            return self.handle_list_operations(name, args)

        if name in ['display', 'newline']:
            return self.handle_output(name, args)

        if name in ['and', 'or', 'not']:
            return self.handle_logic_operations(name, args)

        if name in self.funcions:
            return self.call_user_function(name, args)

        if name in self.current_context():
            return self.call_context_function(name, args)

        if name in self.operators:
            return self.handle_operator(name, args)

        raise Exception(f"Nombre no reconocido: {name}")

    def handle_list(self, args):
        return [self.visit(arg) for arg in args]

    def handle_define(self, args):
        first_arg = args[0]
        if first_arg.getChildCount() > 0 and first_arg.getChild(0).getText() == '(':
            self.define_function(args)
        else:
            self.define_variable(args)

    def define_function(self, args):
        [_, func_name, *params, __] = args[0].getChildren()
        func_name = func_name.getText()
        params = [p.getText() for p in params]
        [_, *body] = args
        self.funcions[func_name] = (params, body)

    def define_variable(self, args):
        [identificador, valor] = args
        if valor.getChildCount() > 0 and valor.getChild(0).getText() == '\'':
            [_, _, *valores, __] = valor.getChildren()
            valores = [self.visit(v) for v in valores]
            self.global_variables[identificador.getText()] = valores
        else:
            valor = self.visit(valor)
            self.global_variables[identificador.getText()] = valor

    def handle_let(self, args):
        self.push_context()
        [variables, *body] = args
        [_, *variables, __] = variables.getChildren()
        for var in variables:
            [_, identificador, valor, _] = var.getChildren()
            valor = self.visit(valor)
            self.update_context(identificador.getText(), valor)
        result = None
        for expr in body:
            result = self.visit(expr)
        self.pop_context()
        return result

    def handle_read(self):
        from schemeLexer import schemeLexer
        from schemeParser import schemeParser
        from antlr4 import InputStream

        valor = InputStream(input())
        lexer = schemeLexer(valor)
        token_stream = CommonTokenStream(lexer)
        parser = schemeParser(token_stream)
        tree = parser.root()
        
        return self.visit(tree)[0]

    def handle_if(self, args):
        if len(args) != 3:
            raise Exception("La expresión `if` requiere 3 argumentos: condición, verdadero, falso")
        condicion = self.visit(args[0])
        return self.visit(args[1] if condicion else args[2])

    def handle_cond(self, args):
        for arg in args:
            [_, condicion, expresion, _] = arg.getChildren()
            if condicion.getText() == 'else' or self.visit(condicion):
                return self.visit(expresion)

    def handle_list_operations(self, name, args):
        lista = self.visit(args[0])
        if name == 'car':
            return lista[0]
        if name == 'cdr':
            return lista[1:]
        if name == 'cons':
            elemento = self.visit(args[0])
            return [elemento] + lista
        if name == 'null?':
            return len(lista) == 0

    def handle_output(self, name, args):
        if name == 'display':
            valor = self.visit(args[0])
            print('#f' if valor is False else '#t' if valor is True else valor, end='')
        elif name == 'newline':
            print()

    def handle_logic_operations(self, name, args):
        if name == 'and':
            return all(self.visit(arg) for arg in args)
        if name == 'or':
            return any(self.visit(arg) for arg in args)
        if name == 'not':
            if len(args) != 1:
                raise Exception("La función `not` requiere 1 argumento")
            return not self.visit(args[0])

    def call_user_function(self, name, args):
        params, body = self.funcions[name]
        args = [self.visit(arg) for arg in args]
        if len(params) != len(args):
            raise Exception(f"La función '{name}' esperaba {len(params)} argumentos, pero recibió {len(args)}.")
        self.push_context()
        for param, arg in zip(params, args):
            self.update_context(param, arg)
        result = None
        for expr in body:
            result = self.visit(expr)
        self.pop_context()
        return result

    def call_context_function(self, name, args):
        func = self.current_context()[name]
        args = [self.visit(arg) for arg in args]
        if isinstance(func, tuple):
            params, body = func
            if len(params) != len(args):
                raise Exception(f"La función '{name}' esperaba {len(params)} argumentos, pero recibió {len(args)}.")
            self.push_context()
            for param, arg in zip(params, args):
                self.update_context(param, arg)
            result = None
            for expr in body:
                result = self.visit(expr)
            self.pop_context()
            return result
        if callable(func):
            return func(*args)
        raise Exception(f"El nombre '{name}' no es una función válida.")

    def handle_operator(self, name, args):
        op = self.operators[name]
        args = [self.visit(arg) for arg in args]
        return reduce(op, args)

    def visitNumero(self, ctx):
        return int(ctx.getText())

    def visitText(self, ctx):
        return ctx.getText()[1:-1]

    def visitIdentificador(self, ctx):
        name = ctx.getText()
        if name in self.funcions:
            return self.funcions[name]
        if name in self.current_context():
            return self.current_context()[name]
        if name in self.global_variables:
            return self.global_variables[name]
        raise Exception(f"Variable no definida: {name}")

    def visitTrue(self, ctx):
        return True

    def visitFalse(self, ctx):
        return False

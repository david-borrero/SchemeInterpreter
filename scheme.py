from antlr4 import *
from schemeLexer import schemeLexer
from schemeParser import schemeParser
from evalVisitor import EvalVisitor
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file')
    args = parser.parse_args()

    entrada = args.input
    
    if not entrada.endswith('.scm'):
        print("Error: El archivo debe tener la extensión .scm")
        exit(1)

    # Verificar que el archivo exista
    if not os.path.isfile(entrada):
        print(f"Error: El archivo '{entrada}' no existe.")
        exit(1)

    input_stream = FileStream(entrada)
    lexer = schemeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = schemeParser(token_stream)
    tree = parser.root()

    visitor = EvalVisitor()
    
    try:
        visitor.visit(tree)
    except Exception as e:
        print(f"Error: {e}")
        exit(1) 
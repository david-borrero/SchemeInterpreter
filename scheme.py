from antlr4 import *
from schemeLexer import schemeLexer
from schemeParser import schemeParser
from evalVisitor import EvalVisitor
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file')
    args = parser.parse_args()

    input_stream = FileStream(args.input)
    lexer = schemeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = schemeParser(token_stream)
    tree = parser.root()

    visitor = EvalVisitor()
    visitor.visit(tree)
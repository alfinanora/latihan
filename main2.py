import vcl_lexer
import vcl_parser
import vcl_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = vcl_lexer.BasicLexer()
    parser = vcl_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('VCL > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            vcl_interpreter.BasicExecute(tree, env)

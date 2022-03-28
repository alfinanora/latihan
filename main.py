import vcl_lexer
import vcl_parser
import vcl_interpreter

from sys import *

#DENGAN MASUKAN BAHASAKU.VCL
lexer = vcl_lexer.BasicLexer()
parser = vcl_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    vcl_interpreter.BasicExecute(tree, env)

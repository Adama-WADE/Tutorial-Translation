import commonmark
import json
import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("string_positions.txt", "a")
   
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()

with open(r'C:\Users\Adama\Documents\Tutorial-Translation\Marp.md','r', encoding="utf-8") as fin:
    md = fin.read()

parser = commonmark.Parser()
ast = parser.parse(md)

# AST object API is more complicated but necessary, as it includes row/column information for each block
commonmark.dumpAST(ast) # pretty print generated AST structure
""" with open('output_ast_1.txt', 'w', encoding="utf-8") as fout:
    fout.write(str(commonmark.dumpJSON(ast))) """
   

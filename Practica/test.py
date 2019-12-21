import sys
import pickle as pk
import networkx as nx
import matplotlib.pyplot as plt
from antlr4 import *
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from EnquestesVisitor import EnquestesVisitor

if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
    input_stream = InputStream(input('? '))
    
lexer = EnquestesLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = EnquestesParser(token_stream)
tree = parser.chatbot()

visitor = EnquestesVisitor()
happiness = visitor.visit(tree)

nx.write_gpickle(happiness, "hi.pickle")

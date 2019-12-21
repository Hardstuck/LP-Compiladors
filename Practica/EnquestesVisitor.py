# Generated from Enquestes.g by ANTLR 4.7.2
from antlr4 import *
import matplotlib.pyplot as plt
import networkx as nx
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.

class EnquestesVisitor(ParseTreeVisitor):
    def __init__(self):
        self.AST = nx.DiGraph()
        self.items = {} #auxiliar dictionary to link items with questions

    # Visit a parse tree produced by EnquestesParser#chatbot.
    def visitChatbot(self, ctx:EnquestesParser.ChatbotContext):
        self.visitChildren(ctx)
        return self.AST


    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx:EnquestesParser.EnquestaContext):
        g = ctx.getChildren()
        n = ctx.getChildCount()
        l = [next(g) for i in range(n)]
        first = l[0].getText();
        for i in range(3, n):
            self.AST.add_edge(first, self.items[l[i].getText()])
            first = self.items[l[i].getText()]
        #nx.draw(self.AST, with_labels = True)
        #plt.show()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#conversation.
    def visitConversation(self, ctx:EnquestesParser.ConversationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#preg.
    def visitPreg(self, ctx:EnquestesParser.PregContext):
        n = next(ctx.getChildren())
        self.AST.add_node(n.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#resp.
    def visitResp(self, ctx:EnquestesParser.RespContext):
        n = next(ctx.getChildren())
        self.AST.add_node(n.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#opcio.
    def visitOpcio(self, ctx:EnquestesParser.OpcioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        g = ctx.getChildren()
        n = ctx.getChildCount()
        l = [next(g) for i in range(n)]
        self.AST.add_edge(l[3].getText(), l[5].getText(), item = l[0].getText())
        self.items[l[0].getText()] = l[3].getText()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#alternativa.
    def visitAlternativa(self, ctx:EnquestesParser.AlternativaContext):
        n = ctx.getChildCount()
        g = ctx.getChildren()
        l = [next(g) for i in range(n)]
        listalternatives = self.visit(l[5])
        pregunta = self.items[l[3].getText()]
        for (a, i) in listalternatives:
            self.AST.add_edge(pregunta, self.items[i], alternativa = a)


    # Visit a parse tree produced by EnquestesParser#alternatives.
    def visitAlternatives(self, ctx:EnquestesParser.AlternativesContext):
        n = ctx.getChildCount()
        g = ctx.getChildren()
        l = [next(g) for i in range(n)]
        if n == 7:
            return [(l[1].getText(), l[3].getText()), self.visit(l[6])]
        else:
            return (l[1].getText(), l[3].getText())



#del EnquestesParser

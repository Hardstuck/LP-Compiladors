from telegram.ext import Updater
from telegram.ext import CommandHandler
from antlr4 import *
if __name__ is not None and '.' in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser
    
class ExprVisitor(ParseTreeVisitor):
    def visitRoot(self, ctx:ExprParser.RootContext):
        n = next(ctx.getChildren())
        print(self.visit(n))
        
    def visitExpr(self, ctx:ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            return int(n.getText()))
        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            l = [next(g) for i in range(3)]
            return self.visit

    
    
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = "Hi, let's talk!")
    
def author(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text = "Author: Niebo Zhang\nEmail: niebo.zhang@est.fib.upc.edu")
    

    
TOKEN = open('token.txt').read().strip()

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('author', author))

updater.start_polling()

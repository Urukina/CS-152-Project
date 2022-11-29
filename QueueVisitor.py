# Generated from Queue.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QueueParser import QueueParser
else:
    from QueueParser import QueueParser

# This class defines a complete generic visitor for a parse tree produced by QueueParser.

class QueueVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QueueParser#prog.
    def visitProg(self, ctx:QueueParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#stmts.
    def visitStmts(self, ctx:QueueParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#stmt.
    def visitStmt(self, ctx:QueueParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#createQueue.
    def visitCreateQueue(self, ctx:QueueParser.CreateQueueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#queueOptions.
    def visitQueueOptions(self, ctx:QueueParser.QueueOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#enqueueOptions.
    def visitEnqueueOptions(self, ctx:QueueParser.EnqueueOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#dequeue.
    def visitDequeue(self, ctx:QueueParser.DequeueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#clear.
    def visitClear(self, ctx:QueueParser.ClearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#printQueueOptions.
    def visitPrintQueueOptions(self, ctx:QueueParser.PrintQueueOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#theQueue.
    def visitTheQueue(self, ctx:QueueParser.TheQueueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#elemental.
    def visitElemental(self, ctx:QueueParser.ElementalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#heads.
    def visitHeads(self, ctx:QueueParser.HeadsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#tails.
    def visitTails(self, ctx:QueueParser.TailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#booleanQueue.
    def visitBooleanQueue(self, ctx:QueueParser.BooleanQueueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#empty.
    def visitEmpty(self, ctx:QueueParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#populated.
    def visitPopulated(self, ctx:QueueParser.PopulatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#inside.
    def visitInside(self, ctx:QueueParser.InsideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#miscQueue.
    def visitMiscQueue(self, ctx:QueueParser.MiscQueueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#swap.
    def visitSwap(self, ctx:QueueParser.SwapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#combine.
    def visitCombine(self, ctx:QueueParser.CombineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#reverse.
    def visitReverse(self, ctx:QueueParser.ReverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QueueParser#exQueue.
    def visitExQueue(self, ctx:QueueParser.ExQueueContext):
        return self.visitChildren(ctx)



del QueueParser
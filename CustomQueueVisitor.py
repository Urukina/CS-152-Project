from QueueParser import QueueParser
from QueueVisitor import QueueVisitor
from PriorityQueue import PriorityQueue, obj


class CustomQueueVisitor(QueueVisitor):
    def __init__(self):
        super(CustomQueueVisitor, self).__init__()
        self.variables = {}

    def visitCreateQueue(self, ctx:QueueParser.CreateQueueContext):
        var = str(ctx.queueName.text)
        if var in self.variables:
            print("Error: " + var + " has already been initialized")
        else:
            self.variables[var] = PriorityQueue(ctx.queueSize.text)
            print (var + " has been created")

    def visitEnqueueOptions(self, ctx:QueueParser.EnqueueOptionsContext):
        var = str(ctx.queueName.text)
        val = str(ctx.elements.text)
        pri = str(ctx.priority.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + " to push")
        else:
            if self.variables[var].isEmpty():
                self.variables[var].insert(obj(ctx.elements.text, ctx.priority.text))
                print(ctx.elements.text + " has been added to queue " + var)
            else:
                if self.variables[var].queue[0].value.find('@') != -1 and ctx.elements.text.find('@') != -1:
                    self.variables[var].insert(obj(ctx.elements.text, ctx.priority.text))
                    print(ctx.elements.text + " has been added to queue " + var)
                elif self.variables[var].queue[0].value.find('#') != -1 and ctx.elements.text.find('#') != -1:
                    print(ctx.elements.text + " has been added to queue " + var)
                    print(ctx.elements.text + " has been added with priority " + ctx.priority.text)
                elif self.variables[var].queue[0].value.find('.') != -1 and ctx.elements.text.find('.') != -1:
                    self.variables[var].insert(obj(ctx.elements.text, ctx.priority.text))
                    print(ctx.elements.text + " has been added to queue " + var)
                elif self.variables[var].queue[0].value.find('*') != -1 and ctx.elements.text.find('*') != -1:
                    self.variables[var].insert(obj(ctx.elements.text, ctx.priority.text))
                    print(ctx.elements.text + " has been added to queue " + var)
                else:
                    print("Error: Wrong datatype for " + var)

    def visitDequeue(self, ctx:QueueParser.DequeueContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var)
        else:
            self.variables[var].delete()
            print("Head has been dequeued")

    def visitClear(self, ctx:QueueParser.ClearContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + "to clear")
        else:
            while not self.variables[str(ctx.queueName.text)].isEmpty():
                self.variables[var].delete()
                print("All contents for " + var + " has been cleared")

    def visitTheQueue(self, ctx:QueueParser.TheQueueContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + " to print")
        else:
            print("Printing elements from: " + var)
            self.variables[var].printQueue()

    def visitElemental(self, ctx:QueueParser.ElementalContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + " to print")
        else:
            self.variables[var].printElementWithPriority(ctx.priority.text)

    def visitHeads(self, ctx:QueueParser.HeadsContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + " to print")
        else:
            self.variables[var].printHead()

    def visitTails(self, ctx:QueueParser.HeadsContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + " to print")
        else:
            self.variables[var].printTail()

    def visitEmpty(self, ctx:QueueParser.EmptyContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + " to check if queue is empty")
        else:
            if self.variables[var].isEmpty():
                print(var + " is empty")
            else:
                print(var + " is not empty")

    def visitPopulated(self, ctx:QueueParser.PopulatedContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + " to check if queue is populated")
        else:
            if not self.variables[var].isEmpty():
                print(ctx.queueName.text + " is populated")
            else:
                print(ctx.queueName.text + " is not populated")

    def visitInside(self, ctx:QueueParser.InsideContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + " to check if" + ctx.elementName.text + "exists in queue")
        else:
            self.variables[str((ctx.queueName.text))].findValue(ctx.elementName.text)

    def visitCombine(self, ctx:QueueParser.CombineContext):
        varOne = str(ctx.queueName.text)
        varTwo = str(ctx.queueNameTwo.text)
        if varOne not in self.variables or varTwo not in self.variables:
            print("Error: No queue exists for one of the two variables to combine")
        elif varOne == varTwo:
            print("Error: queue cannot combine itself")
        else:
            if self.variables[varOne].queue[0].value.find('@') != -1 and \
                    self.variables[varTwo].queue[0].value.find('@') != -1:
                self.variables[varOne].concatenate(self.variables[varTwo])
                print(varOne + " and " + varTwo + " has been combined")
            elif self.variables[varOne].queue[0].value.find('#') != -1 and \
                    self.variables[varTwo].queue[0].value.find('#') != -1:
                self.variables[varOne].concatenate(self.variables[varTwo])
                print(varOne + " and " + varTwo + " has been combined")
            elif self.variables[varOne].queue[0].value.find('.') != -1 and \
                    self.variables[varTwo].queue[0].value.find('.') != -1:
                self.variables[varOne].concatenate(self.variables[varTwo])
                print(varOne + " and " + varTwo + " has been combined")
            else:
                print("Cannot combine queues: Mismatched data types")

    def visitSwap(self, ctx:QueueParser.SwapContext):
        varOne = str(ctx.queueName.text)
        varTwo = str(ctx.queueNameTwo.text)
        if varOne not in self.variables or varTwo not in self.variables:
            print("Error: No queue exists for one of the two variables to swap")
        elif varOne == varTwo:
            print("Error: queue cannot swap contents with itself")
        else:
            self.variables[varOne].swap(self.variables[varTwo])
            print("All contents from " + varOne + " " + varTwo + " has been swapped")

    def visitReverse(self, ctx:QueueParser.ReverseContext):
        var = str(ctx.queueName.text)
        if var not in self.variables:
            print("Error: No queue exists for " + var + " to check if" + ctx.elementName.text + "exists in queue")
        else:
            self.variables[var].reverse()
            print("Elements have been reversed")

    def visitExQueue(self, ctx:QueueParser.ExQueueContext):
        var = str(ctx.queueName.text)
        elm = str(ctx.elementName.text)
        if var not in self.variables:
            print("Error: No queue " + var + " exists for " + elm + " to exit")
        else:
            self.variables[var].exitQueue(elm)

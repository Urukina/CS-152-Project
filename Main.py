import sys
from antlr4 import *
from QueueLexer import QueueLexer
from QueueParser import QueueParser
from CustomQueueVisitor import CustomQueueVisitor

def main(argv):
    input = InputStream("Create [queueName] [4].\n"
                        "Is [queueName] empty?\n"
                        "Enqueue [queueName] [@TwitterHandle][23].\n"
                        "Enqueue [queueName] [@DaiyaKumori][0].\n"
                        "EQ [queueName] [@MagicalSenpai][0].\n"
                        "EQ [queueName] [@InternetH0F][1].\n"
                        "EQ [queueName] [@Interne][3].\n"
                        "DQ [queueName].\n"
                        "Print queue [queueName].\n"
                        "Spawn [queueTwo] [2].\n"
                        "Enqueue [queueTwo] [@edneddy2] [4].\n"
                        "Concatenate queues [queueName] [queueTwo].\n"
                        "Print queue [queueName].\n"
                        "Is [queueTwo] empty?\n"
                        "Output queue [queueTwo].\n"
                        "Enqueue [queueTwo] [Urukina#0579] [6].\n"
                        "EQ [queueTwo] [Magical Senpai#1407] [14].\n"
                        "EQ [queueTwo] [edneddy2#9900] [1].\n"
                        "Output queue [queueTwo].\n"
                        "[queueName] + [queueTwo].\n"
                        "[queueName] <-> [queueTwo].\n"
                        "Is [queueTwo] empty?\n"
                        "Print queue [queueTwo].\n"
                        "[queueTwo]R.\n"
                        "Print queue [queueTwo].\n"
                        "EQ [queueName] [edneddy2#9900] [9].\n"
                        "Print queue [queueName].\n"
                        "Exit from [queueTwo] [@edneddy3].\n"
                        "Exit from [queueTwo] [@TwitterHandle].\n"
                        "Print queue [queueTwo].\n"
                        "Print queue [queueName].\n"
                        "Spawn [IPQueue] [49].\n"
                        "Enqueue [IPQueue] [45.464.814.76] [0].\n"
                        "Enqueue [IPQueue] [45.444.854.78] [1].\n"
                        "EQ [IPQueue] [98.400.854.28] [0].\n"
                        "Output queue [IPQueue].\n"
                        "[queueTwo] + [queueTwo].\n"
                        "Output queue [queueTwo].\n"
                        )
    lexer = QueueLexer(input)
    stream = CommonTokenStream(lexer)
    parse = QueueParser(stream)
    tree = parse.prog()

    res = CustomQueueVisitor().visitProg(tree)

if __name__ == '__main__':
    main(sys.argv)

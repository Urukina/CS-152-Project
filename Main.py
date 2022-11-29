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
                        "EQ [queueName] [@InternetH0F][0].\n"
                        "EQ [queueName] [@Interne][3].\n"
                        "DQ [queueName].\n"
                        "Print queue [queueName].\n"
                        "Spawn [queueTwo] [8].\n"
                        "Enqueue [queueTwo] [@edneddy2] [4].\n"
                        "Concatenate queues [queueName] [queueTwo].\n"
                        "Print queue [queueName].\n"
                        "Is [queueTwo] empty?\n"
                        "Output queue [queueTwo].\n"
                        "Enqueue [queueTwo] [Urukina#0579] [6].\n"
                        "Output queue [queueTwo].\n"
                        "[queueName] + [queueTwo].\n"
                        "[queueName] <-> [queueTwo].\n"
                        "Is [queueTwo] empty?\n"
                        "Print queue [queueTwo].\n"
                        "[queueTwo]R.\n"
                        "Print queue [queueTwo].\n"
                        "Exit from [queueTwo] [@edneddy3].\n"
                        "Print queue [queueTwo].\n"
                        "Print queue [queueName].\n"
                        )
    lexer = QueueLexer(input)
    stream = CommonTokenStream(lexer)
    parse = QueueParser(stream)
    tree = parse.prog()

    res = CustomQueueVisitor().visitProg(tree)

if __name__ == '__main__':
    main(sys.argv)

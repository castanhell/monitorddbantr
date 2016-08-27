from antlr4 import *
import antlr4
from monitorddblexer import monitorddblexer
from monitorddbparser import monitorddbparser
from antlr4.tree.Trees import Trees


def main():
    lexer = monitorddblexer(FileStream("samplelanguage.json"))
    stream = antlr4.CommonTokenStream(lexer)
    parser = monitorddbparser(stream)
    tree = parser.root()
    print(Trees.toStringTree(tree))

if __name__ == '__main__':
    main()

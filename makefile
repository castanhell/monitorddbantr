
CC = antlr4
all : monitorddblexer.g4
	$(CC) -Dlanguage=Python2 monitorddblexer.g4 monitorddbparser.g4

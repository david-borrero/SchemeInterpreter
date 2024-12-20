# Nombres de los archivos
GRAMMAR = scheme
GRAMMAR_FILE = $(GRAMMAR).g4
LEXER = $(GRAMMAR)Lexer.py
PARSER = $(GRAMMAR)Parser.py
VISITOR = $(GRAMMAR)Visitor.py
BASEVISITOR = $(GRAMMAR)BaseVisitor.py
EXECUTABLE = scheme.py
EVALVISITOR = evalVisitor.py

# Comando de ANTLR
ANTLR = antlr4

# Regla principal
all: $(EXECUTABLE)

# Genera el ejecutable
$(EXECUTABLE): $(LEXER) $(PARSER) $(VISITOR) $(BASEVISITOR) $(EVALVISITOR)
	echo "#!/usr/bin/env python3" > $(EXECUTABLE)
	cat $(LEXER) $(PARSER) $(VISITOR) $(BASEVISITOR) $(EVALVISITOR) >> $(EXECUTABLE)
	chmod +x $(EXECUTABLE)

# Genera los archivos de ANTLR
$(LEXER) $(PARSER) $(VISITOR) $(BASEVISITOR): $(GRAMMAR_FILE)
	$(ANTLR) -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR_FILE)

# Limpia los archivos generados
clean:
	rm -f $(LEXER) $(PARSER) $(VISITOR) $(BASEVISITOR) $(EXECUTABLE) scheme.tokens schemeLexer.tokens scheme.interp schemeLexer.interp

# Limpieza completa
distclean: clean
	rm -rf __pycache__

ANTLR_CMD=antlr4 -Dlanguage=Python3 -no-listener -visitor scheme.g4
GENERATED_FILES=schemeLexer.py schemeParser.py schemeVisitor.py schemeListener.py scheme.tokens scheme.interp schemeLexer.interp schemeLexer.tokens

all: generate

generate:
	$(ANTLR_CMD)

clean:
	rm -f $(GENERATED_FILES)
	rm -rf .antlr

.PHONY: all generate clean
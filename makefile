ANTLR_CMD=antlr4 -Dlanguage=Python3 -no-listener -visitor scheme.g4
GENERATED_FILES=schemeLexer.py schemeParser.py schemeVisitor.py schemeListener.py scheme.tokens scheme.interp schemeLexer.interp schemeLexer.tokens
PYTHON_CMD=python3
SCRIPT=scheme.py

all: generate

generate:
	$(ANTLR_CMD)

clean:
	rm -f $(GENERATED_FILES)
	rm -rf .antlr

run:
	@if [ -z "$(file)" ]; then \
		echo "Usage: make run file=<input_file>"; \
	else \
		$(PYTHON_CMD) $(SCRIPT) $(file); \
	fi

.PHONY: all generate clean run

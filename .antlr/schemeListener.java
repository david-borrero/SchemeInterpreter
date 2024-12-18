// Generated from d:/FEINA/Universitat/LP/python/SchemeInterpreter/scheme.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link schemeParser}.
 */
public interface schemeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link schemeParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(schemeParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link schemeParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(schemeParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by the {@code op}
	 * labeled alternative in {@link schemeParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOp(schemeParser.OpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code op}
	 * labeled alternative in {@link schemeParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOp(schemeParser.OpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code numero}
	 * labeled alternative in {@link schemeParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNumero(schemeParser.NumeroContext ctx);
	/**
	 * Exit a parse tree produced by the {@code numero}
	 * labeled alternative in {@link schemeParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNumero(schemeParser.NumeroContext ctx);
	/**
	 * Enter a parse tree produced by the {@code identificador}
	 * labeled alternative in {@link schemeParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIdentificador(schemeParser.IdentificadorContext ctx);
	/**
	 * Exit a parse tree produced by the {@code identificador}
	 * labeled alternative in {@link schemeParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIdentificador(schemeParser.IdentificadorContext ctx);
	/**
	 * Enter a parse tree produced by the {@code llamada}
	 * labeled alternative in {@link schemeParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLlamada(schemeParser.LlamadaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code llamada}
	 * labeled alternative in {@link schemeParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLlamada(schemeParser.LlamadaContext ctx);
}
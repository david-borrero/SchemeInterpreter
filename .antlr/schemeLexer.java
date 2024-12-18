// Generated from d:/FEINA/Universitat/LP/python/SchemeInterpreter/scheme.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class schemeLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, NUM=4, OP=5, ID=6, STRING=7, WS=8;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "NUM", "OP", "ID", "STRING", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'''", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "NUM", "OP", "ID", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public schemeLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "scheme.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\bB\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0003\u0003\u0019\b\u0003\u0001\u0003\u0004\u0003"+
		"\u001c\b\u0003\u000b\u0003\f\u0003\u001d\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004(\b\u0004\u0001\u0005\u0001\u0005\u0005\u0005,\b\u0005\n\u0005\f"+
		"\u0005/\t\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005"+
		"\u00065\b\u0006\n\u0006\f\u00068\t\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0004\u0007=\b\u0007\u000b\u0007\f\u0007>\u0001\u0007\u0001\u0007"+
		"\u0000\u0000\b\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0001\u0000\u0007\u0002\u0000++--\u0001\u0000"+
		"09\u0005\u0000*+--//<<>>\u0002\u0000AZaz\u0003\u000009AZaz\u0003\u0000"+
		"\n\n\r\r\"\"\u0003\u0000\t\n\r\r  K\u0000\u0001\u0001\u0000\u0000\u0000"+
		"\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000"+
		"\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000"+
		"\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f"+
		"\u0001\u0000\u0000\u0000\u0001\u0011\u0001\u0000\u0000\u0000\u0003\u0013"+
		"\u0001\u0000\u0000\u0000\u0005\u0015\u0001\u0000\u0000\u0000\u0007\u0018"+
		"\u0001\u0000\u0000\u0000\t\'\u0001\u0000\u0000\u0000\u000b)\u0001\u0000"+
		"\u0000\u0000\r0\u0001\u0000\u0000\u0000\u000f<\u0001\u0000\u0000\u0000"+
		"\u0011\u0012\u0005\'\u0000\u0000\u0012\u0002\u0001\u0000\u0000\u0000\u0013"+
		"\u0014\u0005(\u0000\u0000\u0014\u0004\u0001\u0000\u0000\u0000\u0015\u0016"+
		"\u0005)\u0000\u0000\u0016\u0006\u0001\u0000\u0000\u0000\u0017\u0019\u0007"+
		"\u0000\u0000\u0000\u0018\u0017\u0001\u0000\u0000\u0000\u0018\u0019\u0001"+
		"\u0000\u0000\u0000\u0019\u001b\u0001\u0000\u0000\u0000\u001a\u001c\u0007"+
		"\u0001\u0000\u0000\u001b\u001a\u0001\u0000\u0000\u0000\u001c\u001d\u0001"+
		"\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001e\u0001"+
		"\u0000\u0000\u0000\u001e\b\u0001\u0000\u0000\u0000\u001f(\u0007\u0002"+
		"\u0000\u0000 !\u0005>\u0000\u0000!(\u0005=\u0000\u0000\"#\u0005<\u0000"+
		"\u0000#(\u0005=\u0000\u0000$(\u0005=\u0000\u0000%&\u0005<\u0000\u0000"+
		"&(\u0005>\u0000\u0000\'\u001f\u0001\u0000\u0000\u0000\' \u0001\u0000\u0000"+
		"\u0000\'\"\u0001\u0000\u0000\u0000\'$\u0001\u0000\u0000\u0000\'%\u0001"+
		"\u0000\u0000\u0000(\n\u0001\u0000\u0000\u0000)-\u0007\u0003\u0000\u0000"+
		"*,\u0007\u0004\u0000\u0000+*\u0001\u0000\u0000\u0000,/\u0001\u0000\u0000"+
		"\u0000-+\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000.\f\u0001\u0000"+
		"\u0000\u0000/-\u0001\u0000\u0000\u000006\u0005\"\u0000\u000015\b\u0005"+
		"\u0000\u000023\u0005\"\u0000\u000035\u0005\"\u0000\u000041\u0001\u0000"+
		"\u0000\u000042\u0001\u0000\u0000\u000058\u0001\u0000\u0000\u000064\u0001"+
		"\u0000\u0000\u000067\u0001\u0000\u0000\u000079\u0001\u0000\u0000\u0000"+
		"86\u0001\u0000\u0000\u00009:\u0005\"\u0000\u0000:\u000e\u0001\u0000\u0000"+
		"\u0000;=\u0007\u0006\u0000\u0000<;\u0001\u0000\u0000\u0000=>\u0001\u0000"+
		"\u0000\u0000><\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?@\u0001"+
		"\u0000\u0000\u0000@A\u0006\u0007\u0000\u0000A\u0010\u0001\u0000\u0000"+
		"\u0000\b\u0000\u0018\u001d\'-46>\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}

import java.util.LinkedList;

public class Parser {

	public Parser() {
	}

	public Token parse(LinkedList<GameToken> gametokens) {

		Token ret = new Token("continue", TokenType.OVERRIDE);
		// some parsing
		return ret;
	}

}

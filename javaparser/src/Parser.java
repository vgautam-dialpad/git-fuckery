
import java.util.LinkedList;

public class Parser {

	public Parser() {
	}

	public OverrideToken parseOverrides(LinkedList<Token> gametokens) {

		// some parsing

		while (!gametokens.isEmpty()) {
			Token curr = gametokens.pop();
			if ((curr.getTokenType()).equals("OVERRIDE")) {
				return (OverrideToken) curr;
			}
		}

		return null;
	}

}

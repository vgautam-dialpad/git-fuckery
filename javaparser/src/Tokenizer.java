
import java.util.LinkedList;

public class Tokenizer {

	private String[] tokens;
	private LinkedList<GameToken> gametokens = new LinkedList<>();

	public Tokenizer() {
	}

	public LinkedList<GameToken> tokenize(String line) {

		String[] tokens = line.split("\\s+");

		for (int i = 0; i < tokens.length; i++) {
			System.out.println(tokens[i]);
		}

		return gametokens;
	}

}

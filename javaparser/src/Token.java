
public class Token {

	private String value;
	private TokenType type;

	public Token(String s, TokenType type) {
		this.value = s;
		this.type = type;
	}

	public String getValue() {
		return value;
	}

	public TokenType getTokenType() {
		return type;
	}

}

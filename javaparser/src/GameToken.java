
public class GameToken extends Token {

  public final GameTokenType type;

	String value;

	public GameToken(String s, GameTokenType type) {
    super(s, TokenType.GAMEPLAY);
		this.type = type;
	}

}

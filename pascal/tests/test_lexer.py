import pytest
from interpreter.Lexer import Lexer
from interpreter._token import TokenType


@pytest.fixture(scope="function")
def lexer():
    return Lexer()


class TestLexer:

    def test_add(self, lexer):
        lexer.init("+")
        token = lexer.next()
        assert token.type_ == TokenType.OPERATOR
        assert token.value == "+"

    def test_minus(self, lexer):
        lexer.init("-")
        token = lexer.next()
        assert token.type_ == TokenType.OPERATOR
        assert token.value == "-"

    def test_numbers(self, lexer):
        lexer.init("123")
        token = lexer.next()
        assert token.type_ == TokenType.NUMBER
        assert token.value == "123"

        lexer.init("123.45")
        token = lexer.next()
        assert token.type_ == TokenType.NUMBER
        assert token.value == "123.45"

    def test_var(self, lexer):
        lexer.init("variableName")
        token = lexer.next()
        assert token.type_ == TokenType.VAR
        assert token.value == "variablename"

    def test_begin(self, lexer):
        lexer.init("BEGIN")
        token = lexer.next()
        assert token.type_ == TokenType.BEGIN
        assert token.value == "BEGIN"

    def test_end(self, lexer):
        lexer.init("END")
        token = lexer.next()
        assert token.type_ == TokenType.END
        assert token.value == "END"

    def test_assignment(self, lexer):
        lexer.init(":=")
        token = lexer.next()
        assert token.type_ == TokenType.ASSIGNMENT
        assert token.value == ":="

    def test_semicolon(self, lexer):
        lexer.init(";")
        token = lexer.next()
        assert token.type_ == TokenType.SEMICOLON
        assert token.value == ";"

    def test_dot(self, lexer):
        lexer.init(".")
        token = lexer.next()
        assert token.type_ == TokenType.DOT
        assert token.value == "."

    def test_parents(self, lexer):
        lexer.init("(")
        token = lexer.next()
        assert token.type_ == TokenType.LPARENT
        assert token.value == "("

        lexer.init(")")
        token = lexer.next()
        assert token.type_ == TokenType.RPARENT
        assert token.value == ")"

    def test_skip(self, lexer):
        lexer.init("  123  ;  ")
        token = lexer.next()
        assert token.type_ == TokenType.NUMBER
        assert token.value == "123"
        token = lexer.next()
        assert token.type_ == TokenType.SEMICOLON
        assert token.value == ";"

    def test_bad_tokens(self, lexer):
        lexer.init(":")
        with pytest.raises(Exception):
            lexer.next()
        lexer.init("#")
        with pytest.raises(Exception):
            lexer.next()

    def test_str_token(self, lexer):
        lexer.init("+")
        token = lexer.next()
        assert str(token) == f"Token(TokenType.OPERATOR, +)"

    def test_empty_input(self, lexer):
        with pytest.raises(Exception, match="Syntax Error! Empty input!"):
            lexer.init("")

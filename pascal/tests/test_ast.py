import pytest
from interpreter.__ast import Number, BinOp, UnaryOp, Assignment, Var, Block
from interpreter._token import Token, TokenType


class TestAST:

    def test_number(self):
        token = Token(TokenType.NUMBER, "42")
        node = Number(token)
        assert str(node) == str("Number(Token(TokenType.NUMBER, 42))")

    def test_binop(self):
        left = Number(Token(TokenType.NUMBER, "2"))
        op = Token(TokenType.OPERATOR, "+")
        right = Number(Token(TokenType.NUMBER, "3"))
        node = BinOp(left, op, right)
        assert str(node) == str("BinOp+(Number(Token(TokenType.NUMBER, 2)), Number(Token(TokenType.NUMBER, 3)))")

    def test_unaryop(self):
        op = Token(TokenType.OPERATOR, "-")
        expr = Number(Token(TokenType.NUMBER, "5"))
        node = UnaryOp(op, expr)
        assert str(node) == str("UnaryOp-(Number(Token(TokenType.NUMBER, 5)))")

    def test_assignment(self):
        variable = Var(Token(TokenType.VAR, "x"))
        value = Number(Token(TokenType.NUMBER, "10"))
        token = TokenType.ASSIGNMENT
        node = Assignment(variable, token, value)
        assert str(node) == str("Assignment :=(Var(x), Number(Token(TokenType.NUMBER, 10)))")

    def test_var(self):
        token = Token(TokenType.VAR, "y")
        node = Var(token)
        assert str(node) == str("Var(y)")

    def test_block(self):
        token = TokenType.ASSIGNMENT
        statements = [
            Assignment(Var(Token(TokenType.VAR, "x")), token, Number(Token(TokenType.NUMBER, "1"))),
            Assignment(Var(Token(TokenType.VAR, "y")), token, Number(Token(TokenType.NUMBER, "2")))
        ]
        node = Block(statements)
        assert str(node) == str("Block(Assignment :=(Var(x), Number(Token(TokenType.NUMBER, 1)))Assignment :=(Var(y), Number(Token(TokenType.NUMBER, 2))))")

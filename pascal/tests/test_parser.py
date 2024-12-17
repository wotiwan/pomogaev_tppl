import pytest
from interpreter.parser import Parser
from interpreter.__ast import BinOp, Number, UnaryOp, Assignment, Var, Block


@pytest.fixture
def parser():
    return Parser()


def test_binop(parser):
    result = parser.eval("BEGIN x:= 2; x + 3; END.")
    assert isinstance(result.expressions[0], Assignment)
    assert result.expressions[0].var.token.value == "x"
    assert isinstance(result.expressions[1], BinOp)
    assert result.expressions[1].right.token.value == "3"
    assert result.expressions[1].op.value == "+"


def test_assignment(parser):
    result = parser.eval("BEGIN x := 10; END.")
    assert isinstance(result.expressions[0], Assignment)
    assert result.expressions[0].var.token.value == "x"
    assert isinstance(result.expressions[0].exp, Number)
    assert result.expressions[0].exp.token.value == "10"


def test_recursive_blocks(parser):
    result = parser.eval("BEGIN BEGIN END; END.")
    assert isinstance(result, Block)
    assert len(result.expressions) == 1
    assert isinstance(result.expressions[0], Block)


def test_invalid_syntax(parser):
    with pytest.raises(Exception, match="Syntax Error, expected: ."):
        parser.eval("BEGIN x := 10; END")
    with pytest.raises(Exception, match="Syntax Error! Expected: ; Got: TokenType.END"):
        parser.eval("BEGIN x := 10 END.")
    with pytest.raises(Exception, match="Invalid Token order. Expected: END"):
        parser.eval("BEGIN x := 10;")
    with pytest.raises(SyntaxError, match="Invalid factor"):
        parser.eval("BEGIN x + * 10; END.")
    with pytest.raises(Exception, match="Invalid Syntax!"):
        parser.eval("BEGIN a:= b:= 5; END.")
    with pytest.raises(Exception, match="Syntax Error, expected: ; got: TokenType.END"):
        parser.eval("BEGIN BEGIN 5; END END.")
    with pytest.raises(Exception, match="Invalid token order. Expected: BEGIN, got TokenType.VAR"):
        parser.eval("a:= 5 + 5;")


def test_correct_program_end(parser):
    result = parser.eval("BEGIN x := 10; END.")
    assert isinstance(result, Block)

import pytest
from interpreter.interpreter import Interpreter


class TestInterpreter:

    @pytest.fixture
    def inter(self):
        return Interpreter()

    def test_assignments(self, inter):
        assert inter.eval('''
            BEGIN
                x := 2 + 3 * (2 + 3);
                y := 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1));
            END.
        ''') == {'x': 17.0, 'y': 11.0}
        assert inter.eval('''
                    BEGIN
                        a := 10;
                        b := a + 5;
                        c := b * 2;
                    END.
                ''') == {'a': 10.0, 'b': 15.0, 'c': 30.0}

    def test_maths(self, inter):
        assert inter.eval("""
            BEGIN
                a:=(6.4 * (-78+44)) / (37 - 34.5) + 18 - 38 * 38;
            END.
        """) == {'a': -1513.04}

    def test_bad_syntax(self, inter):
        with pytest.raises(Exception, match="Bad Token"):
            inter.eval("""
            BEGIN
                y: = 2;
                BEGIN
                    a := 3;
                    a := a;
                    b := 10 + a + 10 * y / 4;
                    c := a - b
                END;
                x := 11;
            END.
            """)
        with pytest.raises(Exception, match="Bad Token"):
            inter.eval("BEGIN 3 % 2; END.")  # % не поддерживается

    def test_unary_op(self, inter):
        assert inter.eval('''
            BEGIN
                x := -5;
                y := +3;
            END.
        ''') == {'x': -5.0, 'y': 3.0}

    def test_variable_use_before_assignment(self, inter):
        with pytest.raises(Exception, match="Variable x is undefined"):
            inter.eval("BEGIN x + 5; END.")


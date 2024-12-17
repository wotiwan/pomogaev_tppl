from interpreter.parser import Parser
from interpreter.interpreter import Interpreter
from interpreter.Lexer import Lexer
inter = Interpreter()
parser = Parser()
lexer = Lexer()

print(inter.eval("""
BEGIN
    var_1 := 5+5;
    var_2 := 12-7;
END.
"""))

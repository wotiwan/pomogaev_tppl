from interpreter.parser import Parser
from interpreter.interpreter import Interpreter
from interpreter.Lexer import Lexer
inter = Interpreter()
parser = Parser()
lexer = Lexer()
# print(lexer.init("""BEGIN
#     y := 2;
#     BEGIN
#         a := 2 / 2 * 2;
#     END;
#     x := 11;
# END."""))
# token = lexer.next()
# while token.type_:
#     print(token)
#     token = lexer.next()

# print(inter.eval("BEGIN 2++_+2 END."))
#
# print(parser.eval("BEGIN BEGIN a:=5-1 * (2 + 4); END; BEGIN END; END."))
# print(inter.eval("BEGIN BEGIN a:= 5-1 * (2 + 4); END; BEGIN END; END."))

print(inter.eval("""
BEGIN
    ABOBA := 5+5;
    aboba := 12-7;
END.
"""))

#  a:=(6.4 * (-78+44)) / (37 - 34.5) + 18 - 38 * 38;
#  a:= 5-1 * (2 + 4);

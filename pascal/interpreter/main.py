from parser import Parser
from interpreter import Interpreter
from Lexer import Lexer
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

print(parser.eval("BEGIN BEGIN a:=5-1 * (2 + 4); END; BEGIN END; END."))
print(inter.eval("BEGIN BEGIN a:= 5-1 * (2 + 4); END; BEGIN END; END."))

print(inter.eval("""
BEGIN
    y := 2;
    BEGIN
        a := 3;
        a := a;
        b := 10 + a + 10 * y / 4;
        c := a - b;
    END;
    x := 11;
END.
"""))

#  a:=(6.4 * (-78+44)) / (37 - 34.5) + 18 - 38 * 38;
#  a:= 5-1 * (2 + 4);

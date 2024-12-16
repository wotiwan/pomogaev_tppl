from _token import Token, TokenType


class Lexer():

    def __init__(self):
        self._pos = 0
        self._text = ""
        self._current_char = None

    def __forward(self):
        self._pos += 1
        if self._pos > len(self._text) - 1:
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def __skip(self):
        while (self._current_char is not None and
               self._current_char.isspace()):
            self.__forward()

    def __number(self):
        result = ""
        while (self._current_char is not None and
               self._current_char.isdigit()):
            result += self._current_char
            self.__forward()
            if self._current_char == '.':
                result += self._current_char
                self.__forward()
        return result

    # todo: name1 or name_1 won`t be recognized
    def __word(self):
        result = ""
        while (self._current_char is not None and
               self._current_char.isalpha()):
            result += self._current_char
            self.__forward()
        return result

    def init(self, s: str):
        self._pos = 0
        self._text = s
        self._current_char = self._text[self._pos]

    def next(self) -> Token:
        while self._current_char:
            if self._current_char.isspace():
                self.__skip()
                continue
            if self._current_char.isdigit():
                return Token(TokenType.NUMBER, self.__number())
            if self._current_char.isalpha():
                word = self.__word()
                if word == "BEGIN":
                    val = word
                    return Token(TokenType.BEGIN, val)
                elif word == "END":
                    val = word
                    return Token(TokenType.END, val)
                else:
                    return Token(TokenType.VAR, word)
            if self._current_char in ['+', '-', '*', '/']:
                op = self._current_char
                self.__forward()
                return Token(TokenType.OPERATOR, op)
            if self._current_char == "(":
                val = self._current_char
                self.__forward()
                return Token(TokenType.LPARENT, val)
            if self._current_char == ")":
                val = self._current_char
                self.__forward()
                return Token(TokenType.RPARENT, val)
            if self._current_char == ":":
                val = self._current_char
                self.__forward()
                if self._current_char == "=":
                    val += self._current_char
                    self.__forward()
                    return Token(TokenType.ASSIGNMENT, val)
            if self._current_char == ";":
                val = self._current_char
                self.__forward()
                return Token(TokenType.SEMICOLON, val)
            if self._current_char == ".":
                val = self._current_char
                self.__forward()
                return Token(TokenType.DOT, val)
            else:
                raise SyntaxError("Bad Token")

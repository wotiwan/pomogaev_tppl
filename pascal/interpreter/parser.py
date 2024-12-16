from _token import TokenType
from Lexer import Lexer
from __ast import Number, BinOp, UnaryOp, Block, Assignment, Var


class Parser():

    def __init__(self):
        self._lexer = Lexer()
        self._current_token = None
        self.scope_counter = 0

    def __check_token(self, type_: TokenType) -> None:
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise SyntaxError("Invalid token order")

    def __factor(self):
        token = self._current_token
        if token.value == "+":
            self.__check_token(TokenType.OPERATOR)
            return UnaryOp(token, self.__factor())
        if token.value == "-":
            self.__check_token(TokenType.OPERATOR)
            return UnaryOp(token, self.__factor())

        if token.type_ == TokenType.NUMBER:
            self.__check_token(TokenType.NUMBER)
            return Number(token)
        if token.type_ == TokenType.LPARENT:
            self.__check_token(TokenType.LPARENT)
            result = self.__expr()
            self.__check_token(TokenType.RPARENT)
            return result
        if token.type_ == TokenType.BEGIN:
            self.__check_token(TokenType.BEGIN)
            return self.__block()
        if token.type_ == TokenType.VAR:
            self.__check_token(TokenType.VAR)
            return Var(token)
        raise SyntaxError("Invalid factor")

    def __term(self):
        result = self.__factor()
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            if self._current_token.value not in ['*', '/']:
                break
            token = self._current_token
            self.__check_token(TokenType.OPERATOR)
            return BinOp(result, token, self.__term())
        return result

    def __expr(self) -> BinOp:
        result = self.__term()
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            token = self._current_token
            self.__check_token(TokenType.OPERATOR)
            result = BinOp(result, token, self.__term())
        return result

    def __assignment(self) -> Assignment:
        result = self.__expr()
        while self._current_token and (self._current_token.type_ == TokenType.ASSIGNMENT):
            var_name = result
            self.__check_token(TokenType.ASSIGNMENT)
            var_value = self.__expr()
            if isinstance(var_name, Assignment):  # for recursive assignments at one
                raise Exception("Invalid Syntax!")
            result = Assignment(var_name, TokenType.ASSIGNMENT, var_value)
        return result

    def __block(self) -> Block:
        self.scope_counter += 1
        expressions = []
        while self._current_token and (self._current_token.type_ != TokenType.END):
            result = self.__assignment()
            if self._current_token and (self._current_token.type_ != TokenType.SEMICOLON):
                raise Exception(f"Syntax Error! Expected: ; Got: {self._current_token.type_}")
            else:
                self.__check_token(TokenType.SEMICOLON)
            expressions.append(result)  # BEGIN BEGIN b; END; END.
        if self._current_token and (self._current_token.type_ == TokenType.END):
            self.__check_token(TokenType.END)
            if self.scope_counter == 1:
                if self._current_token and (self._current_token.type_ == TokenType.DOT):
                    self.__check_token(TokenType.DOT)
                    self.scope_counter -= 1
                    return Block(expressions)
                else:
                    raise Exception(f"Syntax Error, expected: .")
            elif self.scope_counter > 1:
                if self._current_token and (self._current_token.type_ == TokenType.SEMICOLON):
                    # self.__check_token(TokenType.SEMICOLON)
                    self.scope_counter -= 1
                    return Block(expressions)
                else:
                    raise Exception(f"Syntax Error, expected: ; got: {self._current_token.type_}")
        else:
            raise Exception(f"Invalid Token order. Expected: END")

    def __syntax_checker(self) -> Block:
        if self._current_token.type_ == TokenType.BEGIN:
            self.__check_token(TokenType.BEGIN)
            return self.__block()
        else:
            raise Exception(f"Invalid token order. Expected: BEGIN, got {self._current_token.type_}")

    def eval(self, s: str) -> Block:
        self._lexer.init(s)
        self._current_token = self._lexer.next()
        return self.__syntax_checker()

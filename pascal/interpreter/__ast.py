from _token import Token, TokenType


class Node:
    pass


class Number(Node):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        # return f"{self.__class__.__name__} ({self.token})"
        return f"{self.__class__.__name__} ({self.token.value})"


class BinOp(Node):
    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"{self.__class__.__name__} {self.op.value}({self.left}, {self.right})"


class UnaryOp(Node):
    def __init__(self, op: Token, exp: Node):
        self.op = op
        self.expr = exp

    def __str__(self):
        return f"{self.__class__.__name__}{self.op.value}({self.expr})"


class Block(Node):
    def __init__(self, exp: list):
        self.expressions = exp

    def __str__(self):
        return f"{self.__class__.__name__}({''.join(str(i) for i in self.expressions)})" # {''.join(str(i) for i in self.expressions)} {self.expressions}


class Var(Node):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"{self.__class__.__name__}({self.token.value})"


class Assignment(Node):
    def __init__(self, var: Node, op: TokenType, exp: Node):
        self.var = var
        self.op = op
        self.exp = exp

    def __str__(self):
        return f"{self.__class__.__name__} :=({self.var}, {self.exp})"



from enum import Enum, auto


class TokenType(Enum):
    NUMBER = auto()
    OPERATOR = auto()
    LPARENT = auto()
    RPARENT = auto()
    EOL = auto()

    BEGIN = auto()
    END = auto()
    ASSIGNMENT = auto()
    VAR = auto()
    SEMICOLON = auto()
    DOT = auto()


class Token:

    def __init__(self, type_: TokenType, value: str):
        self.type_ = type_
        self.value = value

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.type_}, {self.value})"

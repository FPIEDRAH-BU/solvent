import typing


variable = typing.Union["Integer", "Boolean"]


class Range:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args



class Integer:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Boolean:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


arithmetic = typing.Union[
    "Addition", "Subtraction", "Multiplication", "Division", "Minimum", "Maximum"
]


class Addition:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Subtraction:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Multiplication:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Division:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Minimum:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Maximum:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


relational = typing.Union[
    "Inferior",
    "Superior",
    "Equal",
    "Different",
]


class Inferior:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Superior:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Equal:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Different:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


logic = typing.Union[
    "Equivalence",
    "Implication",
    "Negation",
    "And",
    "Or",
    "Xor",
]


class Equivalence:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Implication:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Negation:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class And:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Or:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args


class Xor:
    def __init__(self, *args: list[typing.Any]) -> None:
        self.parameters = args

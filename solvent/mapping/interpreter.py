import typing

from solvent import modeling, graph


def build_parameters(
    parameters: list[typing.Any], component: graph.component
) -> list[typing.Any]:
    data = []

    for parameter in parameters:
        if isinstance(parameter, int) or isinstance(parameter, bool):
            data.append(parameter)
        else:
            aux = parameter.to_model(component)

            if isinstance(aux, list):
                data.extend(aux)
            else:
                data.append(aux)

    return data


class Logic:
    def __init__(
        self, type: str, parameters: list[typing.Any], parent: typing.Any = None
    ) -> None:
        self.type = type
        self.parameters = parameters
        self.parent = parent

    def to_model(self, component: graph.component) -> modeling.logic:
        parameters = build_parameters(self.parameters, component)

        match self.type:
            case "Equivalence":
                return modeling.Equivalence(*parameters)
            case "Implication":
                return modeling.Implication(*parameters)
            case "Negation":
                return modeling.Negation(*parameters)
            case "And":
                return modeling.And(*parameters)
            case "Or":
                return modeling.Or(*parameters)
            case "Xor":
                return modeling.Xor(*parameters)
            case _:
                raise ValueError()


class Relational:
    def __init__(
        self, type: str, parameters: list[typing.Any], parent: typing.Any = None
    ) -> None:
        self.type = type
        self.parameters = parameters
        self.parent = parent

    def to_model(self, component: graph.component) -> modeling.relational:
        parameters = build_parameters(self.parameters, component)

        match self.type:
            case "Inferior":
                return modeling.Inferior(*parameters)
            case "Superior":
                return modeling.Superior(*parameters)
            case "Equal":
                return modeling.Equal(*parameters)
            case "Different":
                return modeling.Different(*parameters)
            case _:
                raise ValueError


class Arithmetic:
    def __init__(
        self, type: str, parameters: list[typing.Any], parent: typing.Any = None
    ) -> None:
        self.type = type
        self.parameters = parameters
        self.parent = parent

    def to_model(self, component: graph.component) -> modeling.arithmetic:
        parameters = build_parameters(self.parameters, component)

        match self.type:
            case "Addition":
                return modeling.Addition(*parameters)
            case "Subtraction":
                return modeling.Subtraction(*parameters)
            case "Multiplication":
                return modeling.Multiplication(*parameters)
            case "Division":
                return modeling.Division(*parameters)
            case "Minimum":
                return modeling.Minimum(*parameters)
            case "Maximum":
                return modeling.Maximum(*parameters)
            case _:
                raise ValueError


class Variable:
    def __init__(self, type: str, parameters: list[typing.Any]) -> None:
        self.type = type
        self.parameters = parameters
        self.parent = None

    def to_model(self, component: graph.component) -> modeling.variable:
        parameters = build_parameters(self.parameters, component)

        match self.type:
            case "Integer":
                return modeling.Integer(*parameters)
            case "Boolean":
                return modeling.Boolean(*parameters)
            case _:
                raise ValueError()


class Range:
    def __init__(self, minimum: int, maximum: int, parent: typing.Any) -> None:
        self.minimum = minimum
        self.maximum = maximum
        self.parent = parent

    def to_model(self, component: graph.component) -> modeling.Range:
        return modeling.Range(*[self.minimum, self.maximum])


class Value:
    def __init__(self, type: str, values: list[str], parent: typing.Any) -> None:
        self.type = type
        self.values = values
        self.parent = parent

    def to_model(self, component: graph.component) -> typing.Any:
        if self.type == "Node" and not isinstance(component, graph.Node):
            raise TypeError()

        if self.type == "Connection" and not isinstance(component, graph.Connection):
            raise TypeError()

        data = component

        for value in self.values:
            match data:
                case graph.Node() | graph.Connection():
                    data = data.parameters.get(value)
                case dict():
                    data = data.get(value)
                case list():
                    aux = []
                    for item in data:
                        if type(item) in (graph.Node, graph.Connection):
                            aux.append(item.parameters.get(value))
                        elif isinstance(item, dict):
                            aux.append(item.get(value))
                    data = data
                case None:
                    raise ValueError

        return data

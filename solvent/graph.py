import typing
import uuid


component = typing.Union["Node", "Connection"]


class Node:
    def __init__(self, **kwargs: dict[str, typing.Any]) -> None:
        self.validate_id(kwargs)

        self.parameters = kwargs

    def validate_id(self, parameters: dict[str, typing.Any]) -> None:
        if "id" not in parameters:
            raise ValueError()


class Connection:
    def __init__(self, **kwargs: dict[str, typing.Any]) -> None:
        self.validate_id(kwargs)
        self.validate_source(kwargs)
        self.validate_destinations(kwargs)

        self.parameters = kwargs
        self.parameters["destination"] = self.parameters["destinations"][0]  # type: ignore

    def validate_id(self, parameters: dict[str, typing.Any]) -> None:
        if "id" not in parameters:
            raise ValueError()

        if not isinstance(parameters["id"], uuid.UUID):
            raise ValueError()

    def validate_source(self, parameters: dict[str, typing.Any]) -> None:
        if "source" not in parameters:
            raise ValueError()

        if not isinstance(parameters["source"], Node):
            raise ValueError()

    def validate_destinations(self, parameters: dict[str, typing.Any]) -> None:
        if "destinations" not in parameters:
            raise ValueError()

        if not isinstance(parameters["destinations"], list):
            raise ValueError()

        for index, destination in enumerate(parameters["destinations"]):
            if not isinstance(destination, Node):
                raise ValueError()


class MGraph:
    def __init__(self, nodes: list[Node], connections: list[Connection]) -> None:
        self.nodes = nodes
        self.connections = connections

        self._node_table = {node.id: node for node in self.nodes}
        self._connection_table = {connection.id for connection in self.connections}

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)
        self._node_table[node.id] = node

    def add_connection(self, connection: Connection) -> None:
        self.connections.append(connection)
        self._connection_table[connection.id] = connection

    def get_node(self, id: uuid.UUID) -> typing.Optional[Node]:
        return self._node_table.get(id)

    def get_connection(self, id: uuid.UUID) -> typing.Optional[Connection]:
        return self._connection_table.get(id)

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

    def __getattr__(self, name: str) -> typing.Any:
        return self.parameters[name]


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

    def __getattr__(self, name: str) -> typing.Any:
        return self.parameters[name]


class MGraph:
    def __init__(
        self, nodes: list[Node] = None, connections: list[Connection] = None
    ) -> None:
        self.nodes = nodes if nodes else []
        self.connections = connections if connections else []

        self._node_table = {node.id: node for node in self.nodes}
        self._connection_table = {
            connection.id: connection for connection in self.connections
        }

        self._sources_table = {}
        self._destinations_table = {}

        for connection in self.connections:
            self.add_connection(connection)

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)
        self._node_table[node.id] = node

    def add_connection(self, connection: Connection) -> None:
        if connection.id not in self.connections:
            self.connections.append(connection)

        self._connection_table[connection.id] = connection

        if connection.source.id not in self._sources_table:
            self._sources_table[connection.source.id] = []

        self._sources_table[connection.source.id].append(connection)

        for destination in connection.destinations:
            if destination.id not in self._destinations_table:
                self._destinations_table[destination.id] = []

            self._destinations_table[destination.id].append(connection)

    def get_node(self, id: uuid.UUID) -> typing.Optional[Node]:
        return self._node_table.get(id)

    def get_connection(self, id: uuid.UUID) -> typing.Optional[Connection]:
        return self._connection_table.get(id)

    def get_connections_from_source(
        self, id: uuid.UUID
    ) -> typing.Optional[list[Connection]]:
        return self._sources_table.get(id)

    def get_connections_from_destination(
        self, id: uuid.UUID
    ) -> typing.Optional[list[Connection]]:
        return self._destinations_table.get(id)

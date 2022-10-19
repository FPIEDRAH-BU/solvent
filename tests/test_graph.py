import pytest
import uuid

from textx import metamodel_from_file
from solvent.mapping import interpreter
from solvent import graph


@pytest.fixture
def feature_model():
    feature_model = graph.MGraph(
        nodes=[
            graph.Node(
                id=uuid.UUID("897411a9-f316-4f19-a321-10d111dcad58"),
                name="Mobile Phone",
            ),
            graph.Node(
                id=uuid.UUID("e256c537-888e-478f-81bc-920784e39c1f"), name="Calls"
            ),
            graph.Node(
                id=uuid.UUID("cbb3cbb5-69bd-4077-b341-e8b02c67581e"), name="GPS"
            ),
            graph.Node(
                id=uuid.UUID("336805d1-6015-4a93-a04a-f1a3dbf18388"), name="Screen"
            ),
            graph.Node(
                id=uuid.UUID("54d38b28-965a-4251-8711-ac8515303288"), name="Basic"
            ),
            graph.Node(
                id=uuid.UUID("04478096-bae7-4e7f-9c4f-7c08d7eb60af"), name="Color"
            ),
            graph.Node(
                id=uuid.UUID("3ce3e99c-785b-407f-ba8b-a5204f92763b"),
                name="High Resolution",
            ),
            graph.Node(
                id=uuid.UUID("be978953-28f5-4c57-bc46-ecbe156f5316"), name="Media"
            ),
            graph.Node(
                id=uuid.UUID("1f40d88b-96c3-46f8-9644-405f1c37a607"), name="Camera"
            ),
            graph.Node(
                id=uuid.UUID("315c6e46-ec73-46f1-b5d7-bb8fa2f7dbbb"), name="MP3"
            ),
        ]
    )

    feature_model.add_connection(
        graph.Connection(
            type="mandatory",
            id=uuid.UUID("cc5ab3a1-ba2a-41ef-a2ac-d9d0df97f736"),
            source=feature_model.get_node(
                uuid.UUID("e256c537-888e-478f-81bc-920784e39c1f")
            ),
            destinations=[
                feature_model.get_node(
                    uuid.UUID("e256c537-888e-478f-81bc-920784e39c1f")
                )
            ],
        )
    )

    feature_model.add_connection(
        graph.Connection(
            type="optional",
            id=uuid.UUID("50f87a4f-2cfc-4c91-bc80-b0898e98df72"),
            source=feature_model.get_node(
                uuid.UUID("897411a9-f316-4f19-a321-10d111dcad58")
            ),
            destinations=[
                feature_model.get_node(
                    uuid.UUID("cbb3cbb5-69bd-4077-b341-e8b02c67581e")
                )
            ],
        )
    )

    feature_model.add_connection(
        graph.Connection(
            type="mandatory",
            id=uuid.UUID("4683d73d-619b-4f40-802a-6891b0873ad3"),
            source=feature_model.get_node(
                uuid.UUID("897411a9-f316-4f19-a321-10d111dcad58")
            ),
            destinations=[
                feature_model.get_node(
                    uuid.UUID("336805d1-6015-4a93-a04a-f1a3dbf18388")
                )
            ],
        )
    )

    feature_model.add_connection(
        graph.Connection(
            type="optional",
            id=uuid.UUID("dc351128-6332-4d15-8386-181513b6dd25"),
            source=feature_model.get_node(
                uuid.UUID("897411a9-f316-4f19-a321-10d111dcad58")
            ),
            destinations=[
                feature_model.get_node(
                    uuid.UUID("be978953-28f5-4c57-bc46-ecbe156f5316")
                )
            ],
        )
    )

    feature_model.add_connection(
        graph.Connection(
            type="range",
            minimum=1,
            maximum=1,
            id=uuid.UUID("c68d3670-c761-4877-9b74-2c462dab1b2d"),
            source=feature_model.get_node(
                uuid.UUID("336805d1-6015-4a93-a04a-f1a3dbf18388")
            ),
            destinations=[
                feature_model.get_node(
                    uuid.UUID("336805d1-6015-4a93-a04a-f1a3dbf18388")
                ),
                feature_model.get_node(
                    uuid.UUID("54d38b28-965a-4251-8711-ac8515303288")
                ),
                feature_model.get_node(
                    uuid.UUID("04478096-bae7-4e7f-9c4f-7c08d7eb60af")
                ),
            ],
        )
    )

    feature_model.add_connection(
        graph.Connection(
            type="excludes",
            id=uuid.UUID("6cfe4e49-4d5b-43be-b239-39335afbf725"),
            source=feature_model.get_node(
                uuid.UUID("54d38b28-965a-4251-8711-ac8515303288")
            ),
            destinations=[
                feature_model.get_node(
                    uuid.UUID("cbb3cbb5-69bd-4077-b341-e8b02c67581e")
                ),
            ],
        )
    )

    feature_model.add_connection(
        graph.Connection(
            type="optional",
            id=uuid.UUID("86c92ef3-ab59-495d-97ca-befc30224e82"),
            source=feature_model.get_node(
                uuid.UUID("897411a9-f316-4f19-a321-10d111dcad58")
            ),
            destinations=[
                feature_model.get_node(
                    uuid.UUID("be978953-28f5-4c57-bc46-ecbe156f5316")
                ),
            ],
        )
    )

    feature_model.add_connection(
        graph.Connection(
            type="or",
            id=uuid.UUID("c68d3670-c761-4877-9b74-2c462dab1b2d"),
            source=feature_model.get_node(
                uuid.UUID("be978953-28f5-4c57-bc46-ecbe156f5316")
            ),
            destinations=[
                feature_model.get_node(
                    uuid.UUID("1f40d88b-96c3-46f8-9644-405f1c37a607")
                ),
                feature_model.get_node(
                    uuid.UUID("315c6e46-ec73-46f1-b5d7-bb8fa2f7dbbb")
                ),
            ],
        )
    )

    return feature_model


def test_get_node(feature_model):
    node = feature_model.get_node(uuid.UUID("04478096-bae7-4e7f-9c4f-7c08d7eb60af"))

    assert node.name == "Color"


def test_get_connection(feature_model):
    connection = feature_model.get_connection(
        uuid.UUID("6cfe4e49-4d5b-43be-b239-39335afbf725")
    )

    assert connection.type == "excludes"


def test_get_connections_from_source(feature_model):
    connections = feature_model.get_connections_from_source(
        uuid.UUID("897411a9-f316-4f19-a321-10d111dcad58")
    )

    assert len(connections) == 4


def test_get_connections_from_destination(feature_model):
    connections = feature_model.get_connections_from_destination(
        uuid.UUID("cbb3cbb5-69bd-4077-b341-e8b02c67581e")
    )

    assert len(connections) == 2

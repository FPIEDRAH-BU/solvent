import json
import pytest
import uuid

from solvent.variamos import model


@pytest.fixture
def variamos_data():
    with open("tests/assets/feature_model.json", "r") as file:
        return json.loads(file.read())


def test_model(variamos_data):
    m = model.Model(**variamos_data)

    assert m.name == "Features"
    assert isinstance(m.id, uuid.UUID)
    assert all(map(lambda element: isinstance(element, model.Element), m.elements))
    assert all(
        map(lambda relation: isinstance(relation, model.Relationship), m.relationships)
    )

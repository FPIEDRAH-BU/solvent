import pytest
import uuid

from textx import metamodel_from_file
from solvent.mapping import interpreter
from solvent import modeling, graph


@pytest.fixture
def meta_model():
    return metamodel_from_file(
        "./solvent/mapping/mapping.tx",
        classes=[
            interpreter.Logic,
            interpreter.Relational,
            interpreter.Arithmetic,
            interpreter.Variable,
            interpreter.Range,
            interpreter.Value,
        ],
    )


def test_equivalence_static_parameters(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Equivalence(true, true)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Equivalence)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_equivalence_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=False)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Equivalence(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Equivalence)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_equivalence_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Equivalence(Equivalence(true, true), Equivalence(false, true))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Equivalence)
    assert isinstance(model.parameters[0], modeling.Equivalence)
    assert isinstance(model.parameters[0].parameters[0], bool)
    assert isinstance(model.parameters[0].parameters[1], bool)
    assert isinstance(model.parameters[1], modeling.Equivalence)
    assert isinstance(model.parameters[1].parameters[0], bool)
    assert isinstance(model.parameters[1].parameters[1], bool)


def test_equivalence_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Equivalence(23, 29)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_equivalence_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Equivalence(Addition(1, 2, 3), Addition(4, 5))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_implication_static_parameters(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Implication(true, true)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Implication)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_implication_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=False)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Implication(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Implication)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_implication_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Implication(Implication(true, true), Implication(false, true))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Implication)
    assert isinstance(model.parameters[0], modeling.Implication)
    assert isinstance(model.parameters[0].parameters[0], bool)
    assert isinstance(model.parameters[0].parameters[1], bool)
    assert isinstance(model.parameters[1], modeling.Implication)
    assert isinstance(model.parameters[1].parameters[0], bool)
    assert isinstance(model.parameters[1].parameters[1], bool)


def test_implication_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Implication(23, 29)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_implication_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Implication(Addition(1, 2, 3), Addition(4, 5))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_negation_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Negation(true)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Negation)
    assert isinstance(model.parameters[0], bool)


def test_negation_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=False)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Negation(Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Negation)
    assert isinstance(model.parameters[0], bool)


def test_negation_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Negation(Negation(true))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Negation)
    assert isinstance(model.parameters[0], modeling.Negation)
    assert isinstance(model.parameters[0].parameters[0], bool)


def test_negation_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Negation(23)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_negation_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Negation(Addition(1, 2, 3))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_and_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "And(true, false)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.And)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_and_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=False)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "And(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.And)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_and_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "And(And(true))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.And)
    assert isinstance(model.parameters[0], modeling.And)
    assert isinstance(model.parameters[0].parameters[0], bool)


def test_and_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "And(23, 24)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_and_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "And(Addition(1, 2, 3), Addition(1, 2, 3))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_or_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Or(true, false)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Or)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_or_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=False)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Or(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Or)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_or_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Or(Or(true, true), Or(true, true))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Or)
    assert isinstance(model.parameters[0], modeling.Or)
    assert isinstance(model.parameters[0].parameters[0], bool)
    assert isinstance(model.parameters[0].parameters[1], bool)
    assert isinstance(model.parameters[1], modeling.Or)
    assert isinstance(model.parameters[1].parameters[0], bool)
    assert isinstance(model.parameters[1].parameters[1], bool)


def test_or_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Or(23, 21)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_or_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Or(Addition(1, 2, 3), Addition(4, 5))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_xor_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Xor(true, false)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Xor)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_xor_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=False)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Xor(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Xor)
    assert isinstance(model.parameters[0], bool)
    assert isinstance(model.parameters[1], bool)


def test_xor_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Xor(Xor(true, true), Xor(true, true))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Xor)
    assert isinstance(model.parameters[0], modeling.Xor)
    assert isinstance(model.parameters[0].parameters[0], bool)
    assert isinstance(model.parameters[0].parameters[1], bool)
    assert isinstance(model.parameters[1], modeling.Xor)
    assert isinstance(model.parameters[1].parameters[0], bool)
    assert isinstance(model.parameters[1].parameters[1], bool)


def test_xor_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Xor(23, 21)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_xor_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Xor(Addition(1, 2, 3), Addition(4, 5))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_inferior_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Inferior(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Inferior)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_inferior_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Inferior(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Inferior)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_inferior_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Inferior(Addition(1, 2), Addition(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Inferior)
    assert isinstance(model.parameters[0], modeling.Addition)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Addition)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_inferior_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Inferior(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_inferior_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Inferior(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_superior_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Superior(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Superior)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_superior_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Superior(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Superior)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_superior_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Superior(Addition(1, 2), Addition(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Superior)
    assert isinstance(model.parameters[0], modeling.Addition)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Addition)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_superior_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "superior(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_superior_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "superior(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_equal_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Equal(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Equal)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_equal_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Equal(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Equal)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_equal_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Equal(Addition(1, 2), Addition(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Equal)
    assert isinstance(model.parameters[0], modeling.Addition)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Addition)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_equal_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Equal(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_equal_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Equal(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_different_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Different(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Different)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_different_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Different(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Different)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_different_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Different(Addition(1, 2), Addition(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Different)
    assert isinstance(model.parameters[0], modeling.Addition)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Addition)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_different_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Different(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_different_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Different(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_addition_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Addition(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Addition)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_addition_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Addition(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Addition)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_addition_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Addition(Addition(1, 2), Addition(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Addition)
    assert isinstance(model.parameters[0], modeling.Addition)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Addition)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_addition_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Addition(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_addition_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Addition(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_subtraction_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Subtraction(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Subtraction)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_subtraction_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Subtraction(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Subtraction)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_subtraction_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Subtraction(Subtraction(1, 2), Subtraction(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Subtraction)
    assert isinstance(model.parameters[0], modeling.Subtraction)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Subtraction)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_subtraction_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Subtraction(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_subtraction_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Subtraction(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_multiplication_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Multiplication(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Multiplication)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_multiplication_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Multiplication(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Multiplication)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_multiplication_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Multiplication(Multiplication(1, 2), Multiplication(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Multiplication)
    assert isinstance(model.parameters[0], modeling.Multiplication)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Multiplication)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_multiplication_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Multiplication(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_multiplication_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Multiplication(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_division_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Division(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Division)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_division_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Division(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Division)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_division_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Division(Division(1, 2), Division(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Division)
    assert isinstance(model.parameters[0], modeling.Division)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Division)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_division_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Division(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_division_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Division(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_minimum_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Minimum(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Minimum)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_minimum_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Minimum(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Minimum)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_minimum_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Minimum(Minimum(1, 2), Minimum(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Minimum)
    assert isinstance(model.parameters[0], modeling.Minimum)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Minimum)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_minimum_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Minimum(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_minimum_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Minimum(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_maximum_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Maximum(1, 5)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Maximum)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_maximum_variable_parameter(meta_model):
    source = graph.Node(id=uuid.uuid4(), value=3)
    destinations = [graph.Node(id=uuid.uuid4()) for _ in range(5)]

    connection = graph.Connection(
        id=uuid.uuid4(), source=source, destinations=destinations
    )

    code = "Maximum(Connection.source.value, Connection.source.value)"
    model = meta_model.model_from_str(code).to_model(connection)

    assert isinstance(model, modeling.Maximum)
    assert isinstance(model.parameters[0], int)
    assert isinstance(model.parameters[1], int)


def test_maximum_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Maximum(Maximum(1, 2), Maximum(1, 2))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Maximum)
    assert isinstance(model.parameters[0], modeling.Maximum)
    assert isinstance(model.parameters[0].parameters[0], int)
    assert isinstance(model.parameters[0].parameters[1], int)
    assert isinstance(model.parameters[1], modeling.Maximum)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_maximum_wrong_static_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Maximum(true, true)"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_maximum_wrong_nested_parameter(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Maximum(And(true, false), And(true, true))"

    with pytest.raises(Exception):
        meta_model.model_from_str(code).to_model(node)


def test_integer_variant_one(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Integer(Node.id)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Integer)
    assert isinstance(model.parameters[0], uuid.UUID)


def test_integer_variant_two(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Integer(Node.id, Range(0, 1))"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Integer)
    assert isinstance(model.parameters[0], uuid.UUID)
    assert isinstance(model.parameters[1], modeling.Range)
    assert isinstance(model.parameters[1].parameters[0], int)
    assert isinstance(model.parameters[1].parameters[1], int)


def test_boolean(meta_model):
    node = graph.Node(id=uuid.uuid4())
    code = "Boolean(Node.id)"
    model = meta_model.model_from_str(code).to_model(node)

    assert isinstance(model, modeling.Boolean)
    assert isinstance(model.parameters[0], uuid.UUID)

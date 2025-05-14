import pytest

from your_core_library.data_handler import DataHandler
from your_core_library.data_handler import ExampleModel


def test_example_model_core():
    model = ExampleModel(name="core_test", value=456)
    assert model.name == "core_test"
    assert model.value == 456


@pytest.fixture
def handler():
    return DataHandler()


def test_initialization(handler):
    assert handler is not None, "DataHandler should initialize."


def test_simple_processing(handler):
    result = handler.process("test_data")
    assert result == "processed_atad_tset", (
        "Simple processing should reverse and prefix."
    )


def test_process_empty_data(handler):
    with pytest.raises(ValueError, match="Input data cannot be empty."):
        handler.process("")


def test_process_error_condition(handler):
    with pytest.raises(ValueError, match="Simulated processing error based on input."):
        handler.process("trigger error here")


def test_complex_processing_logic(handler):
    # This test was originally for 'another_method'. We'll implement it now.
    assert handler.another_method(0) is True, "another_method(0) should return True."
    assert handler.another_method(-5) is False, (
        "another_method with negative should be False."
    )
    assert handler.another_method(5) is False, (
        "another_method(5) should be False (not > 10)."
    )
    assert handler.another_method(15) is True, (
        "another_method(15) should be True (>10)."
    )
    assert handler.another_method(11) is True


def test_example_model_repr():
    """Tests the __repr__ method of ExampleModel."""
    model = ExampleModel(name="TestName", value=123)
    expected_repr = "ExampleModel(name='TestName', value=123)"
    assert repr(model) == expected_repr


# TODO: Add more tests for edge cases and other methods in DataHandler if necessary

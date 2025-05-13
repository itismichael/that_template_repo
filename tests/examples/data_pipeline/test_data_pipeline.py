import logging
from unittest.mock import patch

import pytest

# Adjust the import path based on your project structure
from examples import data_pipeline

# Sample data for testing
SAMPLE_RAW_DATA = [
    {"id": 1, "value": 60, "category": "A"},
    {"id": 2, "value": 30, "category": "B"},
    {"id": 3, "value": 90, "category": "A"},
    {"id": 4, "value": 50, "category": "C"},
]

MOCK_CORE_MESSAGE = "Mocked core message"


@pytest.fixture(autouse=True)
def capture_logs(caplog):
    """Automatically capture logs for all tests."""
    caplog.set_level(logging.INFO)
    return caplog


def test_extract_data():
    """Test the data extraction simulation."""
    # Since it uses random, just check the type and basic structure
    data = data_pipeline.extract_data()
    assert isinstance(data, list)
    if data:
        assert isinstance(data[0], dict)
        assert "id" in data[0]
        assert "value" in data[0]
        assert "category" in data[0]


@patch("examples.data_pipeline.get_core_greeting", return_value=MOCK_CORE_MESSAGE)
def test_transform_data(mock_get_greeting_func):
    """Test the data transformation logic."""
    transformed = data_pipeline.transform_data(SAMPLE_RAW_DATA)

    # Verify filtering (value > 50)
    assert len(transformed) == 2
    assert all(item["value"] > 50 for item in transformed)

    # Verify added fields
    for item in transformed:
        assert item["status"] == "processed"
        assert item["core_message"] == MOCK_CORE_MESSAGE
        assert "value_category" in item
        assert str(item["value"]) in item["value_category"]
        assert item["category"] in item["value_category"]

    # Ensure the mock was called
    mock_get_greeting_func.assert_called_once()


@patch("builtins.print")
def test_load_data_with_data(mock_print, caplog):
    """Test loading data when data is present."""
    data_to_load = [{"id": 1, "result": "ok"}, {"id": 2, "result": "fine"}]
    data_pipeline.load_data(data_to_load)

    # Check if print was called (at least for the header/footer)
    assert mock_print.call_count >= 2
    # Check log message
    assert f"Successfully loaded {len(data_to_load)} records." in caplog.text


@patch("builtins.print")
def test_load_data_empty(mock_print, caplog):
    """Test loading data when the list is empty."""
    data_pipeline.load_data([])

    # Print should not be called for records
    mock_print.assert_not_called()
    # Check log message
    assert "No data to load." in caplog.text


@patch("examples.data_pipeline.extract_data", return_value=SAMPLE_RAW_DATA)
@patch(
    "examples.data_pipeline.transform_data", return_value=[{"id": 1, "value": 60}]
)  # Simplified return
@patch("examples.data_pipeline.load_data")
def test_main_pipeline_flow(mock_load, mock_transform, mock_extract, caplog):
    """Test the main function orchestrates the pipeline."""
    data_pipeline.main()

    mock_extract.assert_called_once()
    mock_transform.assert_called_once_with(SAMPLE_RAW_DATA)
    mock_load.assert_called_once_with([{"id": 1, "value": 60}])

    assert "ETL Pipeline Started." in caplog.text
    assert "ETL Pipeline Finished." in caplog.text

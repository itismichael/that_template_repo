import pytest
from fastapi.testclient import TestClient

from examples.web.main import app as fastapi_app


@pytest.fixture(scope="module")
def client():
    with TestClient(fastapi_app) as c:
        yield c


def test_read_root_fastapi(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from FastAPI app! Use /core_greet for core library greeting."
    }


def test_health_check_fastapi(client):
    response = client.get("/health")
    assert response.status_code == 200
    # Assuming settings.APP_NAME and settings.APP_VERSION are available and loaded correctly
    # For a robust test, you might want to mock settings or load them from a test config
    from examples.web.config import settings  # Import settings to get expected values

    expected_response = {
        "status": "ok",
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
    }
    assert response.json() == expected_response


def test_core_greet_endpoint(client):
    response = client.get("/core_greet")
    assert response.status_code == 200
    assert (
        "Hello, App User! This greeting comes from 'your_core_library'."
        in response.json().get("core_message")
    )


def test_core_greet_endpoint_with_name(client, caplog):
    import logging  # Ensure logging is imported

    caplog.set_level(logging.DEBUG, logger="examples.web.main")

    response = client.get("/core_greet?name=TestUser")
    assert response.status_code == 200
    assert (
        "Hello, TestUser! This greeting comes from 'your_core_library'."
        in response.json().get("core_message")
    )
    # Optionally, assert that the debug message was logged to be more explicit
    assert "Core library returned:" in caplog.text


def test_read_item_fastapi(client):
    item_id = 42
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    expected_response = {
        "item_id": item_id,
        "name": "Sample Item",
        "owner": "testuser",  # Matches the default in main.py
    }
    assert response.json() == expected_response


def test_init_logging_debug_level():
    """Test that init_logging can be called with DEBUG level."""
    from examples.web.logging_config import init_logging

    # Store current logging state if possible/necessary, or just call
    # This is primarily for coverage, assuming basicConfig handles re-initialization gracefully enough for tests
    init_logging("DEBUG")
    # Optionally, assert something about the logger's state, though it's tricky with basicConfig
    # For instance, check if the root logger's level is set to DEBUG
    import logging

    assert logging.getLogger().getEffectiveLevel() == logging.DEBUG

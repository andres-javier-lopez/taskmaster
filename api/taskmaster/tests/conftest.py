import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def test_client():
    from taskmaster.app import app

    return TestClient(app)

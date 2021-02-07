import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope='function', autouse=True)
def client():
    from app.main import app
    client = TestClient(app)
    yield client
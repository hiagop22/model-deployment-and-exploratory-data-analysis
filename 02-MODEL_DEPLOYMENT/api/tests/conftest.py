from fastapi.testclient import TestClient
from api.main import app
import pytest



@pytest.fixture
def client():
    client = TestClient(app)
    return client

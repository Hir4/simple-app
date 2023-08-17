import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.app
def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["detail"]["message"] == "Hello World"

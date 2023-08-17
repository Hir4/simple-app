import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
# DEFAULT
header = {"Content-Type": "application/json"}
# CONTENT
content_create_account = {"username": "fael012", "password": "senha123"}
content_create_same_account = {"username": "Fael", "password": "123"}
content_create_account_wrong_fields = {"username": "test", "not_right_field": 54131}


@pytest.mark.app
@pytest.mark.account
def test_create_account(mocker):
    mocker.patch(
        "app.db_functions.create_account",
        return_value={
            "id": "151616516848",
            "username": "fael012",
            "password": "senha123",
            "inserted_at": "2023-08-10 00:00:00",
        },
    )
    response = client.post(
        "/create_account/", headers=header, json=content_create_account
    )
    assert response.status_code == 201
    assert response.json()["detail"]["message"]["username"] == "fael012"
    assert response.json()["detail"]["message"]["password"] == "senha123"


@pytest.mark.app
@pytest.mark.account
def test_create_existing_account(mocker):
    mocker.patch(
        "app.db_functions.create_account",
        return_value="duplicate key value violates unique constraint",
    )
    response = client.post(
        "/create_account/", headers=header, json=content_create_same_account
    )
    assert response.status_code == 409
    assert (
        "duplicate key value violates unique constraint"
        in response.json()["detail"]["message"]
    )


@pytest.mark.app
@pytest.mark.account
def test_create_account_wrong_fields():
    response = client.post(
        "/create_account/", headers=header, json=content_create_account_wrong_fields
    )
    assert response.status_code == 400
    assert "field required" in str(response.json()["detail"]["message"]).lower()

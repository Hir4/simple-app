import uuid
from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.validation_models import AccountModel

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
        return_value=AccountModel(
            id=uuid.uuid4().hex,
            username="fael012",
            password="senha123",
            inserted_at=datetime.utcnow(),
        ),
    )
    response = client.post(
        "/create_account/", headers=header, json=content_create_account
    )
    assert response.status_code == 201
    assert response.json()["username"] == "fael012"
    assert response.json()["password"] == "senha123"


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

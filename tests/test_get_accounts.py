import uuid
from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.validation_models import AccountModel

client = TestClient(app)


@pytest.mark.app
@pytest.mark.account
@pytest.mark.unit_test
def test_get_account_by_name(mocker):
    mocker.patch(
        "app.db_functions.get_account_by_name",
        return_value=AccountModel(
            id=uuid.uuid4().hex,
            username="Fael",
            password="senha123",
            inserted_at=datetime.utcnow(),
        ),
    )
    account_name = "Fael"
    response = client.get(f"/get_account_by_name/{account_name}")
    assert response.status_code == 200
    assert account_name == response.json()["username"]


@pytest.mark.app
@pytest.mark.account
@pytest.mark.unit_test
def test_get_inexisting_accounts_by_name(mocker):
    mocker.patch("app.db_functions.get_account_by_name", return_value=None)
    account_name = "some_name"
    response = client.get(f"/get_account_by_name/{account_name}")
    assert response.status_code == 404
    assert "Account not found" == response.json()["message"]

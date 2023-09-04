# TODO: Procurar como mockar connnect to db em um unico local
# https://stackoverflow.com/questions/17801300/how-to-run-a-method-before-all-tests-in-all-classes
import uuid
from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.validation_models import AccountModel

client = TestClient(app)


@pytest.mark.app
@pytest.mark.account
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
    mocker.patch(
        "app.db_functions.connect_to_db",
        return_value=None,
    )
    account_name = "Fael"
    response = client.get(f"/get_account_by_name/{account_name}")
    assert response.status_code == 200
    assert account_name == response.json()["username"]


@pytest.mark.app
@pytest.mark.account
def test_get_inexisting_accounts_by_name(mocker):
    mocker.patch("app.db_functions.get_account_by_name", return_value=None)
    account_name = "some_name"
    response = client.get(f"/get_account_by_name/{account_name}")
    assert response.status_code == 404
    assert "Account not found" == response.json()["message"]

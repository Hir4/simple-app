import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.app
@pytest.mark.account
def test_get_account_by_name(mocker):
    mocker.patch(
        "app.db_functions.get_account_by_name",
        return_value=["1", "Fael", "teste123", "2023-08-02 00:00:00"],
    )
    account_name = "Fael"
    response = client.get(f"/get_account_by_name/{account_name}")
    assert response.status_code == 200
    assert account_name in response.json()["detail"]["message"]


@pytest.mark.app
@pytest.mark.account
def test_get_inexisting_accounts_by_name(mocker):
    mocker.patch("app.db_functions.get_account_by_name", return_value=None)
    account_name = "some_name"
    response = client.get(f"/get_account_by_name/{account_name}")
    assert response.status_code == 404
    assert "Account not found" == response.json()["detail"]["message"]

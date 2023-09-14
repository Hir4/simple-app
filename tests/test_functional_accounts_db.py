import pytest
import requests

# DEFAULT
header = {"Content-Type": "application/json"}
# CONTENT
content_create_account = {"username": "fael012", "password": "senha123"}
content_create_same_account = {"username": "fael012", "password": "senha123"}
content_create_account_wrong_fields = {"username": "test", "not_right_field": 54131}


@pytest.mark.app
@pytest.mark.account
@pytest.mark.functional_test
def test_create_account():
    response = requests.post(
        "http://localhost:8080/create_account/?env=testing",
        headers=header,
        json=content_create_account,
    )
    print(response.json())
    assert response.status_code == 201
    assert response.json()["username"] == "fael012"
    assert response.json()["password"] == "senha123"


@pytest.mark.app
@pytest.mark.account
@pytest.mark.functional_test
def test_create_existing_account():
    response = requests.post(
        "http://localhost:8080/create_account/?env=testing",
        headers=header,
        json=content_create_same_account,
    )
    assert response.status_code == 409
    assert (
        "Username duplicated, already exists." in response.json()["detail"]["message"]
    )


@pytest.mark.app
@pytest.mark.account
@pytest.mark.functional_test
def test_create_account_wrong_fields():
    response = requests.post(
        "http://localhost:8080/create_account/?env=testing",
        headers=header,
        json=content_create_account_wrong_fields,
    )
    assert response.status_code == 400
    assert "Field required" == response.json()["detail"]["message"][0]["msg"]

import pytest

# DEFAULT
url = "http://localhost:8181"
header = {"Content-Type": "application/json"}
# CONTENT
content_create_account = {"username": "fael012", "password": "123"}
content_create_same_account = {"username": "Fael", "password": "123"}
content_create_account_wrong_fields = {"username": "test", "not_right_field": 54131}


@pytest.mark.app
@pytest.mark.account
def test_create_account(httpx_request):
    response = httpx_request.post(
        f"{url}/create_account/", headers=header, json=content_create_account
    )
    assert response.status_code == 201
    assert response.json()["message"] == "Account created successfully"


@pytest.mark.app
@pytest.mark.account
def test_create_existing_account(httpx_request):
    response = httpx_request.post(
        f"{url}/create_account/", headers=header, json=content_create_same_account
    )
    assert response.status_code == 409
    assert (
        "duplicate key value violates unique constraint" in response.json()["message"]
    )


@pytest.mark.app
@pytest.mark.account
def test_create_account_wrong_fields(httpx_request):
    response = httpx_request.post(
        f"{url}/create_account/",
        headers=header,
        json=content_create_account_wrong_fields,
    )
    assert response.status_code == 400
    assert "Field required" in str(response.json()["message"])

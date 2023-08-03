import pytest

# DEFAULT
url = "http://localhost:8080"
header = {"Content-Type": "application/json"}
# CONTENT
content_create_account = {"username": "fael012", "password": "123"}
content_create_same_account = {"username": "Fael", "password": "123"}


@pytest.mark.app
@pytest.mark.account
def test_create_account(httpx_request):
    response = httpx_request.post(
        f"{url}/create_account/", headers=header, json=content_create_account
    )
    assert response.status_code == 200
    assert response.json() == "Account created successfully"


@pytest.mark.app
@pytest.mark.account
def test_create_existing_account(httpx_request):
    response = httpx_request.post(
        f"{url}/create_account/", headers=header, json=content_create_same_account
    )
    assert response.status_code == 409
    assert "duplicate key value violates unique constraint" in response.text

import sys
import httpx
import pytest
import json
# DEFAULT
url = "http://localhost:8080"
header = {"Content-Type": "application/json"}
# URI
uri_create_account = "create_account"
uri_exchange_rate = "exchange_rate"
# CONTENT
content_create_account = {"username": "fael012", "password": "123"}
content_create_same_account = {"username": "Fael", "password": "123"}
content_exchange_rate = {"timestamp": "1690243200", "symbol": "ethbtc"}


@pytest.mark.api
def test_get_home(httpx_request):
    response = httpx_request.get(f"{url}/")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello World"


@pytest.mark.api
def test_create_account(httpx_request):
    response = httpx_request.post(
        f"{url}/{uri_create_account}/", headers=header, json=content_create_account
    )
    assert response.status_code == 200
    assert response.json() == "Account created successfully"
    

@pytest.mark.api
def test_create_same_account(httpx_request):
    response = httpx_request.post(
        f"{url}/{uri_create_account}/", headers=header, json=content_create_same_account
    )
    assert response.status_code == 500
    assert "duplicate key value violates unique constraint" in response.text


# @pytest.mark.api
# def test_exchange_rate():
#     response = httpx.post(
#         f"{url}/{uri_exchange_rate}/", headers=header, json=content_exchange_rate
#     )
#     assert response.status_code == 200
#     assert response.json() == "Exchange rate registered"

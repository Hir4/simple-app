import pytest

# DEFAULT
url = "http://localhost:8080"


@pytest.mark.app
@pytest.mark.account
def test_get_account_by_name(httpx_request):
    response = httpx_request.get(f"{url}/get_accounts_by_name/Fael")
    assert response.status_code == 200
    assert response.json()[0] == "Fael"


@pytest.mark.app
@pytest.mark.account
def test_get_inexisting_accounts_by_name(httpx_request):
    response = httpx_request.get(f"{url}/get_accounts_by_name/rodrigo_goes056061189156")
    assert response.status_code == 404
    assert response.json() is None

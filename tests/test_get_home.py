import pytest

# DEFAULT
url = "http://localhost:8181"


@pytest.mark.app
def test_get_home(httpx_request):
    response = httpx_request.get(f"{url}/")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello World"

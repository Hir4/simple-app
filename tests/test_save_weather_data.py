import pytest

# DEFAULT
url = "http://localhost:8080"
header = {"Content-Type": "application/json"}
# CONTENT
content_send_weather = {
    "latitude": -23.5475,
    "longitude": -46.6361,
    "start_date": "2023-07-14",
    "end_date": "2023-08-02",
}


@pytest.mark.app
@pytest.mark.weather
def test_save_weather_data(httpx_request):
    response = httpx_request.post(
        f"{url}/historical_weather/", headers=header, json=content_send_weather
    )
    assert response.status_code == 200
    assert response.json() == "Weather saved successfully"
import pytest
import requests

# DEFAULT
header = {"Content-Type": "application/json"}
# CONTENT
state_coordinates = {"SP": {"lat": -23.5475, "long": -46.6361}}
content_weather_api = {
    "latitude": state_coordinates["SP"]["lat"],
    "longitude": state_coordinates["SP"]["long"],
    "start_date": "2023-07-14",
    "end_date": "2023-08-03",
}


@pytest.mark.app
@pytest.mark.weather
@pytest.mark.functional_test
def test_save_weather_data():
    response = requests.post(
        "http://localhost:8080/historical_weather/?env=testing",
        headers=header,
        json=content_weather_api,
    )
    assert response.status_code == 200
    assert round(response.json()["latitude"]) == round(state_coordinates["SP"]["lat"])
    assert round(response.json()["longitude"]) == round(state_coordinates["SP"]["long"])

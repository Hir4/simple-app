import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.validation_models import ApiWeatherModelRequest

client = TestClient(app)
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
def test_save_weather_data(mocker):
    mocker.patch(
        "app.db_functions.insert_weather_table",
        return_value=ApiWeatherModelRequest(
            id="213231321",
            latitude=state_coordinates["SP"]["lat"],
            longitude=state_coordinates["SP"]["long"],
            start_date="2023-07-14",
            end_date="2023-08-03",
            inserted_at="2023-08-10T00:00:00",
        ),
    )
    response = client.post(
        "/historical_weather/", headers=header, json=content_weather_api
    )
    assert response.status_code == 200
    assert response.json()["latitude"] == state_coordinates["SP"]["lat"]
    assert response.json()["longitude"] == state_coordinates["SP"]["long"]

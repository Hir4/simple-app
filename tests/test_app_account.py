import time

import pytest
import requests

url = "http://localhost:8080/create_account/"
content = {"username": "test_name01", "password": "123"}
wrong_content = {"username": "x"}


@pytest.mark.api
def test_create_account_happy_path():
    result = requests.post(url, json=content)
    assert result.status_code == 200


@pytest.mark.api
def test_create_account_same_name():
    result = requests.post(url, json=content)
    assert result.status_code == 500


@pytest.mark.api
def test_create_account_bad_path():
    result = requests.post(url, json=wrong_content)
    assert result.status_code == 422

import httpx
import pytest


@pytest.fixture
def httpx_request():
    client = httpx.Client()
    try:
        yield client
    finally:
        client.close()

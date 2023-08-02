import pytest
import psycopg
import httpx


@pytest.fixture
def httpx_request():
  client = httpx.Client()
  try:
      yield client
  finally:
      client.close()
import pytest
import psycopg2

@pytest.fixture
def db_conn():
    conn = psycopg2.connect(
        database="db_simple_app",
        host="localhost",
        user="user_fael",
        password="test123",
        port="5432",
    )

    yield conn

    conn.close()

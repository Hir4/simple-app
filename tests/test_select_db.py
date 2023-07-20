import pytest


@pytest.mark.db
def test_select_db(db_conn):
    cur = db_conn.cursor()
    test_select_query = "SELECT 1"
    cur.execute(test_select_query)
    result = cur.fetchone()
    cur.close()
    assert result[0] == 1

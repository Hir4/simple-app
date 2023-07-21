import pytest


@pytest.mark.db
def test_write_db(db_conn):
    cur = db_conn.cursor()
    test_write_query = """
    CREATE TABLE test_write(
       test VARCHAR PRIMARY KEY
    );
    SELECT EXISTS (
      SELECT FROM information_schema.tables 
      WHERE table_name = 'test_write'
    );
  """
    cur.execute(test_write_query)
    result = cur.fetchone()
    cur.close()
    assert result[0] is True

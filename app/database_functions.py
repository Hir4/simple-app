import psycopg2


def _connect_to_db():
    conn = psycopg2.connect(
        database="db_simple_app",
        host="postgres",
        user="user_fael",
        password="test123",
        port="5432",
    )
    return conn


def save_data(data):
    conn = _connect_to_db()
    cur = conn.cursor()
    for key, value in data.items():
        insert_query = f"INSERT INTO thoughts(id, thoughts) VALUES('{key}', '{value}')"

    cur.execute(insert_query)
    conn.commit()
    cur.close()
    conn.close()


def get_data():
    conn = _connect_to_db()
    cur = conn.cursor()
    select_query = "SELECT * FROM thoughts"
    cur.execute(select_query)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return dict(result)

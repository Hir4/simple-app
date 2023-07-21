#TODO atualizar para o 3
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
    with _connect_to_db() as conn:
        with conn.cursor() as cur:
            #TODO remover sql injection
            for key, value in data.items():
                insert_query = f"INSERT INTO thoughts(id, thoughts) VALUES('{key}', '{value}')"

            cur.execute(insert_query)


def get_data():
    with _connect_to_db() as conn:
        with conn.cursor() as cur:
            select_query = "SELECT * FROM thoughts"
            cur.execute(select_query)
            result = cur.fetchall()
            return dict(result)

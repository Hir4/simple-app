import psycopg


def _connect_to_db():
    conn = psycopg.connect(
        dbname="db_simple_app",
        host="postgres",
        user="user_fael",
        password="test123",
        port="5432",
    )
    return conn


def create_account(new_account):
    with _connect_to_db() as conn:
        with conn.cursor() as cur:
            insert_query = (
                "INSERT INTO account (id, username, password) VALUES (%s, %s, %s);"
            )
            query_data = (
                new_account.id,
                new_account.username,
                new_account.password,
            )

            cur.execute(insert_query, query_data)
    return "Account created successfully"


def get_accounts():
    with _connect_to_db() as conn:
        with conn.cursor() as cur:
            select_query = "SELECT * FROM account"
            cur.execute(select_query)
            result = cur.fetchall()
            return result

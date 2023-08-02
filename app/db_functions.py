import psycopg

def _connect_to_db():
    conn = psycopg.connect(
        host="postgres",
        port="5432",
        dbname="db_simple_app",
        user="user_fael",
        password="test123"
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


def insert_exchange_rate_table(exchange_rate_response):
    with _connect_to_db() as conn:
        with conn.cursor() as cur:
            for index, value in enumerate(exchange_rate_response):
                insert_query = "INSERT INTO exchange_rate (id, symbol, amount, price, type) VALUES (%s, %s, %s, %s, %s);"
                query_data = (
                    exchange_rate_response[index]["id"],
                    exchange_rate_response[index]["symbol"],
                    exchange_rate_response[index]["amount"],
                    exchange_rate_response[index]["price"],
                    exchange_rate_response[index]["type"],
                )

                cur.execute(insert_query, query_data)
    return "Exchange rate registered"

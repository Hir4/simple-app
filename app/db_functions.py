import os
import uuid
from datetime import datetime

import httpx
import psycopg
from validation_models import AccountModel, WeatherModel


def _connect_to_db():
    conn = psycopg.connect(
        host=os.environ["POSTGRES_HOSTNAME"],
        port=os.environ["POSTGRES_PORT"],
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )
    return conn


def create_account(new_account: AccountModel):
    try:
        new_account.id = uuid.uuid4().hex
        new_account.inserted_at = datetime.now()
        with _connect_to_db() as conn:
            with conn.cursor() as cur:
                insert_query = "INSERT INTO account (id, username, password, inserted_at) VALUES (%s, %s, %s, %s);"
                query_data = (
                    new_account.id,
                    new_account.username,
                    new_account.password,
                    new_account.inserted_at,
                )
                cur.execute(insert_query, query_data)
        return new_account
    except psycopg.Error as e:
        return str(e)

#TODO: Pegar a conta
def get_accounts_by_name(account_name: str):
    with _connect_to_db() as conn:
        with conn.cursor() as cur:
            select_query = "SELECT * FROM account WHERE username = (%s)"
            query_data = (account_name,)
            cur.execute(select_query, query_data)
            result = cur.fetchone()
            return result


def insert_weather_table(weather_info: WeatherModel):
    with httpx.Client() as client:
        historical_weather = client.get(
            f"https://archive-api.open-meteo.com/v1/archive?latitude={weather_info.latitude}&longitude={weather_info.longitude}&start_date={weather_info.start_date}&end_date={weather_info.end_date}&hourly=temperature_2m"
        )
        treated_response = historical_weather.json()
        total_data_returned = len(treated_response["hourly"]["time"])
        with _connect_to_db() as conn:
            for i in range(total_data_returned):
                weather_info.id = uuid.uuid4().hex
                weather_info.inserted_at = datetime.utcnow()
                with conn.cursor() as cur:
                    insert_query = "INSERT INTO weather (id, latitude, longitude, time, temperature, unit, inserted_at) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                    query_data = (
                        weather_info.id,
                        treated_response["latitude"],
                        treated_response["longitude"],
                        treated_response["hourly"]["time"][i],
                        treated_response["hourly"]["temperature_2m"][i],
                        treated_response["hourly_units"]["temperature_2m"],
                        weather_info.inserted_at,
                    )
                    cur.execute(insert_query, query_data)

    return "Weather saved successfully"

import os
import uuid
from datetime import datetime

import httpx
import psycopg

from app.validation_models import (
    AccountModel,
    AccountModelRequest,
    ApiWeatherModel,
    ApiWeatherModelRequest,
)


def connect_to_db() -> psycopg.Connection | bool:
    if not os.environ.get("TEST_ENV"):
        conn = psycopg.connect(
            host=os.environ["POSTGRES_HOSTNAME"],
            port=os.environ["POSTGRES_PORT"],
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
        )
        return conn
    else:
        return False


def create_account(
    new_account: AccountModelRequest, db_conn: psycopg.Connection
) -> AccountModel | str:
    try:
        new_account_id = uuid.uuid4().hex
        new_account_inserted_at = datetime.now()
        with db_conn as conn:
            with conn.cursor() as cur:
                insert_query = """INSERT INTO account (
                                    id, 
                                    username, 
                                    password, 
                                    inserted_at) 
                                VALUES (%s, %s, %s, %s);"""
                query_data = (
                    new_account_id,
                    new_account.username,
                    new_account.password,
                    new_account_inserted_at,
                )
                cur.execute(insert_query, query_data)
        return AccountModel(
            id=new_account_id,
            username=new_account.username,
            password=new_account.password,
            inserted_at=new_account_inserted_at,
        )
    except psycopg.Error as e:  # TODO: Tratar o erro melhor, criar minhas exceptions
        return str(e)


def get_account_by_name(account_name: str, db_conn: psycopg.Connection):
    with db_conn as conn:
        with conn.cursor() as cur:
            select_query = "SELECT * FROM account WHERE username = (%s)"
            query_data = (account_name,)
            cur.execute(select_query, query_data)
            result = cur.fetchone()
            if result is None:
                return None
            return AccountModel(
                id=result[0],
                username=result[1],
                password=result[2],
                inserted_at=result[3],
            )


def insert_weather_table(
    coordinates_date: ApiWeatherModelRequest, db_conn: psycopg.Connection
):
    with httpx.Client() as client:
        historical_weather = client.get(
            f"https://archive-api.open-meteo.com/v1/archive?latitude={coordinates_date.latitude}&longitude={coordinates_date.longitude}&start_date={coordinates_date.start_date}&end_date={coordinates_date.end_date}&hourly=temperature_2m"
        )
        treated_response = historical_weather.json()
        total_data_returned = len(treated_response["hourly"]["time"])
        coordinates_date_id = uuid.uuid4().hex
        coordinates_date_inserted_at = datetime.utcnow()
        with db_conn as conn:
            for i in range(total_data_returned):
                coordinates_date_id = uuid.uuid4().hex
                coordinates_date_inserted_at = datetime.utcnow()
                with conn.cursor() as cur:
                    insert_query = """INSERT INTO weather (
                                        id, 
                                        latitude, 
                                        longitude, 
                                        time, 
                                        temperature, 
                                        unit, 
                                        inserted_at) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                    query_data = (
                        coordinates_date_id,
                        treated_response["latitude"],
                        treated_response["longitude"],
                        treated_response["hourly"]["time"][i],
                        treated_response["hourly"]["temperature_2m"][i],
                        treated_response["hourly_units"]["temperature_2m"],
                        coordinates_date_inserted_at,
                    )
                    cur.execute(insert_query, query_data)

    return ApiWeatherModel(
        id=coordinates_date_id,
        latitude=treated_response["latitude"],
        longitude=treated_response["longitude"],
        start_date=coordinates_date.start_date,
        end_date=coordinates_date.end_date,
        inserted_at=coordinates_date_inserted_at,
    )

import uuid
from datetime import datetime, timedelta

import httpx
import psycopg
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def _connect_to_db():
    conn = psycopg.connect(
        host="app_postgres",
        port=5433,
        dbname="db_simple_app",
        user="user_fael",
        password="test123",
    )
    return conn


def send_weather_temperature(reference_date, latitude, longitude):
    start_date = datetime.strptime(reference_date, "%Y-%m-%d") - timedelta(days=1)
    end_date = start_date 

    with httpx.Client() as client:
        historical_weather = client.get(
            f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date.date()}&end_date={end_date.date()}&hourly=temperature_2m"
        )
        treated_response = historical_weather.json()
        total_data_returned = len(treated_response["hourly"]["time"])
        with _connect_to_db() as conn:
            for i in range(total_data_returned):
                id = uuid.uuid4().hex
                inserted_at = datetime.utcnow()
                with conn.cursor() as cur:
                    insert_query = "INSERT INTO weather (id, latitude, longitude, time, temperature, unit, inserted_at) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                    query_data = (
                        id,
                        treated_response["latitude"],
                        treated_response["longitude"],
                        treated_response["hourly"]["time"][i],
                        treated_response["hourly"]["temperature_2m"][i],
                        treated_response["hourly_units"]["temperature_2m"],
                        inserted_at,
                    )
                    cur.execute(insert_query, query_data)

    return "Weather saved successfully"


my_dag = DAG(
    "weather_temperature_1",
    start_date=datetime(2023, 7, 20),
    schedule_interval="@daily",
    catchup=True
)

python_task = PythonOperator(
    task_id="send_weather_temperature_cmd",
    python_callable=send_weather_temperature,
    op_kwargs={
        "reference_date": "{{ ds }}",
        "latitude": -23.5475,
        "longitude": -46.6361,
    },
    dag=my_dag,
)

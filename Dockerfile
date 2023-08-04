FROM python

WORKDIR /app

ENV POSTGRES_DB="db_simple_app"
ENV POSTGRES_USER="user_fael"
ENV POSTGRES_PASSWORD="test123"
ENV POSTGRES_HOSTNAME=app_postgres
ENV POSTGRES_PORT=5433

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./app/ .

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "main:app"]
FROM python

ENV POSTGRES_DB="db_simple_app"
ENV POSTGRES_USER="user_fael"
ENV POSTGRES_PASSWORD="test123"
ENV POSTGRES_HOSTNAME=app_postgres
ENV POSTGRES_PORT=5432

WORKDIR /simple-app

RUN pip install poetry

COPY pyproject.toml pyproject.toml

RUN poetry install

COPY ./app/ ./app/

CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "app.main:app"]
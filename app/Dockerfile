FROM python

WORKDIR app/

COPY . /app

RUN pip install Flask
RUN pip install psycopg2

CMD ["python3", "app.py"]


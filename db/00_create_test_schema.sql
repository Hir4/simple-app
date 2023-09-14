CREATE SCHEMA testing_env;
CREATE TABLE testing_env.account (
    id VARCHAR PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    inserted_at TIMESTAMP NOT NULL
);

CREATE TABLE testing_env.weather (
    id VARCHAR PRIMARY KEY,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    time TIMESTAMP NULL,
    temperature REAL NULL,
    unit VARCHAR NOT NULL,
    inserted_at TIMESTAMP NOT NULL
);
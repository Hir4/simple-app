-- CREATE TABLE
DROP TABLE IF EXISTS account;
CREATE TABLE account (
    id VARCHAR PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    inserted_at TIMESTAMP NOT NULL
);

DROP TABLE IF EXISTS weather;
CREATE TABLE weather (
    id VARCHAR PRIMARY KEY,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    time TIMESTAMP NULL,
    temperature REAL NULL,
    unit VARCHAR NOT NULL,
    inserted_at TIMESTAMP NOT NULL
);
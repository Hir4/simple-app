#!/bin/bash
docker compose up -d

check=1
while [ $check != 0 ]; do 
  echo "App not ready";
  curl http://localhost:8181/ -s
  check=$?
  sleep 5
done

.venv/bin/pytest -v
docker compose down
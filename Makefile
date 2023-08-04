MAKEFLAGS += --always-make

run_app:
	docker compose up

run_airflow:
	docker compose -f docker-compose-airflow.yml up

run_all:
	docker compose -f docker-compose-airflow.yml -f docker-compose.yml up

down_app:
	docker compose down

tests:
	bash script_run_tests.sh
	
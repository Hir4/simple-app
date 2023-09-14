MAKEFLAGS += --always-make

run_app:
	docker compose up

down_app:
	docker compose down

unit_test:
	TEST_ENV=test poetry run pytest -v -m unit_test

functional_test:
	poetry run pytest -v -m functional_test
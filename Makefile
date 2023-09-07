MAKEFLAGS += --always-make

run_app:
	docker compose up

down_app:
	docker compose down

tests_mock:
	TEST_ENV=test poetry run pytest -v -m unit_test
	
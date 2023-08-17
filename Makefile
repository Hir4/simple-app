MAKEFLAGS += --always-make

run_app:
	docker compose up

down_app:
	docker compose down

tests:
	poetry run pytest -v
	
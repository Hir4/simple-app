MAKEFLAGS += --always-make

run_app:
	docker compose up

test_db:
	docker compose up -d
	pytest -v -m "db"
	docker compose down
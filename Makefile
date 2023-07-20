MAKEFLAGS += --always-make

dot_env:
	python3 -m venv .venv
	pip install -r requirements.txt

run_app:
	docker compose up
MAKEFLAGS += --always-make

dot_env:
	python3 -m venv .venv
	pip install Flask
	pip install isort
	pip install black

run_app:
	docker compose up
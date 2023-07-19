MAKEFLAGS += --always-make

dot_env:
	python3 -m venv .venv
	pip install Flask
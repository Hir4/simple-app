MAKEFLAGS += --always-make

dot_env:
	python3 -m venv .venv
	pip install Flask

run_flask:
	docker build -t my-app .
	docker run -p 8080:8080 my-app:latest
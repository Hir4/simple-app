MAKEFLAGS += --always-make

run_flask:
	docker build -t my-app .
	docker run -p 8080:8080 my-app:latest
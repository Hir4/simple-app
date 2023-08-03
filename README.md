# Simple App
Everything I'm studying I'm putting in this repo, to help me improve my skills.

# Prerequisite
- [Docker](https://docs.docker.com/engine/install/ubuntu/#installation-methods)

# Run WEB and DB
You can run this app with the following commands:
    
    make run_app

Turn off with:

    make down_app

## Acessing container
You can access container with:

    docker exec -it <CONTAINER> /bin/bash

# Run Tests
You can easily run tests with:

    make tests
.PHONY: help build run kill create_venv

# Default command, shows quick help
help:
	@echo "Use 'make build' to build the Docker containers."
	@echo "Use 'make run' to run the Docker containers in the background."
	@echo "Use 'make kill' to stop and remove all Docker containers, networks, and volumes."

# Build Docker containers
build: create_environment_variables create_venv
	@docker-compose build

# Run Docker containers
run:
	@docker-compose up

# Stop and remove all Docker containers, networks, and volumes
kill:
	@docker-compose down -v --remove-orphans

# Create virtual environment if it does not exist
create_venv:
	@echo "Checking if virtual environment exists..."
	@test -d backend/env || (echo "Creating virtual environment..." && python3.10 -m venv backend/env)

create_environment_variables:
	@echo "Creating environment variables..."
	@cp env_exemple.txt .env
.PHONY: help build run kill

# Default command, shows quick help
help:
	@echo "Use 'make build' to build the Docker containers."
	@echo "Use 'make run' to run the Docker containers in the background."
	@echo "Use 'make kill' to stop and remove all Docker containers, networks, and volumes."

# Build Docker containers
build:
	@docker-compose build

# Run Docker containers
run:
	@docker-compose up

# Stop and remove all Docker containers, networks, and volumes
kill:
	@docker-compose down -v --remove-orphans

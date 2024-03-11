.PHONY: help clean build run

# Default command, shows quick help
help:
	@echo "Use 'make build' to build the Docker container."
	@echo "Use 'make run' to run the Docker container."
	@echo "Use 'make clean' to cleaning up temporary files and Docker container"

# Clean up temporary files and Docker container
clean:
	@echo "Cleaning up temporary files and Docker container..."
	@docker-compose down --rmi all -v

# Create virtual environment if it does not exist
create_venv:
	@echo "Checking if virtual environment exists..."
	@test -d env || (echo "Creating virtual environment..." && python3.10 -m venv env)

# Build the Docker container
build: create_venv
	@echo "Building the Docker container..."
	@( \
	    . env/bin/activate; \
	    docker-compose build \
	)

# Run migrations
makemigrations: create_venv
	@echo "Running 'makemigrations'..."
	@( \
	    . env/bin/activate; \
	    docker-compose run web python manage.py makemigrations \
	)

# Apply migrations
migrate: create_venv
	@echo "Running 'migrate'..."
	@( \
	    . env/bin/activate; \
	    docker-compose run web python manage.py migrate \
	)

# Run tests
test: create_venv
	@echo "Running tests..."
	@( \
	    . env/bin/activate; \
	    docker-compose run web python manage.py test \
	)

# Build, migrate, run tests, and then run the Docker container
run: create_venv build makemigrations migrate test
	@echo "Running the Docker container..."
	@( \
	    . env/bin/activate; \
	    docker-compose up -d \
	)

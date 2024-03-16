# Use Python image as base
FROM python:3.10

# Set the working directory to /backend
WORKDIR /backend

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the rest of the source code to the working directory
COPY . .

# Grant execute permission to entrypoint script
RUN chmod +x entrypoint.sh

# Default command to run the backend server
CMD ["./entrypoint.sh"]

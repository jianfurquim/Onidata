# Use Python 3.10 image as base
FROM python:3.10

# Set the working directory to /backend
WORKDIR /backend

# Copy the project's requirements file to the working directory
COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the rest of the source code to the working directory
COPY . .

# Copy the custom entrypoint script to the working directory
COPY entrypoint.sh .

# Grant execute permission to the entrypoint script
RUN chmod +x entrypoint.sh

# Set the entrypoint script as the default command
ENTRYPOINT ["./entrypoint.sh"]

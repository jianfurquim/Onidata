# Use Node.js image as base
FROM node:latest

# Set the working directory to /frontend
WORKDIR /frontend

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the source code to the working directory
COPY . .

# Default command to run the frontend server
CMD ["npm", "run", "dev"]

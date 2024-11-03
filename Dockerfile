# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application to the container
COPY . .

# Copy the scores.txt file to the specified location
COPY scores.txt /scores.txt

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "main_scores.py"]

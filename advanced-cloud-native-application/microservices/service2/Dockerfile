FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 8080 to allow communication to/from the Flask application
EXPOSE 8080

# Command to run the Flask application when the container starts
CMD ["python", "app.py"]

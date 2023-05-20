# Use the Python base image
FROM python:3.7-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code
COPY . .

# Expose the required port
EXPOSE 5000

# Set the command to run the back-end server
CMD ["python", "app.py"]

# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend source code
COPY app.py .
COPY templates ./templates

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

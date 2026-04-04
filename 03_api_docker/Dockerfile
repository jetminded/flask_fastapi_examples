# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY main.py .
COPY run.sh .

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Make script executable (optional if you want to use it)
RUN chmod +x run.sh

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

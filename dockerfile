# Use official Python runtime as base image
FROM python:3.9-slim
# Set working directory in container
WORKDIR /app
# Copy Python file to container
COPY *.py .
# Command to run when container starts
CMD ["python", "main.py"]
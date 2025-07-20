# Use a minimal base image with Python
FROM python:3.11-slim

# Create non-root user
RUN useradd --create-home appuser

# Set workdir and install dependencies
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set permissions
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Set environment variables if needed
# ENV PYTHONUNBUFFERED=1

# Start the Celery worker
CMD ["celery", "-A", "alx_travel_app", "worker", "--loglevel=info"]
FROM python:3.11-slim

LABEL Author="YuzkoBot"

# Environment variables to ensure immediate output and no .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /sinai_bot

# Install dependencies
COPY requirements_docker.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements_docker.txt && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Copy the application code
COPY . .
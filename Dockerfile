# Use an official lightweight Python image
FROM python:3.9-slim

# Install system dependencies including espeak for pyttsx3
RUN apt-get update && apt-get install -y \
    procps \
    libportaudio2 \
    libsdl2-2.0-0 \
    ffmpeg \
    espeak \
    libespeak-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create a test mode script for CI pipeline
RUN echo '#!/usr/bin/env python\nimport sys\nprint("Hello from Jarvis!")' > /app/client.py && \
    chmod +x /app/client.py

# Make sure python output is unbuffered for better logging
ENV PYTHONUNBUFFERED=1

# Set the command to run Jarvis with unbuffered output
CMD ["python", "-u", "main.py"]
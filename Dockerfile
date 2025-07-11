FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download model weights at build time (optional for faster runtime)
RUN python -c "from transformers import pipeline; pipeline('text-generation', model='gpt2')"

# Copy source code
COPY app ./app
WORKDIR /app/app

# Create a writable log file
RUN touch log.jsonl && chmod 666 log.jsonl

# Expose API port
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

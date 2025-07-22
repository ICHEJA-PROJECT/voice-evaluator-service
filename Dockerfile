FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create and use working directory
WORKDIR /app

# Upgrade pip and install wheel for better package installation
RUN pip install --upgrade pip wheel

# Copy requirements and install dependencies with optimizations
COPY requirements.txt .

# Install PyTorch CPU-only version first to avoid CUDA packages
RUN pip install --no-cache-dir \
    --timeout=300 \
    --retries=3 \
    torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install other requirements
RUN pip install --no-cache-dir \
    --timeout=300 \
    --retries=3 \
    -r requirements.txt

COPY app/ ./app

# Expose port and run app
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]

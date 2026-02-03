FROM python:3.12-slim-bookworm

# 1. Install system libraries (including WeasyPrint dependencies)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libcairo2-dev \
    pkg-config \
    libpango1.0-dev \
    build-essential \
    texlive \
    texlive-latex-extra \
    curl \
    libjpeg-dev \
    zlib1g-dev \
    libffi-dev \
    libnss3 \
    libatk-bridge2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf2.0-0 \
    shared-mime-info \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. Copy requirements.txt and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Install Playwright browsers
RUN playwright install chromium
RUN playwright install-deps

# 4. Copy all code
COPY . .

# 5. Start API
CMD ["uvicorn", "api_minimal:app", "--host", "0.0.0.0", "--port", "8000"]

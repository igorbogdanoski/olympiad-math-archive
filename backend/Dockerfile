FROM python:3.12-slim-bookworm

# 1. Инсталација на системски библиотеки
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
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. ВАЖНО: Копирај го requirements.txt од 'backend' папката
COPY backend/requirements.txt .

# 3. Инсталирај Python библиотеки
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium

# 4. Копирај го ЦЕЛИОТ проект
COPY . .

# 5. Влези во backend папката
WORKDIR /app/backend

# 6. Стартувај
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

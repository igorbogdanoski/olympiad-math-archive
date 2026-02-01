<<<<<<< HEAD
# Користиме официјален Python image (slim верзија за помала големина)
FROM python:3.12-slim

# 1. Инсталација на системски зависности за Manim (ffmpeg, libcairo) и Playwright
=======
FROM python:3.12-slim-bookworm

# 1. Инсталација на системски библиотеки
>>>>>>> 2cfe4e73e9ab08775608bd53fa4d5ed4ddf2ab80
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libcairo2-dev \
    pkg-config \
    libpango1.0-dev \
    build-essential \
    texlive \
    texlive-latex-extra \
    curl \
<<<<<<< HEAD
    && rm -rf /var/lib/apt/lists/*

# 2. Поставување на работна околина
WORKDIR /app

# 3. Копирање на requirements и инсталација
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Инсталација на Playwright прелистувачи
RUN playwright install chromium
RUN playwright install-deps

# 5. Копирање на целиот код
COPY . .

# 6. Оваа команда е default, но ќе ја прегазиме во docker-compose
=======
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
>>>>>>> 2cfe4e73e9ab08775608bd53fa4d5ed4ddf2ab80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

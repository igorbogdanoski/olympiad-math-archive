@echo off
REM Start Redis Queue System for Manim Rendering
REM Run this script to start worker process

echo.
echo ========================================
echo   Manim Queue Worker Startup
echo ========================================
echo.

REM Check if Redis is running
echo [1/3] Checking Redis connection...
redis-cli ping >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Redis is not running!
    echo.
    echo Please start Redis first:
    echo   Option 1: redis-server
    echo   Option 2: docker run -d -p 6379:6379 redis:7-alpine
    echo   Option 3: wsl -d Ubuntu; sudo service redis-server start
    echo.
    pause
    exit /b 1
)
echo [OK] Redis is running

REM Check if Node.js is installed
echo [2/3] Checking Node.js...
where node >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js not found!
    pause
    exit /b 1
)
echo [OK] Node.js found

REM Start worker
echo [3/3] Starting Manim Queue Worker...
echo.
cd web
npm run worker:manim

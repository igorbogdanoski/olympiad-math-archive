# ========================================
# BULLETPROOF TEST - Quick Start
# ========================================

Write-Host "`n=== BULLETPROOF QUIZ SYSTEM TEST ===" -ForegroundColor Cyan
Write-Host ""

# Check backend
Write-Host "[1/3] Checking Backend..." -ForegroundColor Yellow
try {
    Invoke-WebRequest -Uri "http://localhost:8000/docs" -TimeoutSec 2 -ErrorAction Stop | Out-Null
    Write-Host "      OK - Backend is running" -ForegroundColor Green
} catch {
    Write-Host "      FAILED - Start backend first:" -ForegroundColor Red
    Write-Host "      cd backend && uvicorn main:app --reload" -ForegroundColor White
    exit
}

# Check frontend
Write-Host "[2/3] Checking Frontend..." -ForegroundColor Yellow
try {
    Invoke-WebRequest -Uri "http://localhost:4321" -TimeoutSec 2 -ErrorAction Stop | Out-Null
    Write-Host "      OK - Frontend is running" -ForegroundColor Green
} catch {
    Write-Host "      FAILED - Start frontend first:" -ForegroundColor Red
    Write-Host "      cd web && npm run dev" -ForegroundColor White
    exit
}

# Create quiz
Write-Host "[3/3] Creating Live Quiz..." -ForegroundColor Yellow

$quizData = @{
    teacher_id = "test_teacher"
    quiz_title = "Bulletproof Test Quiz"
    bro_codes = @("M.7.2.3", "M.7.2.4")
    question_count = 3
    time_limit = 5
    formats = @("multiple_choice", "true_false")
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "http://localhost:8000/api/quiz-generator/live/create" `
        -Method Post -Body $quizData -ContentType "application/json" -ErrorAction Stop

    $code = $response.access_code
    $id = $response.quiz_id

    Write-Host "      OK - Quiz created!" -ForegroundColor Green
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host " ACCESS CODE: $code" -ForegroundColor Yellow
    Write-Host " QUIZ ID:     $id" -ForegroundColor White
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""

    Set-Clipboard -Value $code
    Write-Host "Code copied to clipboard!" -ForegroundColor Magenta

} catch {
    Write-Host "      FAILED - Cannot create quiz" -ForegroundColor Red
    Write-Host "      Error: $($_.Exception.Message)" -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "=== TEST INSTRUCTIONS ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "STEP 1: Open Student Portal" -ForegroundColor White
Write-Host "        http://localhost:4321/student/quiz" -ForegroundColor Cyan
Write-Host ""
Write-Host "STEP 2: Enter code: $code" -ForegroundColor White
Write-Host ""
Write-Host "STEP 3: Enter name: Test Student" -ForegroundColor White
Write-Host ""
Write-Host "STEP 4: Answer the quiz (3 questions)" -ForegroundColor White
Write-Host ""
Write-Host "STEP 5: BEFORE clicking Submit:" -ForegroundColor Red
Write-Host "        - Open Chrome DevTools (F12)" -ForegroundColor Yellow
Write-Host "        - Network tab -> Dropdown -> Offline" -ForegroundColor Yellow
Write-Host "        - OR disable Wi-Fi on phone" -ForegroundColor Yellow
Write-Host ""
Write-Host "STEP 6: Click 'Submit Test'" -ForegroundColor White
Write-Host ""
Write-Host "EXPECTED:" -ForegroundColor Green
Write-Host "  - NO alert error" -ForegroundColor Gray
Write-Host "  - See 'No internet connection' message" -ForegroundColor Gray
Write-Host "  - Toast: 'No internet. Will send auto...'" -ForegroundColor Gray
Write-Host ""
Write-Host "STEP 7: Enable internet (Disable 'Offline')" -ForegroundColor White
Write-Host ""
Write-Host "STEP 8: Wait 5-10 seconds..." -ForegroundColor White
Write-Host ""
Write-Host "EXPECTED:" -ForegroundColor Green
Write-Host "  - Toast: 'Successfully synced!'" -ForegroundColor Gray
Write-Host "  - Score appears (instead of '?')" -ForegroundColor Gray
Write-Host "  - Confetti animation" -ForegroundColor Gray
Write-Host ""

Write-Host "=== VALIDATION ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "DevTools -> Application -> Local Storage" -ForegroundColor White
Write-Host "  - Offline: Should have 'quiz_submission_queue'" -ForegroundColor Gray
Write-Host "  - Online:  Should be cleared (empty)" -ForegroundColor Gray
Write-Host ""

Write-Host "Teacher Dashboard:" -ForegroundColor Yellow
Write-Host "http://localhost:4321/teachers/live-quiz?id=$id" -ForegroundColor Cyan
Write-Host ""

Write-Host "Opening Student Portal..." -ForegroundColor Magenta
Start-Sleep -Seconds 1
Start-Process "http://localhost:4321/student/quiz"

Write-Host ""
Write-Host "Good luck testing!" -ForegroundColor Green
Write-Host ""

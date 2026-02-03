# ========================================
# GAMIFICATION TEST - Speed Bonus System
# ========================================

Write-Host "`n=== SPEED BONUS GAMIFICATION TEST ===" -ForegroundColor Cyan
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
Write-Host "[3/3] Creating Speed Test Quiz..." -ForegroundColor Yellow

$quizData = @{
    teacher_id = "test_teacher"
    quiz_title = "Speed Bonus Test - Lightning Round"
    bro_codes = @("M.7.2.3", "M.7.2.4", "M.7.3.1")
    question_count = 5
    time_limit = 10
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
Write-Host "=== GAMIFICATION TEST INSTRUCTIONS ===" -ForegroundColor Cyan
Write-Host ""

Write-Host "TEST 1: SPEED BADGE" -ForegroundColor Yellow
Write-Host "  1. Open Student Portal" -ForegroundColor White
Write-Host "  2. Enter code: $code" -ForegroundColor Cyan
Write-Host "  3. Answer FIRST question VERY FAST (< 5 seconds)" -ForegroundColor White
Write-Host ""
Write-Host "  EXPECTED:" -ForegroundColor Green
Write-Host "    - Lightning bolt badge appears: BRZO!" -ForegroundColor Gray
Write-Host "    - Yellow popup animation" -ForegroundColor Gray
Write-Host ""

Write-Host "TEST 2: SPEED BONUS POINTS" -ForegroundColor Yellow
Write-Host "  1. Question 1: Answer in 2 seconds (fast)" -ForegroundColor White
Write-Host "  2. Question 2: Answer in 15 seconds (medium)" -ForegroundColor White
Write-Host "  3. Question 3: Answer in 30 seconds (slow)" -ForegroundColor White
Write-Host "  4. Submit quiz" -ForegroundColor White
Write-Host ""
Write-Host "  EXPECTED:" -ForegroundColor Green
Write-Host "    - Fast answer gets ~200% points" -ForegroundColor Gray
Write-Host "    - Medium answer gets ~150% points" -ForegroundColor Gray
Write-Host "    - Slow answer gets ~100% points" -ForegroundColor Gray
Write-Host ""

Write-Host "TEST 3: STREAK SYSTEM" -ForegroundColor Yellow
Write-Host "  1. Answer 5 questions CORRECTLY in a row" -ForegroundColor White
Write-Host "  2. Submit quiz" -ForegroundColor White
Write-Host ""
Write-Host "  EXPECTED:" -ForegroundColor Green
Write-Host "    - Feedback: 'Neveroaten Streak: 5!'" -ForegroundColor Gray
Write-Host "    - EXTRA confetti (300 particles)" -ForegroundColor Gray
Write-Host ""

Write-Host "TEST 4: SCORE COMPARISON" -ForegroundColor Yellow
Write-Host "  Run quiz TWICE with same student:" -ForegroundColor White
Write-Host ""
Write-Host "  Round 1: Answer slowly (20-30 sec per question)" -ForegroundColor White
Write-Host "  Round 2: Answer fast (< 5 sec per question)" -ForegroundColor White
Write-Host ""
Write-Host "  EXPECTED:" -ForegroundColor Green
Write-Host "    - Round 2 score should be ~2x higher" -ForegroundColor Gray
Write-Host "    - Same correct answers, different points" -ForegroundColor Gray
Write-Host ""

Write-Host "=== DEVELOPER TOOLS ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Monitor in Console (F12):" -ForegroundColor White
Write-Host "  - Watch for: 'questionStartTime' logs" -ForegroundColor Gray
Write-Host "  - Check: localStorage.answers object" -ForegroundColor Gray
Write-Host "  - Verify: {option: 'A', time: 3} structure" -ForegroundColor Gray
Write-Host ""

Write-Host "Backend Response (should include):" -ForegroundColor White
Write-Host "  - 'streak': 5" -ForegroundColor Gray
Write-Host "  - 'max_score': <dynamic value>" -ForegroundColor Gray
Write-Host "  - 'feedback': 'Neveroaten Streak...'" -ForegroundColor Gray
Write-Host ""

Write-Host "Teacher Dashboard:" -ForegroundColor Yellow
Write-Host "http://localhost:4321/teachers/live-quiz?id=$id" -ForegroundColor Cyan
Write-Host ""
Write-Host "  - Check student scores (should vary based on speed)" -ForegroundColor Gray
Write-Host "  - Compare time_spent per answer" -ForegroundColor Gray
Write-Host ""

Write-Host "Opening Student Portal..." -ForegroundColor Magenta
Start-Sleep -Seconds 1
Start-Process "http://localhost:4321/student/quiz"

Write-Host ""
Write-Host "Test the speed! May the fastest win!" -ForegroundColor Green
Write-Host ""

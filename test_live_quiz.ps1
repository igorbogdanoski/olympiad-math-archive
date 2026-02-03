# ========================================
# LIVE QUIZ E2E TEST SCRIPT
# ========================================

$API_BASE = "http://localhost:8000"

Write-Host "`n🎯 LIVE QUIZ E2E TEST" -ForegroundColor Cyan
Write-Host "==========================================`n" -ForegroundColor Cyan

# Step 1: Create Live Quiz
Write-Host "📝 Чекор 1: Креирање на Live Quiz..." -ForegroundColor Yellow

$quizData = @{
    teacher_id = "teacher_demo_001"
    quiz_title = "DEMO Математика - 7 Одделение"
    bro_codes = @("М.7.2.3", "М.7.2.4", "М.7.3.1")
    question_count = 5
    time_limit = 10
    formats = @("multiple_choice", "true_false")
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "$API_BASE/api/quiz-generator/live/create" `
        -Method Post `
        -Body $quizData `
        -ContentType "application/json" `
        -ErrorAction Stop

    Write-Host "✅ Quiz креиран успешно!" -ForegroundColor Green
    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host "  QUIZ ID:      $($response.quiz_id)" -ForegroundColor White
    Write-Host "  ACCESS CODE:  $($response.access_code)" -ForegroundColor Yellow
    Write-Host "  QUESTIONS:    $($response.question_count)" -ForegroundColor White
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host ""

    # Save to clipboard
    Set-Clipboard -Value $response.quiz_id
    Write-Host "📋 Quiz ID е ископиран во Clipboard!" -ForegroundColor Magenta
    Write-Host ""

    # URLs
    $teacherUrl = "http://localhost:4321/teachers/live-quiz?id=$($response.quiz_id)"
    $studentUrl = "http://localhost:4321/student/quiz"

    Write-Host "🔗 ЛИНКОВИ:" -ForegroundColor Green
    Write-Host ""
    Write-Host "   TEACHER DASHBOARD:" -ForegroundColor Yellow
    Write-Host "   $teacherUrl" -ForegroundColor White
    Write-Host ""
    Write-Host "   STUDENT PORTAL:" -ForegroundColor Yellow  
    Write-Host "   $studentUrl" -ForegroundColor White
    Write-Host "   (Внеси код: $($response.access_code))" -ForegroundColor Gray
    Write-Host ""

    # Test Plan
    Write-Host "📋 ТЕСТ ПЛАН:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "   1️⃣  Отвори го TEACHER DASHBOARD во browser" -ForegroundColor White
    Write-Host "       → Треба да го видиш кодот $($response.access_code)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "   2️⃣  Отвори STUDENT PORTAL во друг tab (или телефон)" -ForegroundColor White
    Write-Host "       → Внеси код: $($response.access_code)" -ForegroundColor Gray
    Write-Host "       → Внеси име: 'Тест Ученик'" -ForegroundColor Gray
    Write-Host ""
    Write-Host "   3️⃣  На Teacher Dashboard треба да се појави картичка!" -ForegroundColor White
    Write-Host "       → Статус: '✍️ РАБОТИ...'" -ForegroundColor Gray
    Write-Host ""
    Write-Host "   4️⃣  Реши го квизот и кликни 'Предај'" -ForegroundColor White
    Write-Host "       → Картичката треба да стане ЗЕЛЕНА" -ForegroundColor Gray
    Write-Host "       → Да ги покаже поените!" -ForegroundColor Gray
    Write-Host ""

    # Open URLs automatically
    Write-Host "🚀 Отварам линкови автоматски..." -ForegroundColor Magenta
    Start-Sleep -Seconds 2
    
    Start-Process $teacherUrl
    Start-Sleep -Seconds 1
    Start-Process $studentUrl

    Write-Host ""
    Write-Host "✨ ГОТОВО! Добра среќа со тестирањето!" -ForegroundColor Green
    Write-Host ""

} catch {
    Write-Host ""
    Write-Host "❌ ГРЕШКА!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Порака: $($_.Exception.Message)" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Можни причини:" -ForegroundColor Yellow
    Write-Host "  1. Backend не работи (стартувај го: cd backend && uvicorn main:app --reload)" -ForegroundColor Gray
    Write-Host "  2. Frontend не работи (стартувај го: cd web && npm run dev)" -ForegroundColor Gray
    Write-Host "  3. Нема податоци во база за тие БРО кодови" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Тест детали:" -ForegroundColor Gray
    Write-Host $_.Exception | Format-List -Force
}

Write-Host ""
Write-Host "Притисни било кој копче за излез..." -ForegroundColor DarkGray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

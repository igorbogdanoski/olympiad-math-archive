# ========================================
# БРЗО ТЕСТИРАЊЕ - Bulletproof Quiz System
# ========================================

Write-Host "`n🚀 СТАРТУВАМ ТЕСТ СЕСИЈА..." -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Проверка дали backend работи
Write-Host "1️⃣  Проверка на Backend..." -ForegroundColor Yellow
try {
    $backendCheck = Invoke-WebRequest -Uri "http://localhost:8000/docs" -TimeoutSec 2 -ErrorAction Stop
    Write-Host "   ✅ Backend работи!" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Backend НЕ работи!" -ForegroundColor Red
    Write-Host "   Стартувај го во друг терминал:" -ForegroundColor Yellow
    Write-Host "   cd backend" -ForegroundColor White
    Write-Host "   uvicorn main:app --reload" -ForegroundColor White
    Write-Host ""
    exit
}

# Проверка дали frontend работи
Write-Host "`n2️⃣  Проверка на Frontend..." -ForegroundColor Yellow
try {
    $frontendCheck = Invoke-WebRequest -Uri "http://localhost:4321" -TimeoutSec 2 -ErrorAction Stop
    Write-Host "   ✅ Frontend работи!" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Frontend НЕ работи!" -ForegroundColor Red
    Write-Host "   Стартувај го во друг терминал:" -ForegroundColor Yellow
    Write-Host "   cd web" -ForegroundColor White
    Write-Host "   npm run dev" -ForegroundColor White
    Write-Host ""
    exit
}

# Креирај live quiz
Write-Host "`n3️⃣  Креирам Live Quiz..." -ForegroundColor Yellow

$quizData = @{
    teacher_id = "test_teacher"
    quiz_title = "🛡️ BULLETPROOF TEST - Offline Challenge"
    bro_codes = @("М.7.2.3", "М.7.2.4")
    question_count = 3
    time_limit = 5
    formats = @("multiple_choice", "true_false")
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "http://localhost:8000/api/quiz-generator/live/create" `
        -Method Post `
        -Body $quizData `
        -ContentType "application/json" `
        -ErrorAction Stop

    $quizId = $response.quiz_id
    $accessCode = $response.access_code

    Write-Host "   ✅ Quiz креиран!" -ForegroundColor Green
    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host "  ACCESS CODE:  $accessCode" -ForegroundColor Yellow
    Write-Host "  QUIZ ID:      $quizId" -ForegroundColor White
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan

    # Copy code to clipboard
    Set-Clipboard -Value $accessCode
    Write-Host "`n📋 Кодот е ископиран! Paste со Ctrl+V" -ForegroundColor Magenta

} catch {
    Write-Host "   ❌ Грешка при креирање на quiz!" -ForegroundColor Red
    Write-Host "   Причина: $($_.Exception.Message)" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   Можни проблеми:" -ForegroundColor Yellow
    Write-Host "   - Нема податоци за БРО кодови М.7.2.3, М.7.2.4" -ForegroundColor Gray
    Write-Host "   - MongoDB не е поврзана" -ForegroundColor Gray
    exit
}

Write-Host "`n" 
Write-Host "╔════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                                            ║" -ForegroundColor Cyan
Write-Host "║     🧪 BULLETPROOF ТЕСТ ИНСТРУКЦИИ        ║" -ForegroundColor Cyan
Write-Host "║                                            ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

Write-Host "📱 ТЕСТ 1: AIRPLANE MODE (КРИТИЧЕН ТЕСТ)" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host ""
Write-Host "   1. Отвори Student Portal:" -ForegroundColor White
Write-Host "      http://localhost:4321/student/quiz" -ForegroundColor Cyan
Write-Host ""
Write-Host "   2. Внеси код: $accessCode" -ForegroundColor White
Write-Host ""
Write-Host "   3. Внеси име: Тест Ученик" -ForegroundColor White
Write-Host ""
Write-Host "   4. Реши го квизот (3 прашања)" -ForegroundColor White
Write-Host ""
Write-Host "   5. ⚠️  ПРЕД 'Предај':" -ForegroundColor Red
Write-Host "      → Отвори Chrome DevTools (F12)" -ForegroundColor Yellow
Write-Host "      → Network tab → Dropdown → Offline" -ForegroundColor Yellow
Write-Host "      → ИЛИ исклучи Wi-Fi на телефон" -ForegroundColor Yellow
Write-Host ""
Write-Host "   6. Кликни '🏁 Предај Тест'" -ForegroundColor White
Write-Host ""
Write-Host "   ✅ ОЧЕКУВАНО:" -ForegroundColor Green
Write-Host "      • НЕ треба alert грешка" -ForegroundColor Gray
Write-Host "      • Види '⚠️ Нема интернет конекција...'" -ForegroundColor Gray
Write-Host "      • Toast: '📡 Нема интернет. Ќе се прати...'" -ForegroundColor Gray
Write-Host ""
Write-Host "   7. Вклучи интернет назад (Disable 'Offline')" -ForegroundColor White
Write-Host ""
Write-Host "   8. Почекај 5-10 секунди..." -ForegroundColor White
Write-Host ""
Write-Host "   ✅ ОЧЕКУВАНО:" -ForegroundColor Green
Write-Host "      • Toast: '✅ Успешно синхронизирано!'" -ForegroundColor Gray
Write-Host "      • Score се прикажува (наместо '?')" -ForegroundColor Gray
Write-Host "      • Confetti 🎉" -ForegroundColor Gray
Write-Host ""

Write-Host "`n📊 ВАЛИДАЦИЈА:" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host ""
Write-Host "   DevTools → Application → Local Storage" -ForegroundColor White
Write-Host "   • Offline: Треба 'quiz_submission_queue'" -ForegroundColor Gray
Write-Host "   • Online: Треба да се исчисти (празно)" -ForegroundColor Gray
Write-Host ""

Write-Host "`n🖥️  TEACHER DASHBOARD:" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host ""
Write-Host "   http://localhost:4321/teachers/live-quiz?id=$quizId" -ForegroundColor Cyan
Write-Host ""
Write-Host "   ✅ Треба да се прикаже картичка со score!" -ForegroundColor Green
Write-Host ""

Write-Host "`n📋 ДОПОЛНИТЕЛНИ ТЕСТОВИ:" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host ""
Write-Host "   📖 Прочитај: BULLETPROOF_TEST_GUIDE.md" -ForegroundColor White
Write-Host "   • Тест 2: Tab Close Recovery" -ForegroundColor Gray
Write-Host "   • Тест 3: Slow Network (3G)" -ForegroundColor Gray
Write-Host "   • Тест 4: Backend Crash" -ForegroundColor Gray
Write-Host ""

Write-Host "`n🚀 АВТОМАТСКО ОТВАРАЊЕ..." -ForegroundColor Magenta
Start-Sleep -Seconds 1

Start-Process "http://localhost:4321/student/quiz"

Write-Host ""
Write-Host "✨ СРЕЌНО ТЕСТИРАЊЕ! ✨" -ForegroundColor Green
Write-Host ""
Write-Host "Притисни Enter за излез..." -ForegroundColor DarkGray
$null = Read-Host

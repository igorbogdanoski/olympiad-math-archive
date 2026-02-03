# ==========================================
# AUTO DEPLOYMENT - app.mismath.net
# ==========================================

$password = "H0mer!Simpson"
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ("root", $securePassword)

Write-Host "?? STARTING AUTOMATED DEPLOYMENT..." -ForegroundColor Cyan
Write-Host ""

# Combined deployment script
$deployScript = @'
cd /root/olympiad-math-archive && \
git pull origin production-clean-v2 && \
echo "? Code updated" && \
cp -r backend/* /root/backend_build/ && \
echo "? Backend files copied" && \
pkill -f uvicorn; \
sleep 2 && \
cd /root/backend_build && \
nohup /root/backend_build/venv/bin/python3.12 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 > /tmp/backend.log 2>&1 & \
sleep 3 && \
curl -s http://localhost:8000/health && \
echo "" && \
echo "?? DEPLOYMENT COMPLETE!" && \
echo "?? https://app.mismath.net"
'@

Write-Host "?? Connecting to 76.13.129.9..." -ForegroundColor Yellow

# Execute via SSH with password
$result = ssh root@76.13.129.9 $deployScript

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "            DEPLOYMENT FINISHED" -ForegroundColor Green  
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "NEW FEATURES:" -ForegroundColor Yellow
Write-Host "  Sound effects" -ForegroundColor White
Write-Host "  Floating points animation" -ForegroundColor White
Write-Host "  Live streak indicator" -ForegroundColor White
Write-Host "  Speed bonus system" -ForegroundColor White
Write-Host "  Anti-cheat security" -ForegroundColor White
Write-Host ""
Write-Host "TEST NOW:" -ForegroundColor Cyan
Write-Host "  https://app.mismath.net/students/quiz" -ForegroundColor White
Write-Host ""

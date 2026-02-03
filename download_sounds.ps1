# Sound Download Script for Gamification System
# Downloads placeholder sounds for production deployment

$soundsDir = "web\public\sounds"

Write-Host ""
Write-Host "=== DOWNLOADING SOUND FILES FOR GAMIFICATION ===" -ForegroundColor Cyan
Write-Host "=" * 60
Write-Host ""

# Create directory if it doesn't exist
if (!(Test-Path $soundsDir)) {
    New-Item -ItemType Directory -Path $soundsDir -Force | Out-Null
    Write-Host "[OK] Created folder: $soundsDir" -ForegroundColor Green
} else {
    Write-Host "[OK] Folder already exists: $soundsDir" -ForegroundColor Green
}

Write-Host ""

# Sound file definitions (Using public CDN placeholder sounds)
$sounds = @{
    "click.mp3" = "https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample.mp3"
    "success.mp3" = "https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample2.mp3"
    "streak.mp3" = "https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample3.mp3"
}

# Fallback: Use local Windows system sounds if downloads fail
$windowsSounds = @{
    "click.mp3" = "C:\Windows\Media\Windows Background.wav"
    "success.mp3" = "C:\Windows\Media\tada.wav"
    "streak.mp3" = "C:\Windows\Media\Ring05.wav"
}

Write-Host "[INFO] Attempting to download sounds from internet..." -ForegroundColor Yellow
Write-Host ""

$downloadedCount = 0
$failedCount = 0

foreach ($sound in $sounds.Keys) {
    $outputPath = Join-Path $soundsDir $sound
    $url = $sounds[$sound]
    
    try {
        # Check if file already exists
        if (Test-Path $outputPath) {
            Write-Host "[SKIP] $sound already exists, skipping..." -ForegroundColor Gray
            $downloadedCount++
            continue
        }
        
        Write-Host "   Downloading: $sound..." -NoNewline
        
        # Try downloading from URL
        Invoke-WebRequest -Uri $url -OutFile $outputPath -TimeoutSec 10 -ErrorAction Stop
        
        # Verify file size
        $fileSize = (Get-Item $outputPath).Length
        if ($fileSize -gt 1KB) {
            Write-Host " [OK] Success ($([math]::Round($fileSize/1KB, 1)) KB)" -ForegroundColor Green
            $downloadedCount++
        } else {
            throw "File too small"
        }
        
    } catch {
        Write-Host " [FAIL] Failed" -ForegroundColor Red
        $failedCount++
        
        # Try copying from Windows sounds as fallback
        $windowsSound = $windowsSounds[$sound]
        if (Test-Path $windowsSound) {
            Write-Host "      [INFO] Using Windows sound as fallback..." -ForegroundColor Yellow
            try {
                Copy-Item -Path $windowsSound -Destination $outputPath -Force
                Write-Host "      [OK] Copied Windows sound: $([System.IO.Path]::GetFileName($windowsSound))" -ForegroundColor Green
                $downloadedCount++
                $failedCount--
            } catch {
                Write-Host "      [FAIL] Cannot copy Windows sound" -ForegroundColor Red
            }
        }
    }
}

Write-Host ""
Write-Host "=" * 60
Write-Host ""

# Summary
if ($downloadedCount -eq 3) {
    Write-Host "[SUCCESS] ALL SOUNDS READY! ($downloadedCount/3)" -ForegroundColor Green
    Write-Host ""
    Write-Host "[INFO] Location:" -ForegroundColor Cyan
    Write-Host "   $((Resolve-Path $soundsDir).Path)" -ForegroundColor White
    Write-Host ""
    Write-Host "[READY] System is FULLY PREPARED for production!" -ForegroundColor Green
    Write-Host ""
    Write-Host "[NEXT STEP]" -ForegroundColor Yellow
    Write-Host "   python backend/setup_production.py" -ForegroundColor White
    Write-Host ""
    
} elseif ($downloadedCount -gt 0) {
    Write-Host "[WARNING] PARTIALLY SUCCESSFUL ($downloadedCount/3)" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "System will work, but some sounds may be missing." -ForegroundColor Gray
    Write-Host ""
    Write-Host "[TIP] You can download manually from:" -ForegroundColor Cyan
    Write-Host "   - https://pixabay.com/sound-effects/search/click/" -ForegroundColor White
    Write-Host "   - https://pixabay.com/sound-effects/search/success/" -ForegroundColor White
    Write-Host ""
    
} else {
    Write-Host "[FAIL] DOWNLOAD FAILED (0/3)" -ForegroundColor Red
    Write-Host ""
    Write-Host "[PLAN B] Manual Download:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. Open: https://pixabay.com/sound-effects/" -ForegroundColor White
    Write-Host "2. Search: 'click', 'success', 'streak'" -ForegroundColor White
    Write-Host "3. Download MP3 files (short, <100KB)" -ForegroundColor White
    Write-Host "4. Place in: $soundsDir" -ForegroundColor White
    Write-Host ""
    Write-Host "[ALTERNATIVE] System works WITHOUT sounds!" -ForegroundColor Cyan
    Write-Host "   SoundManager has graceful degradation." -ForegroundColor Gray
    Write-Host ""
}

# List current files
Write-Host "[FOLDER CONTENTS]" -ForegroundColor Cyan
if (Test-Path $soundsDir) {
    $files = Get-ChildItem $soundsDir
    if ($files.Count -gt 0) {
        foreach ($file in $files) {
            $size = if ($file.Length -gt 1KB) { "$([math]::Round($file.Length/1KB, 1)) KB" } else { "$($file.Length) bytes" }
            Write-Host "   - $($file.Name) - $size" -ForegroundColor White
        }
    } else {
        Write-Host "   (Folder is empty)" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "=" * 60

# Offer to create placeholder silent files if nothing worked
if ($downloadedCount -eq 0) {
    Write-Host ""
    $response = Read-Host "Create empty placeholder files to avoid 404 errors? (Y/N)"
    if ($response -eq "Y" -or $response -eq "y") {
        Write-Host ""
        Write-Host "[INFO] Creating placeholder files..." -ForegroundColor Yellow
        
        # Create empty MP3 files (not valid audio, but prevents 404)
        foreach ($sound in $sounds.Keys) {
            $outputPath = Join-Path $soundsDir $sound
            if (!(Test-Path $outputPath)) {
                # Create minimal valid MP3 header (silent 1ms)
                $mp3Header = @(0xFF, 0xFB, 0x90, 0x00, 0x00, 0x00, 0x00, 0x00)
                [System.IO.File]::WriteAllBytes($outputPath, $mp3Header)
                Write-Host "   [OK] $sound (empty placeholder)" -ForegroundColor Gray
            }
        }
        
        Write-Host ""
        Write-Host "[SUCCESS] Placeholder files created!" -ForegroundColor Green
        Write-Host "   (No sound, but no 404 errors)" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "[DONE] Ready for next step! Type 'GOTOVO' to continue." -ForegroundColor Green
Write-Host ""

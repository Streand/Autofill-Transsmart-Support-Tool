# PowerShell script to remove autofill from Windows startup

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   Autofill Startup Removal" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

$startupFolder = [Environment]::GetFolderPath("Startup")
$shortcutPath = Join-Path $startupFolder "Autofill Transsmart Support Tool.lnk"

Write-Host "Checking for startup shortcut..." -ForegroundColor Yellow
Write-Host "Location: $shortcutPath" -ForegroundColor Gray
Write-Host ""

if (Test-Path $shortcutPath) {
    try {
        Remove-Item $shortcutPath -Force
        
        Write-Host "✓ SUCCESS: Autofill service removed from Windows startup!" -ForegroundColor Green
        Write-Host "✓ Will no longer start automatically on boot" -ForegroundColor Green
        Write-Host ""
        Write-Host "Note: Any currently running autofill service will continue" -ForegroundColor Yellow
        Write-Host "      until you close the command window manually." -ForegroundColor Yellow
        
    } catch {
        Write-Host "✗ ERROR: Failed to remove startup shortcut" -ForegroundColor Red
        Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
        Write-Host ""
        Write-Host "You can manually delete it from:" -ForegroundColor Yellow
        Write-Host "  $shortcutPath" -ForegroundColor Gray
    }
} else {
    Write-Host "ℹ INFO: No autofill startup shortcut found" -ForegroundColor Blue
    Write-Host "  Either it was already removed or never installed" -ForegroundColor Gray
    Write-Host ""
    Write-Host "To add to startup, run: setup_startup.ps1" -ForegroundColor Cyan
}

Write-Host ""
Read-Host "Press Enter to continue..."
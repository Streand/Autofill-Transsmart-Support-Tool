# PowerShell script to add autofill to Windows startup

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   Autofill Startup Setup" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

$currentDir = Get-Location
$batFile = Join-Path $currentDir "autofill_support_tool.bat"
$startupFolder = [Environment]::GetFolderPath("Startup")
$shortcutPath = Join-Path $startupFolder "Autofill Transsmart Support Tool.lnk"

if (Test-Path $batFile) {
    Write-Host "Found: $batFile" -ForegroundColor Yellow
    
    try {
        # Create WScript Shell object
        $WshShell = New-Object -ComObject WScript.Shell
        
        # Create shortcut
        $Shortcut = $WshShell.CreateShortcut($shortcutPath)
        $Shortcut.TargetPath = $batFile
        $Shortcut.WorkingDirectory = $currentDir
        $Shortcut.WindowStyle = 7  # Minimized window
        $Shortcut.Description = "Autofill Transsmart Support Tool - Auto Login Service"
        $Shortcut.Save()
        
        Write-Host ""
        Write-Host "✓ SUCCESS: Autofill service added to Windows startup!" -ForegroundColor Green
        Write-Host "✓ Will run minimized on next boot" -ForegroundColor Green
        Write-Host "✓ Shortcut created at:" -ForegroundColor Green
        Write-Host "  $shortcutPath" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "To remove later, run: remove_startup.ps1" -ForegroundColor Cyan
        
    } catch {
        Write-Host "✗ ERROR: Failed to create startup shortcut" -ForegroundColor Red
        Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    Write-Host "✗ ERROR: autofill_support_tool.bat not found in current directory" -ForegroundColor Red
    Write-Host "  Please run this script from the autofill project folder" -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Press Enter to continue..."
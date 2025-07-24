@echo off
cd /d "%~dp0"

REM Set window title
title Autofill Transsmart Support Tool - Auto Monitor

REM Display header
echo =========================================
echo    Autofill Transsmart Support Tool
echo         Auto Monitor Mode
echo =========================================
echo.

REM Check if virtual environment exists, if not create it
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements if needed (hide output)
pip install -r requirements.txt --quiet --disable-pip-version-check > nul 2>&1

REM Start monitoring
echo Starting automatic monitoring...
echo Monitoring for "Transsmart Support.exe" process...
echo This window will stay minimized and run in background.
echo.

REM Initialize variables
set "autofill_running=false"

:monitor_loop
REM Check if Transsmart Support Tool is running
tasklist /FI "IMAGENAME eq Transsmart Support.exe" 2>NUL | find /I "Transsmart Support.exe" >NUL

if %ERRORLEVEL%==0 (
    REM Process is running
    if "%autofill_running%"=="false" (
        echo [%DATE% %TIME%] Transsmart Support Tool detected! Starting autofill...
        set "autofill_running=true"
    )
    REM Run autofill silently
    python autofill_support_tool.py >NUL 2>&1
) else (
    REM Process is not running
    if "%autofill_running%"=="true" (
        echo [%DATE% %TIME%] Transsmart Support Tool closed. Stopping autofill...
        set "autofill_running=false"
    )
)

REM Wait 3 seconds before checking again
timeout /t 3 /nobreak >nul
goto monitor_loop


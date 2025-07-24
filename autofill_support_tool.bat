@echo off
cd /d "%~dp0"

title Autofill Transsmart Support Tool

echo =========================================
echo    Autofill Transsmart Support Tool
echo =========================================
echo.

if not exist "venv\" (
    echo Setting up environment...
    python -m venv venv
)

call venv\Scripts\activate.bat
pip install -r requirements.txt --quiet --disable-pip-version-check > nul 2>&1

echo Starting monitor service...
echo Waiting for Transsmart Support Tool...
echo.

set "autofill_running=false"
set "last_status=unknown"

:monitor_loop
tasklist /FI "IMAGENAME eq Transsmart Support.exe" 2>NUL | find /I "Transsmart Support.exe" >NUL

if %ERRORLEVEL%==0 (
    if "%autofill_running%"=="false" (
        echo [%TIME%] Process detected - Starting autofill service
        set "autofill_running=true"
        set "last_status=running"
    )
    python autofill_support_tool.py
) else (
    if "%autofill_running%"=="true" (
        echo [%TIME%] Process stopped - Autofill service disabled
        set "autofill_running=false"
        set "last_status=stopped"
    ) else (
        if not "%last_status%"=="waiting" (
            echo [%TIME%] Monitoring for Transsmart Support Tool...
            set "last_status=waiting"
        )
    )
)

timeout /t 3 /nobreak >nul
goto monitor_loop


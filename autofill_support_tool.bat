@echo off
cd /d "%~dp0"

REM Set window title
title Autofill Transsmart Support Tool

REM Display header
echo =========================================
echo    Autofill Transsmart Support Tool
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

REM Run the Python script in a loop
:loop
echo Waiting for Support Tool to start
python autofill_support_tool.py
timeout /t 5 /nobreak >nul
goto loop


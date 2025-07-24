# Support Tool Autofill

Automatically fills in your username and password when the Transsmart Support Tool login window appears.

## Setup Instructions

1. **Install Python** (if not already installed):
   - Download from https://www.python.org/downloads/release/python-31018/
   - **IMPORTANT**: Check "Add Python to PATH" during installation


2. **Configure your credentials**:
   - Edit `credentials.json` with your actual username and password
   - Save the file

3. **Start the autofill service**:
   - Double-click `autofill_support_tool.bat`
   - The service will automatically monitor for the Transsmart Support Tool
   - When the tool starts, autofill will activate automatically
   - Keep the command window open while working

4. **Optional: Auto-Start with Windows**:
   - Right-click `setup_startup.ps1` → "Run with PowerShell"
   - This will add the autofill service to Windows startup
   - The service will run minimized on every boot
   - To remove later, run `remove_startup.ps1`

## How It Works

- Monitors for "Transsmart Support.exe" process
- Automatically detects when Support Tool login window appears
- Fills credentials and waits for successful login
- Continues monitoring for subsequent logins

## Files

- `autofill_support_tool.py` - Main autofill script
- `autofill_support_tool.bat` - Process monitor and launcher
- `credentials.json` - Your username/password configuration
- `requirements.txt` - Python dependencies

## Auto-Start Management

**Method 1: Create Shortcut (Recommended)**
1. Right-click `autofill_support_tool.bat` → "Create shortcut"
2. Press `Win + R` → type `shell:startup` → Enter
3. Move the shortcut into the Startup folder
4. The service will start automatically on next boot

**To remove from startup:**
- Go to the Startup folder and delete the shortcut

**Note:** Don't copy the `.bat` file directly - use a shortcut instead so it can find the Python files.

## Security Note

Your credentials are stored locally in `credentials.json`. Keep this file secure and don't share it.

## Troubleshooting

- If Python is not found, make sure it's installed and added to PATH
- If autofill doesn't work, verify the login window title is "Support Tool Login"
- If process detection fails, check that "Transsmart Support.exe" is the correct process name
- To stop the service, close the command window or press Ctrl+C
- If startup scripts don't work, ensure PowerShell execution policy allows scripts

## System Requirements

- Windows OS
- Python 3.6 or higher
- Transsmart Support Tool application
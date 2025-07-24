# Support Tool Autofill

Automatically fills in your username and password when the Support Tool login window appears.

## Setup Instructions

1. **Install Python** (if not already installed):
   - Download from https://www.python.org/downloads/
   - **IMPORTANT**: Check "Add Python to PATH" during installation


2. **Configure your credentials**:
   - Open `credentials.json`
   - Replace `YOUR_USERNAME_HERE` with your username
   - Replace `YOUR_PASSWORD_HERE` with your password
   - Save the file

3. **Start the autofill service**:
   - Double-click `autofill_support_tool.bat`
   - Keep this window open while working
   - The script will automatically fill your credentials whenever the Support Tool login appears

## Files

- `autofill_support_tool.py` - Main script
- `autofill_support_tool.bat` - Launcher (creates virtual environment automatically)
- `setup.bat` - One-time setup
- `credentials.json` - Your username/password (created by setup)
- `requirements.txt` - Python dependencies

## Security Note

Your credentials are stored locally in `credentials.json`. Keep this file secure and don't share it.

## Troubleshooting

- If Python is not found, make sure it's installed and added to PATH
- If the autofill doesn't work, check that the window title is exactly "Support Tool Login"
- To stop the service, close the command window or press Ctrl+C
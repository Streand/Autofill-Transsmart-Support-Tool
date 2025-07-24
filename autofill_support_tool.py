# Save as autofill_support_tool.py

import os
import sys
import subprocess
import time
import json
import pyautogui
import pygetwindow as gw


def ensure_venv():
    venv_dir = os.path.join(os.path.dirname(__file__), "venv")
    if not os.path.isdir(venv_dir):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    # Activate venv for subprocesses (not current process)
    activate_this = os.path.join(venv_dir, "Scripts", "activate_this.py")
    if os.path.isfile(activate_this):
        with open(activate_this) as f:
            exec(f.read(), {'__file__': activate_this})

ensure_venv()

def load_credentials():
    credentials_file = os.path.join(os.path.dirname(__file__), "credentials.json")
    print(f"DEBUG: Looking for credentials at: {credentials_file}")  # Debug line
    try:
        with open(credentials_file, 'r') as f:
            creds = json.load(f)
            username = creds.get("username")
            password = creds.get("password")
            print(f"DEBUG: Loaded username: {username}")  # Debug line
            print(f"DEBUG: Password length: {len(password) if password else 0}")  # Debug line
            return username, password
    except FileNotFoundError:
        print("Error: credentials.json file not found!")
        return None, None
    except json.JSONDecodeError:
        print("Error: Invalid JSON in credentials.json!")
        return None, None

USERNAME, PASSWORD = load_credentials()
WINDOW_TITLE = "Support Tool Login"

def wait_for_window(title, timeout=60):
    for _ in range(timeout * 2):
        windows = gw.getWindowsWithTitle(title)
        if windows:
            return windows[0]
        time.sleep(0.5)
    return None

def wait_for_window_to_disappear(title, timeout=30):
    """Wait for window to disappear after successful login"""
    for _ in range(timeout * 2):
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            print("login successful!")
            return True
        time.sleep(0.5)
    return False

def autofill():
    if not USERNAME or not PASSWORD:
        print("Credentials not loaded. Please check credentials.json file.")
        print(f"DEBUG: USERNAME = {USERNAME}")  # Debug line
        print(f"DEBUG: PASSWORD = {PASSWORD}")  # Debug line
        return False
        
    # Silently check for window (no print while waiting)
    win = wait_for_window(WINDOW_TITLE, timeout=1)  # Very short timeout for silent check
    if not win:
        return False  # No print, just return False
    
    print("Support tool started, Filling credentials")
    print(f"DEBUG: About to type username: {USERNAME}")  # Debug line
    win.activate()
    time.sleep(0.5)
    
    # Clear any existing text first
    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.typewrite(USERNAME)
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')  # Select all in password field
    pyautogui.typewrite(PASSWORD)
    print("Credentials filled successfully!")
    
    # Wait for window to disappear (silently)
    if wait_for_window_to_disappear(WINDOW_TITLE, timeout=60):
        return True
    else:
        # Wait indefinitely for window to disappear before continuing (no messages)
        while True:
            windows = gw.getWindowsWithTitle(WINDOW_TITLE)
            if not windows:
                print("Login window disappeared - login successful!")
                return True
            time.sleep(2)

if __name__ == "__main__":
    first_run = True
    while True:
        # Silently check for window first
        win = wait_for_window(WINDOW_TITLE, timeout=1)
        if win:
            if not first_run:
                print("." * 80)  # Add separator line before subsequent logins
            first_run = False
            autofill()
        time.sleep(3)  # Check every 3 seconds for new login windows
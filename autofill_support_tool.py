import os
import sys
import subprocess
import time
import json
import pyautogui
import pygetwindow as gw


def ensure_venv():
    """Ensure virtual environment exists and is activated"""
    venv_dir = os.path.join(os.path.dirname(__file__), "venv")
    if not os.path.isdir(venv_dir):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    
    activate_this = os.path.join(venv_dir, "Scripts", "activate_this.py")
    if os.path.isfile(activate_this):
        with open(activate_this) as f:
            exec(f.read(), {'__file__': activate_this})


def load_credentials():
    """Load username and password from credentials.json"""
    credentials_file = os.path.join(os.path.dirname(__file__), "credentials.json")
    try:
        with open(credentials_file, 'r') as f:
            creds = json.load(f)
            return creds.get("username"), creds.get("password")
    except (FileNotFoundError, json.JSONDecodeError):
        return None, None


def wait_for_window(title, timeout=60):
    """Wait for window with specified title to appear"""
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
            print("Authentication successful")
            return True
        time.sleep(0.5)
    return False


def autofill(show_separator=False):
    """Main autofill function"""
    if not USERNAME or not PASSWORD:
        print("Error: Authentication credentials not loaded")
        return False
        
    win = wait_for_window(WINDOW_TITLE, timeout=1)
    if not win:
        return False
    
    # Show separator before starting autofill (not after)
    if show_separator:
        print("." * 60)
    
    print("Login window detected - Authenticating...")
    win.activate()
    time.sleep(0.5)
    
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(USERNAME)
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(PASSWORD)
    print("Credentials submitted")
    
    if wait_for_window_to_disappear(WINDOW_TITLE, timeout=60):
        return True
    else:
        while True:
            windows = gw.getWindowsWithTitle(WINDOW_TITLE)
            if not windows:
                print("Authentication successful")
                return True
            time.sleep(2)


# Initialize
ensure_venv()
USERNAME, PASSWORD = load_credentials()
WINDOW_TITLE = "Support Tool Login"

if __name__ == "__main__":
    session_count = 0
    while True:
        if autofill(show_separator=session_count > 0):
            session_count += 1
        time.sleep(3)
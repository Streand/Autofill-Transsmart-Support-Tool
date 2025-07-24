import psutil
import subprocess
import time
import os

PROCESS_NAME = "Transsmart Support.exe"
BATCH_FILE = os.path.join(os.path.dirname(__file__), "autofill_support_tool.bat")

def is_process_running(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() == process_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False

def monitor_process():
    print("=========================================")
    print("   Transsmart Support Tool Monitor")
    print("=========================================")
    print()
    print("Monitoring for Transsmart Support Tool...")
    
    batch_process = None
    
    while True:
        try:
            if is_process_running(PROCESS_NAME):
                if batch_process is None:
                    print("Transsmart Support Tool detected! Starting autofill...")
                    batch_process = subprocess.Popen(BATCH_FILE, shell=True)
            else:
                if batch_process is not None:
                    print("Transsmart Support Tool closed. Stopping autofill...")
                    batch_process.terminate()
                    batch_process = None
            
            time.sleep(2)
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
            if batch_process:
                batch_process.terminate()
            break

if __name__ == "__main__":
    monitor_process()
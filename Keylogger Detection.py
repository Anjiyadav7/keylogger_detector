import psutil
import pygetwindow as gw
import os
import time

# Common keylogger process names (expand list as needed)
SUSPICIOUS_PROCESSES = ["keylogger", "spyware", "hook", "record", "logger"]

def detect_suspicious_processes():
    print("🔍 Scanning for keyloggers...\n")
    suspicious_found = False
    
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_name = process.info['name'].lower()
            for keyword in SUSPICIOUS_PROCESSES:
                if keyword in process_name:
                    print(f"⚠️ Suspicious Process Found: {process.info['name']} (PID: {process.info['pid']})")
                    suspicious_found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if not suspicious_found:
        print("✅ No suspicious keylogger processes detected.")

def detect_keyboard_hooks():
    print("\n🔍 Checking for suspicious keyboard hooks...\n")
    
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            print(f"🖥️ Active Window: {active_window.title}")
        else:
            print("⚠️ Could not detect the active window.")
    except Exception as e:
        print(f"⚠️ Error detecting active window: {e}")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clears terminal screen
        print("🔒 Keylogger Detector 🔒\n")
        
        detect_suspicious_processes()
        detect_keyboard_hooks()
        
        print("\n🔄 Scanning again in 30 seconds...")
        time.sleep(30)

if __name__ == "__main__":
    main()

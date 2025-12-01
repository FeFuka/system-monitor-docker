import requests
from datetime import datetime

URL = "http://localhost:8000"
LOG_FILE = "uptime.log"

def check_status():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            if "PostgreSQL" in response.text:
                status = "SUCCESS!"
                message = "System Online and Database Connected"
            else:
                status = "ALERT"
                message = "App Online, Database not found"
        else:
            status = "ERROR"
            message = f"Unexpected Status Code: {response.status_code}"
    except Exception as e:
        status = "CRITIC"
        message = f"Web Server out: {str(e)}"

    log_line = f"[{timestamp}] {status}: {message}\n"

    
    with open(LOG_FILE, "a") as f:
        f.write(log_line)
    print(log_line.strip())

if __name__ == "__main__":
    check_status()

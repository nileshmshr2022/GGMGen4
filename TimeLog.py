import os
import schedule
import time
from datetime import datetime

def log_system_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "system_time_log.txt")
    with open(log_path, "a") as log_file:
        log_file.write(f"{current_time}\n")
    print(f"Logged system time: {current_time}")

# Schedule the function to run every hour
schedule.every().hour.do(log_system_time)

while True:
    schedule.run_pending()
    time.sleep(1)

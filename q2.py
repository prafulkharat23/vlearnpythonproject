import psutil
import time
import sys

# Set CPU usage threshold (in %)
THRESHOLD = 80

def monitor_cpu():
    print(" Starting CPU monitoring... Press Ctrl+C to stop.\n")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU Usage: {cpu_usage}%")

            if cpu_usage > THRESHOLD:
                print(f" ALERT: CPU usage has exceeded {THRESHOLD}%!")

            time.sleep(1)  # wait for 1 second before next check

    except KeyboardInterrupt:
        print("\n Monitoring stopped by user.")
        sys.exit(0)

    except Exception as e:
        print(f" Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    monitor_cpu()

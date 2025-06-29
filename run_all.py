# run_all.py

import threading
import subprocess
import time

def run_scheduler():
    print("🕒 Starting scheduler.py...")
    subprocess.run(["python", "scheduler.py"])

def run_bot_server():
    print("🤖 Starting bot_server.py...")
    subprocess.run(["python", "bot_server.py"])

# Create two threads
t1 = threading.Thread(target=run_scheduler)
t2 = threading.Thread(target=run_bot_server)

# Start both
t1.start()
t2.start()

# Optional: wait for both to finish (blocks main thread)
t1.join()
t2.join()

print("✅ Both processes are running in parallel.")

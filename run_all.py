import threading
import subprocess

def run_scheduler():
    print("🕒 Starting scheduler.py...")
    subprocess.run(["python", "scheduler.py"])

def run_upload_server():
    print("🌐 Starting upload_server.py...")
    subprocess.run(["python", "upload_server.py"])

def run_bot_server():
    print("🤖 Starting bot_server.py...")
    subprocess.run(["python", "bot_server.py"])

# Start all 3 in parallel
t1 = threading.Thread(target=run_scheduler)
t2 = threading.Thread(target=run_upload_server)
t3 = threading.Thread(target=run_bot_server)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

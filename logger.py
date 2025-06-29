import csv
from datetime import datetime
import os

def log_alerts(alerts,method='unknown'):
    file = "alert_log.csv"
    file_exists = os.path.isfile(file)
    with open(file,'a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['Timestamp',"Coin","Price","Method"])
        for coin,price in alerts:
            writer.writerow([datetime.now().isformat(),coin,price,method])

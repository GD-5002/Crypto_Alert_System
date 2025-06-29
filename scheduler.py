import schedule
import time
import json
import os
import asyncio

from api import get_simple_price
from alerts import check_price_alerts
from config import CURRENCY
from notifier import send_email_alert
from telegram_bot import send_telegram_alert_async
from spike import detect_spikes
from logger import log_alerts

# Load alert configuration
def load_alert_config():
    try:
        if not os.path.exists("alert_config.json"):
            print("❌ No alert configuration found. Please run main.py or the Streamlit UI first.")
            return None, None, None

        with open("alert_config.json", "r") as f:
            config = json.load(f)
            email = config.get("email")
            chat_id = config.get("telegram_chat_id")
            alerts = config.get("alerts")
            return email, chat_id, alerts

    except Exception as e:
        print(f"⚠️ Error loading alert config: {e}")
        return None, None, None

# Main alert execution job
def run_alert_job():
    try:
        email, chat_id, alert_config = load_alert_config()
        if not alert_config:
            print("❗ Missing alerts in configuration.")
            return

        coin_ids = list(alert_config.keys())
        prices = get_simple_price(coin_ids, currency=CURRENCY)
        print("📊 Current Prices Fetched:", prices)

        if prices:
            # Check price-based alerts
            range_alerts = check_price_alerts(prices, alert_config)

            # Check spike-based alerts
            spikes = detect_spikes(prices, alert_config)
            spike_alerts = [(coin, price) for coin, price, _ in spikes]

            if spikes:
                for coin, price, percent in spikes:
                    print(f"🚀 SPIKE DETECTED: {coin.upper()} moved {percent:.2f}% → now ${price}")

            # Combine all alerts (range + spike)
            all_alerts = range_alerts + spike_alerts

            if all_alerts:
                for coin, price in all_alerts:
                    print(f"🚨 ALERT: {coin.upper()} is within range at ${price}")

                method_used = ""
                if email:
                    send_email_alert(email, all_alerts)
                    method_used += "email"

                if chat_id:
                    asyncio.run(send_telegram_alert_async(chat_id, all_alerts))
                    method_used += "+telegram" if method_used else "telegram"

                log_alerts(all_alerts, method=method_used)
            else:
                print("✅ No alerts triggered at this time.")
        else:
            print("⚠️ Failed to fetch prices.")

    except Exception as e:
        print(f"❌ Error during alert check: {e}")

# Schedule it every 10 minutes
schedule.every(10).minutes.do(run_alert_job)
print("🕒 Crypto Alert Scheduler is running... (Press Ctrl+C to stop)")

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Scheduler stopped by user.")
        break
    except Exception as e:
        print(f"⚠️ Scheduler error: {e}")
        time.sleep(5)

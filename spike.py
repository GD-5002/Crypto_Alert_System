import json
import os

PRICE_HISTORY_FILE = "price_history.json"

def load_price_history():
    if os.path.exists(PRICE_HISTORY_FILE):
        with open(PRICE_HISTORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_price_history(history):
    with open(PRICE_HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def detect_spikes(current_prices, alert_config):
    spikes = []
    price_history = load_price_history()

    for coin, current_data in current_prices.items():
        current_price = current_data["usd"]
        config = alert_config.get(coin)
        spike_threshold = config.get("spike_percent", None)

        # ✅ Only detect spikes if threshold is set and positive
        if spike_threshold is not None and spike_threshold > 0:
            old_price = price_history.get(coin)
            if old_price:
                change_percent = abs((current_price - old_price) / old_price * 100)
                if change_percent >= spike_threshold:
                    spikes.append((coin, current_price, change_percent))

        # ✅ Always update price history even if no spike
        price_history[coin] = current_price

    save_price_history(price_history)
    return spikes

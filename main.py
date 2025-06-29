# main.py

import json
from api import get_simple_price, get_supported_coins, get_trending_coins
from alerts import check_price_alerts
from config import CURRENCY

def list_supported_coins_paginated():
    try:
        coins = get_supported_coins()
        if not coins:
            print("Could not fetch coin list.")
            return

        page_size = 100
        total = len(coins)
        pages = (total + page_size - 1) // page_size

        print("\nAll Supported Coins (100 per page):")
        for i in range(pages):
            start = i * page_size
            end = min(start + page_size, total)
            print(f"\nPage {i + 1}/{pages}")
            for coin in coins[start:end]:
                print(f"- {coin['id']} ({coin['symbol']})")

            if i < pages - 1:
                proceed = input("\nPress Enter to view next page, or type 'q' to quit: ").strip().lower()
                if proceed == 'q':
                    break
    except Exception as e:
        print(f"Error listing supported coins: {e}")

def show_trending_coins():
    try:
        print("\nTrending Coins (via CoinGecko):")
        trending = get_trending_coins()
        coins = trending.get('coins', [])
        if coins:
            for item in coins:
                coin = item['item']
                print(f"- {coin['name']} ({coin['symbol']}) - Rank #{coin['market_cap_rank']}")
        else:
            print("Could not fetch trending coins.")
    except Exception as e:
        print(f"Error fetching trending coins: {e}")

def run_alert_system():
    try:
        print("\n🔧 Welcome to the Crypto Alert Setup\n")

        alert_config = {}
        n = int(input("💰 How many coins do you want to track? "))
        for _ in range(n):
            coin = input("Enter coin ID (e.g., bitcoin): ").strip().lower()
            min_price = float(input(f"📉 Minimum alert price for {coin}: "))
            max_price = float(input(f"📈 Maximum alert price for {coin}: "))
            spike_input = input(f"📈 Spike % alert for {coin} (e.g., 5 for 5%, or leave blank to skip): ").strip()

            alert_config[coin] = {
                'min': min_price,
                'max': max_price
            }

            if spike_input:
                try:
                    spike_percent = float(spike_input)
                    alert_config[coin]['spike_percent'] = spike_percent
                except ValueError:
                    print("⚠️ Invalid spike % — skipping for this coin.")

        print("\n📨 Email Alerts Setup:")
        email = input("Enter your email address (or press Enter to skip): ").strip()

        print("\n📲 Telegram Alerts Setup:")
        print("👉 Step 1: Open the Telegram app")
        print("👉 Step 2: Search for your bot (e.g., @CryptoCurrencyAlertBot)")
        print("👉 Step 3: Press 'Start' and send any message (e.g., Hello)")
        print("👉 Step 4: To find your Telegram Chat ID, message @userinfobot")
        chat_id = input("Enter your Telegram Chat ID (or press Enter to skip): ").strip()

        config_data = {
            "email": email if email else None,
            "telegram_chat_id": chat_id if chat_id else None,
            "alerts": alert_config
        }

        with open("alert_config.json", "w") as f:
            json.dump(config_data, f, indent=2)

        print("\n✅ Alert configuration saved successfully to 'alert_config.json'.")
        print("ℹ️ You can now run 'scheduler.py' or 'run_all.py' to receive alerts.")

        # Optional test message
        if chat_id:
            try:
                from telegram import Bot
                from telegram_bot import TELEGRAM_TOKEN
                bot = Bot(token=TELEGRAM_TOKEN)
                bot.send_message(chat_id=chat_id, text="✅ Telegram alert setup successful!")
                print("✅ Telegram test message sent.")
            except Exception as e:
                print("⚠️ Failed to send test Telegram message. Make sure you've messaged the bot first.")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values for prices.")
    except Exception as e:
        print(f"❌ Unexpected error during alert setup: {e}")

def main():
    print("Welcome to the Crypto Watcher Tool")
    print("\nPlease select a function:")
    print("1. Coin Listings")
    print("2. Trending Coins")
    print("3. Coin Alerting System")

    try:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == '1':
            list_supported_coins_paginated()
        elif choice == '2':
            show_trending_coins()
        elif choice == '3':
            run_alert_system()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    except Exception as e:
        print(f"Error in main menu: {e}")

if __name__ == "__main__":
    main()

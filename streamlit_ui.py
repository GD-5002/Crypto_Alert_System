import streamlit as st
import json
import requests
from telegram import Bot
from telegram_bot import TELEGRAM_TOKEN

# ✅ Use your actual Railway backend here
RAILWAY_BACKEND_URL = "https://prolific-generosity.up.railway.app/upload"
CONFIG_FILE = "alert_config.json"

st.set_page_config(page_title="Crypto Alert Configurator", page_icon="📊")
st.title("📊 Crypto Alert System Setup")
st.markdown("Configure your coin alerts and send them to the backend alert engine.")

# ✅ Manual coin input (user-defined)
user_input = st.text_input(
    "🪙 Enter coin IDs to track (comma-separated, e.g. bitcoin, ethereum):"
)
selected_coins = [coin.strip().lower() for coin in user_input.split(",") if coin.strip()]

alerts = {}

for coin in selected_coins:
    st.subheader(f"⚙️ Alert Settings for `{coin}`")
    min_price = st.number_input(f"Minimum price for {coin}", min_value=0.0, step=1.0, key=f"min_{coin}")
    max_price = st.number_input(f"Maximum price for {coin}", min_value=0.0, step=1.0, key=f"max_{coin}")
    spike = st.text_input(f"Spike alert % for {coin} (optional)", placeholder="e.g., 5", key=f"spike_{coin}")

    if min_price == 0.0 and max_price == 0.0:
        st.warning(f"⚠️ You must enter at least a min or max price for {coin}")
        continue

    coin_alert = {"min": min_price, "max": max_price}

    if spike.strip():
        try:
            spike_val = float(spike)
            if spike_val > 0:
                coin_alert["spike_percent"] = spike_val
        except ValueError:
            st.warning(f"⚠️ Invalid spike value for {coin}, skipping spike.")

    alerts[coin] = coin_alert

# 📧 Email and Telegram Setup
st.subheader("📨 Email Alerts")
email = st.text_input("Your email address", placeholder="you@example.com")

st.subheader("📲 Telegram Alerts")
chat_id = st.text_input("Your Telegram chat ID")

# 💾 Save & Upload
if st.button("💾 Save & Upload Alert Configuration"):
    if not selected_coins:
        st.warning("⚠️ Please enter at least one coin ID.")
    elif not alerts:
        st.warning("⚠️ Valid price alert details are required.")
    else:
        config = {
            "email": email if email else None,
            "telegram_chat_id": chat_id if chat_id else None,
            "alerts": alerts
        }

        try:
            # Save config locally
            with open(CONFIG_FILE, "w") as f:
                json.dump(config, f, indent=2)
            st.success("✅ Configuration saved locally.")

            # 📲 Optional Telegram test
            if chat_id:
                try:
                    bot = Bot(token=TELEGRAM_TOKEN)
                    bot.send_message(chat_id=chat_id, text="✅ Telegram alert setup successful!")
                    st.success("📲 Telegram test message sent.")
                except Exception:
                    st.warning("⚠️ Failed to send Telegram test message. Did you message the bot first?")

            # 🌐 Upload config to Railway backend
            try:
                res = requests.post(RAILWAY_BACKEND_URL, json=config)
                if res.status_code == 200:
                    st.success("🚀 Configuration uploaded to alert engine successfully!")
                else:
                    st.warning(f"⚠️ Upload failed: {res.status_code} - {res.text}")
            except Exception as e:
                st.error(f"❌ Failed to send config to backend: {e}")

            # 📥 Download config
            st.download_button(
                label="⬇️ Download alert_config.json",
                data=json.dumps(config, indent=2),
                file_name="alert_config.json",
                mime="application/json"
            )

        except Exception as e:
            st.error(f"❌ Error saving configuration: {e}")

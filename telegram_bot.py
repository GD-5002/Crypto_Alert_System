# telegram_bot.py

import asyncio
from telegram import Bot

TELEGRAM_TOKEN = "8144948345:AAGl6E57rcl4ND1i4Bjm2S35m4afqdkAjzI"

async def send_telegram_alert_async(chat_id, alerts):
    try:
        bot = Bot(token=TELEGRAM_TOKEN)
        for coin, price in alerts:
            message = f"🔔 ALERT: {coin.upper()} is within your range at ${price}"
            await bot.send_message(chat_id=chat_id, text=message)
        print(f"✅ Telegram alert sent to {chat_id}")
    except Exception as e:
        print(f"❌ Telegram alert failed: {e}")

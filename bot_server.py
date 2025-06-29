# bot_server.py

import json
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from api import get_simple_price

# Load alert config
with open("alert_config.json", "r") as f:
    config = json.load(f)

TELEGRAM_TOKEN = "8144948345:AAGl6E57rcl4ND1i4Bjm2S35m4afqdkAjzI"
ALLOWED_CHAT_ID = int(config.get("telegram_chat_id"))
ALERT_COIN_IDS = list(config["alerts"].keys())
CURRENCY = "usd"

# /status command handler
def status_command(update: Update, context: CallbackContext):
    user_id = update.effective_chat.id
    if user_id != ALLOWED_CHAT_ID:
        update.message.reply_text("⛔ Unauthorized access.")
        return

    try:
        prices = get_simple_price(ALERT_COIN_IDS, currency=CURRENCY)
        msg = "📊 *Current Crypto Prices:*\n"
        for coin, data in prices.items():
            msg += f"• `{coin}`: ${data['usd']}\n"
        update.message.reply_text(msg, parse_mode="Markdown")
    except Exception as e:
        update.message.reply_text("⚠️ Failed to fetch prices.")

# /help command
def help_command(update: Update, context: CallbackContext):
    if update.effective_chat.id != ALLOWED_CHAT_ID:
        return
    update.message.reply_text(
        "🤖 *Crypto Bot Commands:*\n"
        "/status - Show current crypto prices\n"
        "/help - Show this help message",
        parse_mode="Markdown"
    )

# Main bot logic
def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("status", status_command))
    dp.add_handler(CommandHandler("help", help_command))

    print("✅ Bot is running... Send /status in Telegram to test.")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

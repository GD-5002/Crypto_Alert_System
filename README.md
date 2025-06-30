# 🧠 Real-Time Crypto Alerting System (Python + APIs)

A real-time cryptocurrency alerting system built entirely in **Python**, using live data from the [CoinGecko API](https://www.coingecko.com/), with automated **Telegram** and **Email** notifications. Designed for users who want to track crypto prices without relying on heavy apps or dashboards.

---

## 🚀 Features

- 💰 **Track Any Coin** by ID (e.g., bitcoin, ethereum)
- 📉 **Price Range Alerts** — get notified when a coin enters a specified price range
- 📈 **Spike Detection Alerts** — alerts for sudden price changes beyond a user-defined %
- 📬 **Email Notifications** — configured via SMTP
- 🤖 **Telegram Bot Integration** — receive alerts and use `/status` command to check live prices
- 📄 **Streamlit UI** for setting preferences (no coding needed!)
- ☁️ **Deployed backend using Railway** — no local runtime required

---

## 🧰 Tech Stack (Not Full-Stack)

| Component         | Description                              |
|------------------|------------------------------------------|
| **Python**        | Core logic, alerting engine              |
| **CoinGecko API** | Live cryptocurrency price data           |
| **SMTP**          | Email alert integration                  |
| **Telegram Bot**  | Real-time user alerts & interaction      |
| **Streamlit**     | Lightweight UI for alert configuration   |
| **Railway**       | Cloud-hosted backend                     |

---

## 🖥 How It Works

1. **User configures alerts** (Streamlit UI or locally)
2. The system:
   - Pulls live prices from CoinGecko every 10 mins
   - Detects price range matches or spike %
   - Sends alerts via Email and/or Telegram
3. Telegram bot also responds to `/status` for live checking

---

## 🧪 Demo (If public)

> 🔗 Streamlit App: [your-streamlit-link-here]  
> 🔗 Telegram Bot: `@YourBotName`  
> 🔗 GitHub Repo: [your-repo-link-here]

---

## 🛠 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/crypto-alert-system.git
cd crypto-alert-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run full engine (scheduler + bot server)
python run_all.py

# Optional: Launch only the config UI
streamlit run streamlit_ui.py

🤖 Telegram Bot Setup (Once)
Go to @BotFather → create new bot → get your token

Add token in telegram_bot.py

Start a chat with your bot

Use @userinfobot to get your Telegram chat ID


📬 Email Setup (Optional)
Configure your Gmail or SMTP email address in notifier.py

App passwords recommended for Gmail

🧠 Why This Project
No heavy web stack — built by a backend + data enthusiast

Real-world use case for crypto traders and hobbyists

Designed for low maintenance: configure once, let it run

🧑‍💻 Author
Dheeraj Gogula
🎓 B.Tech Student, NIT Durgapur
💡 Python, APIs, Deep Learning, Automation
📧 dheerajgogula05@gmail.com

📄 License
This project is licensed under the MIT License.
Feel free to fork, adapt, and use!

⭐️ Support
If you liked this project:

⭐️ Star this repo

🐛 Report issues

🍴 Fork and improve it

🗣 Share it with friends

⚠️ Note: This is not a web development project. Built entirely using Python, with real-world deployment and automation features for alerting systems.

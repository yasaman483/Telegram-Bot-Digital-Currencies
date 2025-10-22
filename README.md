# Telegram Bot - Digital Currencies
A simple Telegram bot that displays **real-time cryptocurrency prices**. Users can choose a coin and instantly recieve live price updates (@Digital_currencies_a_bot)

# Version 1: Local execution
If you want to run the bot manually on your system (ideal for development or texting):
1. Clone the repository:
```
git clone https://github.com/yasaman483/Telegram-Bot-Digital-Currencies.git  
cd Telegram-Bot-Digital-Currencies
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Create a `.env` file (or set environment variables) with your Telegram Bot token and optionally proxy settings:
```
BOT_TOKEN=your_telegram_bot_token  
PROXY=your_proxy_if_needed
```   
# Notes:
If you are using a proxy, it helps the bot to connect to Telegram servers more reliably (specially if Telegram is restricted in your region)
4. Run the bot locally.

# Version 2: Deployed on Vercel
The bot is also deployed on Vercel and runs 24/7 without requiring you to keep your local machine online. Simply use the bot via its Telegram interface.
With this version:
* You don't need to run the script locally.
* Updates can be done via Github and Vercel deployment.
* Ideal for production/live usage.

# Features
- Displays live prices of top cryptocurrencies.
- Build with telbot **[pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI)**
- Optional proxy support for better Telegram connectivity.
- Users can select a coin name and receive instant updates.
- Two execution models: local (for dev) and deployed (for production).

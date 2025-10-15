Telegram Crypto Bot
A simple Telegram bot that displays **real-time cryptocurrency prices**. Users can choose a coin and instantly recieve live price updates.

# Features
- Displays live prices of top cryptocurrencies
- Build with telbot **[pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI)**
- Optional proxy support for better Telegram connectivity.

# Run locally
1. Clone this repository.
2. Install dependencies
   `
   pip install -r requirements.txt
   `
3. Create a '.env' file in the root directory with your own telegram bot token and if you use proxy, include it as well:
   ` BOT_TOKEN='your_bot_token' `
   ` PROXY='your_proxy' `
4. Run the bot:
   'Python crypto_bot.py'
   
# Notes:
If you are using a proxy, it helps the bot to connect to Telegram servers more reliably (specially if Telegram is restricted in your region)
If you don't need the proxy, simply remove the related code lines.

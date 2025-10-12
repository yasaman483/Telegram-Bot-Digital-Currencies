import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BOT_TOKEN')
proxy = os.getenv('PROXY')
URL = 'https://api.binance.com/api/v3/ticker/price'

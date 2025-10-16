import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('BOT_TOKEN')
proxy = os.getenv('PROXY')
URL='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1'

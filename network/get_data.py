import logging
from config import URL, proxy
from telebot import asyncio_helper
asyncio_helper.proxy = proxy
import aiohttp
from aiohttp_socks import ProxyConnector
import time

fetch_time = 0
data = None
session = None

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

async def get_data():
    """
    Get data from Binance.
    """
    global fetch_time, data

    if time.time() - fetch_time < 120 and data is not None:
        return data

    try:
        global session
        if not session:
            connector = ProxyConnector.from_url(proxy)
            session = aiohttp.ClientSession(connector=connector)

        async with session.get(URL) as response:
            if response.status != 200:
                logging.error(f'Get bad response with {response.status} status.')
                return None
            data = await response.json()
            fetch_time = time.time()
            logging.info('Data created.')
            return data
    except RuntimeError as e:
        logging.error(f'Find runtime error: {e}')
    except Exception as e:
        logging.error(f'Find an error while fetching datas: {e}')
        return None

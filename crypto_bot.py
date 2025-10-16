import logging
from config import token
from telebot.async_telebot import AsyncTeleBot
import asyncio
import platform
if platform.system() == 'windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from handlers import default_handlers, currency_handlers

logger = logging.getLogger(__name__)

currencies = {'Bitcoin': 'BTC',
              'Litecoin': 'LTC',
              'Dogecoin': 'DOGE',
              'Ripple': 'XRP',
              'Dash': 'DASH',
              'NEO': 'NEO',
              'Monero': 'XMR',
              'Verge': 'XVG',
              'Stellar': 'XLM',
              'Ethereum': 'ETH',
              'Ethereum Classic': 'ETC',
              'Nano': 'XNO',
              'Firo': 'FIRO',
              'Zcash': 'ZEC',
              'Bitcoin Cash': 'BCH',
              'EOS.IO': 'EOS',
              'Cardano': 'ADA',
              'Tron': 'TRX',
              'Nervos Network': 'CKB',
              'Algorand': 'ALGO',
              'Avalanche': 'AVAX',
              'Shiba lnu': 'SHIB',
              'Polkadot': 'DOT',
              'Solana': 'SOL',
              'Binance Coin': 'BNB',
              'USDC': 'USDC',
              'Polygon': 'MATIC',
              'Chainlink': 'LINK',
              'Toncoin': 'TON',
              'Arbitrum': 'ARB',
              'Sui': 'SUI',
              'Hedera': 'HBAR',
              'Dai': 'DAI',
              'Uniswap': 'UNI',
              'World Liberty Financial': 'WLFI',
              'Aave': 'AAVE',
              'Ethena': 'ENA',
              'Pepe': 'PEPE',
              'Aptos': 'APT',
              'Bittensor': 'TAO',
              'Ondo': 'ONDO',
              'Worldcoin': 'WLD',
              'Internet Computer': 'ICP',
              'Cosmos': 'ATOM'}


def create_bot():
    """
    Create the bot.
    :return: telebot.async_telebot.AsyncTeleBot
    """
    try:
        bot = AsyncTeleBot(token)
        logger.info(f'Bot created with token.')
        default_handlers.register(bot, currencies)
        currency_handlers.register(bot, currencies)
        logger.info('Registers activate.')
        return bot
    except Exception as e:
        logger.error(f'Exception: {e}')


async def main():
    """
    Start the bot.
    """
    bot = create_bot()
    await bot.infinity_polling()


if __name__ == "__main__":
    asyncio.run(main())

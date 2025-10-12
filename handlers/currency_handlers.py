import telebot
from config import proxy
from telebot import asyncio_helper
asyncio_helper.proxy = proxy
from network.get_data import get_data


def register(bot, currencies):
    async def make_markup(message):
        """
        Make buttons if the message of user isn't recognize.
        :param message:
        """
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
        markup.add('Back to the currencies.')
        await bot.reply_to(message, "Can't find your chosen currency.", reply_markup=markup)

    @bot.message_handler(func=lambda m: m.text == 'Back to the currencies.')
    async def back_to_the_currencies(message):
        new_markup = telebot.types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
        new_markup.add(*currencies.keys())
        await bot.send_message(message.chat.id, 'Choose a currency:', reply_markup=new_markup)

    @bot.message_handler(func=lambda m: m.text != 'Back to the currencies.')
    async def response_to_message(message):
        """
        Response to the message that user sent, try to match the message
        with a digital currency.
        :param message:
        """
        user_choice = message.text
        if user_choice not in currencies.keys():
            await make_markup(message)
            return None

        symbol = currencies[user_choice]
        data = await get_data()

        if data:
            pairs = [pair for pair in data if symbol + 'USDT' == pair['symbol']]
        else:
            await bot.reply_to(message, "Can't fetch your data, please try again later.")
            return None

        if not pairs:
            await bot.reply_to(message, f'No data found for {user_choice}')
            await make_markup(message)
            return None

        result = '\n'.join([f'{pair["symbol"]}: {pair["price"]}' for pair in pairs])
        await bot.reply_to(message, result)

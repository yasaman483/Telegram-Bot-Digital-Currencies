import telebot
from config import proxy
from telebot import asyncio_helper
asyncio_helper.proxy = proxy

def register(bot, currencies):
    async def make_markup(chat_id):
        """
        Make buttons for user to use the bot more efficiently and find
        the digital currency easily.
        :param chat_id:
        """
        markup = telebot.types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
        buttons = [button for button in currencies.keys()]
        markup.add(*buttons)
        await bot.send_message(chat_id, 'Please choose a currency from the under list:', reply_markup=markup)


    @bot.message_handler(commands=['start'])
    async def start_the_bot(message):
        """
        Start the bot with /start in telegram.
        :param message:
        """
        await bot.reply_to(message, 'Hello, Hope you have a great day!')
        await make_markup(message.chat.id)


    @bot.message_handler(commands=['help'])
    async def help_with_bot(message):
        """
        Help with bot with /help in telegram.
        :param message:
        """
        await bot.reply_to(message, 'This bot helps you to find out the current amount of Digital currencies.')
        await make_markup(message.chat.id)
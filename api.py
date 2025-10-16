import sys
import telebot
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from crypto_bot import create_bot
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logging.info('Bot called to create.')
bot = create_bot()
app = FastAPI()


@app.post("/api/webhook")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        logging.info(f'{data} received.')
    except Exception as e:
        logging.exception(f'Invalid json request: {e}')
        raise HTTPException(status_code=400, detail='Invalid Json')

    try:
        update = telebot.types.Update.de_json(data)
        bot.process_new_updates([update])
        logging.info('Update processed.')
    except Exception as e:
        logging.exception(f'Invalid Telegram update json: {e}')
        raise HTTPException(status_code=500, detail=f'Bot processing error.')

    return JSONResponse(content={'ok': True})

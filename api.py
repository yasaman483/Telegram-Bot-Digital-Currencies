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
        logging.info('datas received.')
    except Exception as e:
        logging.exception(f'Invalid json request: {e}')
        raise HTTPException(status_code=400, detail='Invalid Json')

    try:
        update = telebot.types.Update.de_json(data)
        logging.info('Update received.')
    except Exception as e:
        logging.exception(f'Invalid Telegram update json: {e}')
        raise HTTPException(status_code=400, detail=f'Bot processing error.')

    try:
        await bot.process_new_updates([update])
        logging.info('Update processed successfully.')
    except Exception as e:
        logging.exception(f'Error received while processing new updates.')
        raise HTTPException(status_code=500, detail=f'Bot processing update error: {e}')

    return JSONResponse(content={'ok': True})

import asyncio
import inspect
import telebot
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from crypto_bot import create_bot
import logging

bot = create_bot()
app = FastAPI()
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname) - %(message)')

@app.post("/")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
    except Exception as e:
        logging.exception(f'Invalid json request: {e}')
        raise HTTPException(status_code=400, detail='Invalid Json')

    try:
        update = telebot.types.Update.de_json(data)
    except Exception as e:
        logging.exception(f'Invalid Telegram update json: {e}')
        raise HTTPException(status_code=400, detail=f'Invalid Telegram update: {e}')

    try:
        proc = bot.process_new_updates([update])
    except Exception as e:
        logging.exception(f'Error calling process_new_updates: {e}')
        raise HTTPException(status_code=500, detail=f'Bot processing error: {e}')

    if inspect.isawaitable(proc):
        asyncio.ensure_future(proc)
    else:
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, bot.process_new_updates, [update])

    return JSONResponse(content={'ok': True})

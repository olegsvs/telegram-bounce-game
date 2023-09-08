from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, status, Response, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
import asyncio
import logging
import os
from datetime import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle, InlineKeyboardMarkup, \
    InlineKeyboardButton, ParseMode, ChatPermissions

from os.path import exists
import json
import sys
from aiogram import types, Dispatcher, Bot
from bounce import dp, bot, TOKEN


# Enable logging
logging.basicConfig(
    filename=datetime.now().strftime('log_game_%d_%m_%Y.log'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("game_server")

app = FastAPI()


logger.info("request")
@app.get("/score/")
async def score(user_id: str, i_id: str, score: str, request: Request):
    try:
        logger.info("score request, user_id: " + str(user_id) + ", i_id:" + str(i_id) + ", score: " + str(score))
        Dispatcher.set_current(dp)
        Bot.set_current(bot)
        await bot.set_game_score(user_id = user_id, score = score, inline_message_id = i_id)
        await bot.session.close()
        return Response(status_code=200)
    except Exception as e:
        logger.error("score error: " + str(e))
        raise HTTPException(502, detail=str(e))


app.mount("/", StaticFiles(directory="bounce", html=True), name="bounce")

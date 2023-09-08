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


logging.basicConfig(
    filename=datetime.now().strftime('log_bot_%d_%m_%Y.log'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("bot")
load_dotenv()

TOKEN = os.getenv("TG_BOT_TOKEN")
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.callback_query_handler()
async def send_welcome(callback_query: types.CallbackQuery):
    try:
        logger.info(callback_query)
        await bot.answer_callback_query(callback_query.id, url="https://voljchill.cf:4435/?i_id=" + str(callback_query.inline_message_id) + "&user_id=" + str(callback_query.from_user.id))
    except Exception as e:
        logger.error("welcome error: " + str(e))


GAME_SHORT_NAME = 'bounce'
@dp.inline_handler()
async def inline_query_handler(inline_query: types.InlineQuery):
    try:
        if inline_query.query == '':
            game_result = types.InlineQueryResultGame(
                id='1',
                game_short_name=GAME_SHORT_NAME,
                reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[
                    [types.InlineKeyboardButton(text="Play Game!", callback_game=GAME_SHORT_NAME)]
                ]),
            )
            await bot.answer_inline_query(inline_query.id, results=[game_result])
    except Exception as e:
        logger.error("inline query error: " + str(e))


@dp.callback_query_handler(lambda c: c.game_short_name == GAME_SHORT_NAME)
async def button_click(callback_query: types.CallbackQuery):
    try:
        logger.info(callback_query)
        await bot.answer_callback_query(callback_query.id, url="https://voljchill.cf:4435/?i_id=" + str(callback_query.inline_message_id) + "&user_id=" + str(callback_query.from_user.id))
    except Exception as e:
        logger.error("button error: " + str(e))


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()

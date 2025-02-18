from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import logging
import asyncio

logging.basicConfig(level= logging.INFO)
TOKEN = "7777192625:AAFYRKfroJHcjuU8tKfPPQRzroniN60WDyM"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    rep_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = KeyboardButton('Открыть сайт', web_app=WebAppInfo(url='https://aleksander-hub.github.io/index-html/'))
    rep_kb.row(bt1)
    await message.answer('Привет! Нажми кнопку ниже:', reply_markup=rep_kb)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

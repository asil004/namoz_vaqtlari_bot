import os

from aiogram import Router, types
from aiogram.filters import CommandStart
from constants import SALAM_TEXT
from dotenv import load_dotenv

router = Router()

load_dotenv('.env')


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer_sticker(sticker=os.getenv('SALAM_STICKER'))
    await message.answer(text=SALAM_TEXT)

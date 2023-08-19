import os
from aiogram import Router, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from constants import (
    START_TEXT
)

load_dotenv('.env')
router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer_sticker(sticker=os.getenv('SALAM_STICKER'))
    await message.answer(text=START_TEXT)

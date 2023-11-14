import os

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import URLInputFile

from constants import SALAM_TEXT
from dotenv import load_dotenv
from keyboards.keyboards import main_menu, main_menu_for_users
from app.database import get_if_user

router = Router()

load_dotenv('.env')


@router.message(CommandStart())
async def start_handler(message: types.Message):
    reg = await get_if_user(message.from_user.id)
    if not reg:
        await message.answer_sticker(sticker=os.getenv('SALAM_STICKER'))
        await message.answer(text=SALAM_TEXT, reply_markup=main_menu())
    else:
        await message.answer_sticker(sticker=os.getenv('SALAM_STICKER'))
        await message.answer(text=SALAM_TEXT, reply_markup=main_menu_for_users(reg[0]))
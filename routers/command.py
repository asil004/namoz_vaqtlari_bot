import os

from aiogram import Router, F
from aiogram import types
from dotenv import load_dotenv

from app.methods import get_location, get_prayer_time
from constants import (
    CONFIRMITION,
    CONFIRMITION_TEXT,
    SELECT,
    regions,
    LOCATION_BACK, CONFIRM_LOC, TODAY,
    TODAY_PRAY_TEXT
)
from keyboards.keyboards import (
    main_menu,
    when,
    select,
    send_location
)
from users_location import users

load_dotenv('users_location.txt')

router = Router()
city = ''


@router.message(F.content_type.in_({"location"}))
async def my_location(message: types.Message):
    lat = message.location.latitude
    long = message.location.longitude
    locat = get_location(lat, long)
    await message.answer(text=CONFIRM_LOC.format(city=locat), reply_markup=send_location())


@router.message(F.text == CONFIRMITION)
async def confirmition(message: types.Message):
    global city
    if str(message.from_user.id) in users.keys():
        users[message.from_user.id] = city
    else:
        users[message.from_user.id] = city
    await message.answer(text=CONFIRMITION_TEXT, reply_markup=when())


@router.message(F.text == LOCATION_BACK)
async def back(message: types.Message):
    await message.answer(text="Asosiy menyu", reply_markup=main_menu())


@router.message(F.text == SELECT)
async def select_handler(message: types.Message):
    await message.answer(text="Hududni tanlang", reply_markup=select())


@router.message(F.text == LOCATION_BACK)
async def back_handler(message: types.Message):
    await message.answer(text="Bosh menuga qaytdingiz!", reply_markup=main_menu())


@router.message(F.text.in_(regions))
async def get_pray_times(message: types.Message):
    await message.answer(text=CONFIRM_LOC.format(city=message.text), reply_markup=send_location())
    global city
    city = message.text


@router.message(F.text == TODAY)
async def get_pray_times_today(message: types.Message):
    user_id = message.from_user.id
    namoz_time = get_prayer_time(location=users[message.from_user.id], select=message.text)
    print(namoz_time)
    # await message.answer(namoz_time)
    await message.answer(
        text=TODAY_PRAY_TEXT.format(day=namoz_time['date'], month=namoz_time['date'], hudud=namoz_time['region'],
                                    bomdod=namoz_time['times']['tong_saharlik'], quyosh=namoz_time['times']['quyosh'],
                                    peshin=namoz_time['times']['peshin'], asr=namoz_time['times']['asr'],
                                    shom=namoz_time['times']['shom_iftor'], xufton=namoz_time['times']['hufton']))

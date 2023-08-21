from aiogram import Router, F
from aiogram import types
from app.methods import get_location, get_prayer_time
from constants import (
    CONFIRMITION,
    LOCATION_BACK,
    CONFIRMITION_TEXT,
    SELECT,
    regions,
    LOCATION_BACK, CONFIRM_LOC, TODAY
)
from keyboards.keyboards import (
    main_menu,
    when,
    select,
    send_location
)

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
    with open('users_location.txt', 'w') as file:
        file.writelines(f'{message.from_user.id}={city}')
    city = ''
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
    pass

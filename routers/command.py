from aiogram import Router, F
from aiogram import types

from app.methods import get_location
from constants import (
    CONFIRMITION,
    LOCATION_BACK,
    CONFIRMITION_TEXT,
    SELECT
)
from keyboards.keyboards import (
    main_menu,
    when,
    select
)

router = Router()


@router.message(F.content_type.in_({"location"}))
async def my_location(message: types.Message):
    lat = message.location.latitude
    long = message.location.longitude
    locat = get_location(lat, long)
    await message.answer(locat)


@router.message(F.text == CONFIRMITION)
async def confirmition(message: types.Message):
    await message.answer(text=CONFIRMITION_TEXT, reply_markup=when())


@router.message(F.text == LOCATION_BACK)
async def back(message: types.Message):
    await message.answer(text="Asosiy menyu", reply_markup=main_menu())


@router.message(F.text == SELECT)
async def select(message: types.Message):
    await message.answer(text="Huduni tanlang", reply_markup=select())

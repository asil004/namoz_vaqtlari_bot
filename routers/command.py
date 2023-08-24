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
    TODAY_PRAY_TEXT, WEEK, WEEK_PRAY_TIME
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
    await message.answer(
        text=TODAY_PRAY_TEXT.format(time=namoz_time['date'], hudud=namoz_time['region'],
                                    bomdod=namoz_time['times']['tong_saharlik'], quyosh=namoz_time['times']['quyosh'],
                                    peshin=namoz_time['times']['peshin'], asr=namoz_time['times']['asr'],
                                    shom=namoz_time['times']['shom_iftor'], xufton=namoz_time['times']['hufton']))


@router.message(F.text == WEEK)
async def get_pray_times_week(message: types.Message):
    user_id = message.from_user.id
    namoz_time = get_prayer_time(location=users[message.from_user.id], select=message.text)
    await message.answer(
        text=WEEK_PRAY_TIME.format(
            start_date=namoz_time[0]['date'][:10], end_date=namoz_time[-1]['date'][:10], hudud=namoz_time[0]['region'],
            dush_bomdod=namoz_time[0]['times']['tong_saharlik'], dush_quyosh=namoz_time[0]['times']['quyosh'],
            dush_peshin=namoz_time[0]['times']['peshin'], dush_asr=namoz_time[0]['times']['asr'],
            dush_shom=namoz_time[0]['times']['shom_iftor'], dush_xufton=namoz_time[0]['times']['hufton'],
            sesh_bomdod=namoz_time[1]['times']['tong_saharlik'], sesh_quyosh=namoz_time[1]['times']['quyosh'],
            sesh_peshin=namoz_time[1]['times']['peshin'], sesh_asr=namoz_time[1]['times']['asr'],
            sesh_shom=namoz_time[1]['times']['shom_iftor'], sesh_xufton=namoz_time[1]['times']['hufton'],
            chor_bomdod=namoz_time[2]['times']['tong_saharlik'], chor_quyosh=namoz_time[2]['times']['quyosh'],
            chor_peshin=namoz_time[2]['times']['peshin'], chor_asr=namoz_time[2]['times']['asr'],
            chor_shom=namoz_time[2]['times']['shom_iftor'], chor_xufton=namoz_time[2]['times']['hufton'],
            pay_bomdod=namoz_time[3]['times']['tong_saharlik'], pay_quyosh=namoz_time[3]['times']['quyosh'],
            pay_peshin=namoz_time[3]['times']['peshin'], pay_asr=namoz_time[3]['times']['asr'],
            pay_shom=namoz_time[3]['times']['shom_iftor'], pay_xufton=namoz_time[3]['times']['hufton'],
            juma_bomdod=namoz_time[4]['times']['tong_saharlik'], juma_quyosh=namoz_time[4]['times']['quyosh'],
            juma_peshin=namoz_time[4]['times']['peshin'], juma_asr=namoz_time[4]['times']['asr'],
            juma_shom=namoz_time[4]['times']['shom_iftor'], juma_xufton=namoz_time[4]['times']['hufton'],
            shan_bomdod=namoz_time[5]['times']['tong_saharlik'], shan_quyosh=namoz_time[5]['times']['quyosh'],
            shan_peshin=namoz_time[5]['times']['peshin'], shan_asr=namoz_time[5]['times']['asr'],
            shan_shom=namoz_time[5]['times']['shom_iftor'], shan_xufton=namoz_time[5]['times']['hufton'],
            yak_bomdod=namoz_time[6]['times']['tong_saharlik'], yak_quyosh=namoz_time[6]['times']['quyosh'],
            yak_peshin=namoz_time[6]['times']['peshin'], yak_asr=namoz_time[6]['times']['asr'],
            yak_shom=namoz_time[6]['times']['shom_iftor'], yak_xufton=namoz_time[6]['times']['hufton']
        )
    )

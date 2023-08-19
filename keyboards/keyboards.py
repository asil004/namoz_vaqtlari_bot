from aiogram.utils.keyboard import KeyboardBuilder, KeyboardButton

from constants import (
    SEND_LOCATION,
    SELECT,
    RETRY_SEND_LOCATION,
    LOCATION_BACK,
    CONFIRMITION,

    TASHKENT,
    NAMANGAN,
    JIZZAX,
    FARGONA,
    ANDIJON,
    SIRDARYO,
    NAVOIY,
    SAMARQAND,
    BUXORO,
    QASHQADARYO,
    SURXONDARYO,
    XORAZIM,
    QORAQALPOGISTON,

    TODAY,
    WEEK
)


def main_menu():
    builder = KeyboardBuilder(KeyboardButton)

    builder.add(
        *[
            KeyboardButton(text=SEND_LOCATION, request_location=True),
            KeyboardButton(text=SELECT)
        ]
    )
    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)


def send_location():
    builder = KeyboardBuilder(KeyboardButton)

    builder.add(
        *[
            KeyboardButton(text=RETRY_SEND_LOCATION, request_location=True),
            KeyboardButton(text=CONFIRMITION),
            KeyboardButton(text=LOCATION_BACK)
        ]
    )
    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)


def select():
    builder = KeyboardBuilder(KeyboardButton)

    builder.add(
        *[
            KeyboardButton(text=TASHKENT),
            KeyboardButton(text=NAMANGAN),
            KeyboardButton(text=JIZZAX),
            KeyboardButton(text=FARGONA),
            KeyboardButton(text=ANDIJON),
            KeyboardButton(text=SIRDARYO),
            KeyboardButton(text=NAVOIY),
            KeyboardButton(text=SAMARQAND),
            KeyboardButton(text=BUXORO),
            KeyboardButton(text=QASHQADARYO),
            KeyboardButton(text=SURXONDARYO),
            KeyboardButton(text=XORAZIM),
            KeyboardButton(text=QORAQALPOGISTON),
            KeyboardButton(text=LOCATION_BACK)
        ]
    )
    builder.adjust(3)

    return builder.as_markup(resize_keyboard=True)


def when():
    builder = KeyboardBuilder(KeyboardButton)

    builder.add(
        *[
            KeyboardButton(text=TODAY),
            KeyboardButton(text=WEEK),
            KeyboardButton(text=LOCATION_BACK)
        ]
    )
    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)

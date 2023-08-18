import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from dotenv import load_dotenv

load_dotenv('.env')
router = Router()

#hello
#salom xumoyun
#qale
async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(token=os.getenv("TOKEN"), parse_mode=ParseMode.HTML)
    commands = [
        BotCommand(command='start', description="Botni ishga tushurish uchun bosing")
    ]
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logging.info('bot stopped')

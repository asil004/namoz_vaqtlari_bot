import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from dotenv import load_dotenv
from routers import router as all_router

load_dotenv('.env')
router = Router()
router.include_router(all_router)


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(token=os.getenv("TOKEN"), parse_mode=ParseMode.HTML)
    commands = [
        BotCommand(command='start', description="Botni ishga tushurish uchun bosing")
    ]
    await bot.set_my_commands(commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logging.info('bot stopped')

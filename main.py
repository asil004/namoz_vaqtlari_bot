import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from dotenv import load_dotenv
from routers import router as all_router
from app import database as db

from aiogram.client.session.aiohttp import AiohttpSession

load_dotenv('.env')
router = Router()
router.include_router(all_router)
storage = MemoryStorage()


async def on_startup():
    await db.db_start()
    print("Baza ishga tushdi!")


async def on_shutdown():
    await db.close()
    print("Baza to'xtatildi")


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    session = AiohttpSession(proxy=os.getenv("PROXY_URL"))
    bot = Bot(token=os.getenv("TOKEN"), parse_mode=ParseMode.HTML, session=session)
    commands = [
        BotCommand(command='start', description="Botni ishga tushurish uchun bosing")
    ]
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await bot.set_my_commands(commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, storage=storage)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logging.info('bot stopped')

from aiogram import Router

from .start import router as start_router
from .command import router as command_router

router = Router()
router.include_router(start_router)
router.include_router(command_router)

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommandScopeDefault, BotCommand
from aiogram_dialog import setup_dialogs

from bot.dialogs.menu_dialogs import main_menu_dialog
from bot.dialogs.services_dialog import order_dialog, order_router
from bot.handlers.start import start_router
from bot.notify.notify import notify_admin
from core import settings, logger

bot = Bot(token=settings.telegram.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())


async def set_commands():
    commands = [
        BotCommand(command='start', description='Рестарт'),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot():
    await set_commands()
    dp.include_router(start_router)
    dp.include_routers(order_dialog, main_menu_dialog)
    setup_dialogs(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await notify_admin("Бот запущен")
    logger.info("Telegram бот запущен!")
    asyncio.create_task(dp.start_polling(bot))

async def stop_bot():
    await notify_admin("Бот остановлен")


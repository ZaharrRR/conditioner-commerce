from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram_dialog import DialogManager

from bot.states import MainMenuStates

start_router = Router()

@start_router.message(Command("start"))
async def start_cmd(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainMenuStates.main_menu)

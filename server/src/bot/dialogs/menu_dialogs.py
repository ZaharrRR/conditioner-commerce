from aiogram import types
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.api.entities import ShowMode

from bot.states import MainMenuStates, OrderStates


async def go_to_services(callback: types.CallbackQuery, button: Button, manager: DialogManager):
    try:
        await callback.message.delete()
    except:
        pass
    await manager.start(OrderStates.select_services, show_mode=ShowMode.SEND)

async def go_to_about(callback: types.CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(MainMenuStates.about)

async def go_to_contacts(callback: types.CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(MainMenuStates.contacts)

async def back_to_menu(callback: types.CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(MainMenuStates.main_menu)

# Геттеры
async def main_menu_getter(dialog_manager: DialogManager, **kwargs):
    return {}

async def about_getter(dialog_manager: DialogManager, **kwargs):
    return {
            "about_text": (
                "❄️ <b>Абсолют холод</b> - создаем идеальный климат для вас!\n\n"
                "✨ <u>Наши услуги:</u>\n"
                "• 🛒 Продажа кондиционеров\n"
                "• 🔧 Установка и монтаж\n"
                "• 🛠️ Обслуживание и ремонт\n\n"
                "🏆 <i>Почему мы?</i>\n"
                "  ▸ ✅ Гарантия качества\n"
                "  ▸ ⏱️ Быстрый выезд\n"
                "  ▸ 💯 Профессионализм\n\n"
                "📞 <code>Ваш комфорт - наша забота!</code>"
        )
    }

async def contacts_getter(dialog_manager: DialogManager, **kwargs):
    return {
        "owner": "Болгарь Олег Иванович",
        "phone": "+7 (912) 430-33-33",
        "email": "siberian.park@yandex.ru",
        "address": "625042, Россия, Тюмень, улица Федюнинского 60к1",
        "time_work": "8:00 - 20:00"
    }

# Окна
main_menu_window = Window(
    Const("🏠 <b>Главное меню</b>\n\nВыберите раздел:"),
    Row(
        Button(Const("🛠 Услуги"), id="services", on_click=go_to_services),
        Button(Const("ℹ️ О нас"), id="about", on_click=go_to_about),
    ),
    Button(Const("📞 Контактная информация"), id="contacts", on_click=go_to_contacts),
    state=MainMenuStates.main_menu,
    getter=main_menu_getter
)

about_window = Window(
    Format("ℹ️ <b>О нас</b>\n\n{about_text}"),
    Button(Const("⬅️ Назад"), id="back", on_click=back_to_menu),
    state=MainMenuStates.about,
    getter=about_getter
)

contacts_window = Window(
    Const("📞 <b>Контактная информация</b>\n\n"),
    Format(
          "👨‍🔧 <b>ФИО</b>: {owner}\n"
          "☎️ <b>Телефон</b>: {phone}\n"
          "📧 <b>Email</b>: {email}\n"
          "🏢 <b>Адрес</b>: {address}\n"
          "⌚ <b>Режим работы</b>: {time_work}"
    ),
    Button(Const("⬅️ Назад"), id="back", on_click=back_to_menu),
    state=MainMenuStates.contacts,
    getter=contacts_getter
)

# Сборка диалога
main_menu_dialog = Dialog(
    main_menu_window,
    about_window,
    contacts_window
)
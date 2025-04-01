from typing import Any, Dict

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import (
    Multiselect, ScrollingGroup, Next, Back, Cancel, RequestContact, Group
)
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram_dialog.widgets.text import Const, Format, List
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.api.entities import ShowMode

from bot.dao.dao import TelegramOrderDAO
from bot.notify.notify import notify_orders_admins
from bot.states import OrderStates
from dao.service import ServiceDAO
from db.database import connection



# Handlers ---------------------------------------------------------------
async def on_services_selected(
        event: types.Message | types.CallbackQuery,
        widget: Any,
        manager: DialogManager,
        item_id: str,
):
    selected = set(manager.dialog_data.get("selected_services", []))
    selected.symmetric_difference_update({item_id})
    manager.dialog_data["selected_services"] = list(selected)


async def handle_address_input(
        message: types.Message,
        widget: TextInput,
        manager: DialogManager,
        address: str,
):
    manager.dialog_data["address"] = address.strip()
    await manager.next()


async def handle_contact_received(
        message: types.Message,
        widget: Any,
        manager: DialogManager,
):
    if message.contact:
        manager.dialog_data["phone"] = message.contact.phone_number
        await finalize_order(message, manager)
    else:
        await message.answer("Пожалуйста, используйте кнопку для отправки контакта")

@connection()
async def finalize_order(
        message: types.Message,
        manager: DialogManager,
        session
):
    data = manager.dialog_data
    user = message.from_user
    all_services = data["services"]
    selected_ids = set(data["selected_services"])
    selected_services = [
        (s_id, name, price)
        for s_id, name, price in all_services
        if s_id in selected_ids
    ]

    services_list = "\n".join(
        f"▪️ <b>{name}</b> — <i>от {price}₽</i>"
        for _, name, price in selected_services
    )
    total = sum(price for _, _, price in selected_services)

    order_text = (
        "🎉 <b>🚀 Ваш заказ успешно оформлен!</b>\n\n"
        "👤 <u>Контактные данные:</u>\n"
        f"   ▫️ <b>Имя:</b> {user.full_name}\n"
        f"   ▫️ <b>Телефон:</b> {data['phone']}\n"
        f"   ▫️ <b>Адрес:</b> {data['address']}\n\n"
        "🛠 <u>Выбранные услуги:</u>\n"
        f"{services_list}\n\n"
        f"💸 <b>Итоговая сумма:</b> <code>{total}₽</code>"
    )

    order_dao = TelegramOrderDAO(session)
    await order_dao.create_order_with_services(
        customer_name=user.full_name,
        customer_phone=data["phone"],
        address=data["address"],
        total_price=total,
        services=selected_services
    )
    await message.answer(order_text, reply_markup=types.ReplyKeyboardRemove())
    await manager.done(show_mode=ShowMode.DELETE_AND_SEND)

# Data getters -----------------------------------------------------------
@connection()
async def services_getter(
        dialog_manager: DialogManager,
        session,
        **kwargs,
) -> Dict[str, Any]:
    if "services" not in dialog_manager.dialog_data:
        service_dao = ServiceDAO(session)
        services = await service_dao.get_all_services()
        dialog_manager.dialog_data["services"] = [
            (str(s.id), s.service_type, s.base_price) for s in services
        ]

    selected_ids = dialog_manager.dialog_data.get("selected_services", [])

    selected_services = [
        (s_id, name, price)
        for s_id, name, price in dialog_manager.dialog_data["services"]
        if s_id in selected_ids
    ]

    total = sum(price for _, _, price in selected_services)

    return {
        "services": dialog_manager.dialog_data["services"],
        "selected_services": selected_services,
        "total": total,
        "selected_count": len(selected_ids),
    }


async def contact_data_getter(
        dialog_manager: DialogManager,
        **kwargs,
) -> Dict[str, Any]:
    return {"address": dialog_manager.dialog_data.get("address", "")}


services_multiselect = Multiselect(
    checked_text=Format("✅ {item[1]} - от {item[2]}₽"),
    unchecked_text=Format("◽ {item[1]} - от {item[2]}₽"),
    id="ms_services",
    item_id_getter=lambda item: item[0],
    items="services",
    on_click=on_services_selected,
)

services_scroll = ScrollingGroup(
    services_multiselect,
    width=1,
    height=5,
    id="scroll_services",
)

selected_services_list = List(
    Format("⭐ <b>{item[1]}</b> — <i>{item[2]}₽</i>"),
    items="selected_services",
)

select_services_window = Window(
    Format("🛒 <b>Выбор услуг</b>\n"
           "────────────────────\n"
           "🔍 Выбрано: {selected_count} услуг"),
    services_scroll,
    Format("\n📥 <u>Ваш выбор:</u>"),
    selected_services_list,
    Format("\n💵 <b>Общая сумма:</b> <code>{total}₽</code>"),
    Next(Const("✅ Продолжить оформление"), id="next_btn",
         when=F["dialog_data"]["selected_services"].len() > 0),
    Cancel(Const("❌ Отменить заказ")),
    state=OrderStates.select_services,
    getter=services_getter,
)


address_window = Window(
    Const("🏡 <b>Введите адрес</b>\n\n"
          "📍 Пример:\n"
          "<i>г. Тюмень, ул. Федюнинского,  д. 60к1</i>"),
    TextInput(id="address_input", on_success=handle_address_input),
    Back(Const("⬅️ Назад")),
    state=OrderStates.enter_address,
)



contact_window = Window(
    Format("📱 <b>Контактные данные</b>\n\n"
           "🏠 Адрес доставки:\n"
           "<i>{address}</i>\n\n"
           "👇 Нажмите кнопку ниже, чтобы поделиться контактом:"),
    Group(
        RequestContact(Const("📲 Отправить мой контакт")),
        Back(Const("↩️ Назад")),
    ),
    MessageInput(handle_contact_received),
    state=OrderStates.enter_contact,
    getter=contact_data_getter,
    markup_factory=ReplyKeyboardFactory(
        resize_keyboard=True,
        one_time_keyboard=True
    )
)

order_dialog = Dialog(
    select_services_window,
    address_window,
    contact_window,
)


order_router = Router()

@order_router.message(Command('service'))
async def start_service_dialog(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(OrderStates.select_services, show_mode=ShowMode.SEND)
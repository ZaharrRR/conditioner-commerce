from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommandScopeDefault, BotCommand
from aiogram_dialog import setup_dialogs

from core import settings, logger
from schemas import OrderRead

bot = Bot(token=settings.telegram.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

async def set_commands():
    commands = [BotCommand(command='start', description='Рестарт')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

async def start_bot():
    setup_dialogs(dp)
    await set_commands()

    for admin_id in settings.telegram.admin_ids:
        try:
            await bot.send_message(admin_id, 'Бот запущен🥳')
        except Exception as e:
            logger.warning(f"Не удалось отправить сообщение администратору {admin_id}: {e}")
            pass
    logger.info("Бот успешно запущен.")

async def stop_bot():
    try:
        for admin_id in settings.telegram.admin_ids:
            await bot.send_message(admin_id, 'Бот остановлен')
    except:
        pass
    logger.error("Бот остановлен!")

async def notify_admins(new_order: OrderRead):
    created_date = new_order.created_at.strftime('%d.%m.%Y %H:%M')

    message_text = (
        f"📦 <b>Новый заказ! ({created_date})</b> 📦\n"
        f"👤 <b>Клиент:</b> {new_order.customer_name} {new_order.customer_surname}\n"
        f"📞 <b>Телефон:</b> {new_order.customer_phone}\n"
        f"🏠 <b>Адрес:</b> {new_order.address}\n"
        f"💵 <b>Итоговая цена:</b> {new_order.total_price}\n"
        f"🔸 <b>Товар:</b> {new_order.product.name} ({new_order.product.brand_name}) за {new_order.product.price}\n"
    )

    if new_order.services:
        message_text += "🔧 <b>Услуги:</b>\n"
        for service in new_order.services:
            message_text += f"   • {service.service_type}: {service.base_price}\n"

    for admin_id in settings.telegram.admin_ids:
        try:
            await bot.send_message(admin_id, message_text, parse_mode=ParseMode.HTML)
        except Exception as e:
            logger.warning(f"Ошибка отправки сообщения администратору {admin_id}: {e}")

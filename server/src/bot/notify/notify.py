from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core import settings, logger
from schemas import OrderRead

bot = Bot(token=settings.telegram.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def notify_admin(message: str):
    for admin_id in settings.telegram.admin_ids:
        try:
            await bot.send_message(admin_id, message)
        except Exception as e:
            logger.warning(f"Не удалось отправить сообщение администратору {admin_id}: {e}")

async def notify_orders_admins(new_order: OrderRead):

    created_date = new_order.created_at.strftime('%d.%m.%Y %H:%M')

    message_text = (
        f"📦 <b>Новый заказ! ({created_date})</b> 📦\n"
        f"👤 <b>Клиент:</b> {new_order.customer_name}"
        f"{' ' + new_order.customer_surname if new_order.customer_surname else ''}\n"
        f"📞 <b>Телефон:</b> {new_order.customer_phone}\n"
        f"🏠 <b>Адрес:</b> {new_order.address}\n"
        f"📝 <b>Комментарий:</b> {new_order.comment if new_order.comment else ' '}\n"
        f"💵 <b>Итоговая цена:</b> {new_order.total_price}\n"
    )

    if new_order.product:
        message_text += (
            f"🔸 <b>Товар:</b> {new_order.product.name} "
            f"({new_order.product.brand_name}) за {new_order.product.price}\n"
        )

    if new_order.services:
        message_text += "🔧 <b>Услуги:</b>\n"
        for service in new_order.services:
            message_text += f"   • {service.service_type}: {service.base_price}\n"

    await notify_admin(message_text)
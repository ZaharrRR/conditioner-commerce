from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from bot.notify.notify import notify_orders_admins
from core import logger
from models import TelegramOrder, TelegramOrderService, Service
from decimal import Decimal

from schemas import OrderServiceRead, OrderRead


class TelegramOrderDAO:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_order_with_services(
        self,
        customer_name: str,
        customer_phone: str,
        address: str,
        total_price: Decimal,
        services
    ) -> TelegramOrder:
        try:
            new_order = TelegramOrder(
                customer_name=customer_name,
                customer_phone=customer_phone,
                address=address,
                total_price=total_price
            )
            self.session.add(new_order)
            await self.session.flush()

            for service_id, name, price in services:
                order_service = TelegramOrderService(
                    order_id=new_order.id,
                    service_id=service_id,
                    total_price=price
                )
                self.session.add(order_service)
            await self.session.commit()

            stmt_services = (
                select(Service.id, Service.service_type, Service.base_price, Service.created_at)
                .join(TelegramOrderService, TelegramOrderService.service_id == Service.id)
                .where(TelegramOrderService.order_id == new_order.id)
                .distinct()
            )
            result_services = await self.session.execute(stmt_services)

            services = [OrderServiceRead.model_validate(service) for service in result_services]

            order_pydantic = OrderRead(
                id=new_order.id,
                customer_name=new_order.customer_name,
                customer_phone=new_order.customer_phone,
                address=new_order.address,
                total_price=new_order.total_price,
                created_at=new_order.created_at,
                updated_at=new_order.updated_at,
                services=services,
            )
            await notify_orders_admins(order_pydantic)

            return order_pydantic

        except IntegrityError:
            await self.session.rollback()
            logger.warning("⚠️ Заказ с такими данными уже существует")
            raise ValueError("Order already exists")
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка при создании заказа: {e}")
            raise RuntimeError("Database error")
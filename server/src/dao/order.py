from typing import Optional
from uuid import UUID


from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from core import logger
from models.order import Order
from schemas.orders import OrderCreate, OrderRead

class OrderDAO:
    """DAO для заказов (Order)"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_order(self, order: OrderCreate):
        try:
            new_order = Order(**order.model_dump())
            self.session.add(new_order)
            await self.session.flush()
            await self.session.commit()
            logger.info(f"✅ Заказ (Order) с ID {new_order.id} создан")
            return new_order
        except IntegrityError:
            await self.session.rollback()
            logger.warning("⚠️ Заказ с такими данными уже существует")
            raise ValueError("Order already exists")
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка при создании заказа: {e}")
            raise RuntimeError("Database error")

    async def get_order_by_id(self, order_id: UUID) -> Optional[OrderRead]:
        logger.debug(f"🔎 Получение заказа с ID: {order_id}")
        try:
            stmt = select(Order).options(selectinload(Order.services)).where(Order.id == order_id)
            result = await self.session.execute(stmt)
            order = result.scalar_one_or_none()
            logger.info(f"✅ Заказ с ID {order_id} {'найден' if order else 'не найден'}")
            if order is None:
                return None
            return OrderRead.model_validate(order, from_attributes=True)
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка при получении заказа с ID {order_id}: {e}")
            raise RuntimeError("Database error")

    async def get_orders(self) -> list[OrderRead]:
        """Получает все заказы с предзагрузкой услуг"""



    async def delete_order_by_id(self, order_id: UUID) -> bool:
        """Удаляет заказ по ID"""
        logger.debug(f"🗑️ Удаление заказа с ID: {order_id}")
        try:
            order = await self.get_order_by_id(order_id)
            if not order:
                logger.warning(f"❌ Заказ с ID {order_id} не найден")
                return False
            await self.session.delete(order)
            await self.session.flush()
            await self.session.commit()
            logger.info(f"✅ Заказ с ID {order_id} удалён")
            return True
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка при удалении заказа с ID {order_id}: {e}")
            raise RuntimeError("Database error")

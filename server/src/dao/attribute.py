from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core import logger
from models import Attribute
from schemas import AttributeCreate, AttributeRead


class AttributeDAO:
    """DAO для Attribute"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_attribute(self, attribute: AttributeCreate) -> AttributeRead:
        """Создает Attribute"""

        logger.debug("⚙️ Создание Attribute")
        try:
            new_attribute = Attribute(name=attribute.name)
            self.session.add(new_attribute)
            await self.session.flush()
            await self.session.commit()
            logger.info(f"✅ Запись Attribute c ID {new_attribute.id} создана")
            return new_attribute
        except IntegrityError:
            await self.session.rollback()
            logger.warning(
                f"⚠️ Запись Attribute с таким именем уже существует: {attribute.name}"
            )
            raise ValueError(f"Attribute '{attribute.name}' already exists")
        except SQLAlchemyError as e:
            logger.error(f"❌Ошибка при создание Attribute: {e}")
            raise RuntimeError("Database error")
            await self.session.rollback()

    async def get_attribute_by_id(self, attribute_id: UUID) -> Optional[AttributeRead]:
        """Получает Attribute по id"""

        logger.debug(f"🔎 Получение Attribute с ID: {attribute_id}")
        try:
            stmt = select(Attribute).where(Attribute.id == attribute_id)
            result = await self.session.execute(stmt)
            record = result.scalar_one_or_none()
            logger.info(
                f"✅ Запись Attribute с ID {attribute_id} {'найдена' if record else 'не найдена'}"
            )
            return record
        except SQLAlchemyError as e:
            logger.error(
                f"❌Ошибка при получение записи Attribute с ID {attribute_id}: {e}"
            )
            raise RuntimeError("Database error")

    async def get_attributes(self) -> list[AttributeRead]:
        """Получает все записи Attribute"""

        logger.debug("🔎 Получение всех записей Attribute")
        try:
            stmt = select(Attribute)
            result = await self.session.execute(stmt)
            records = result.scalars().all()
            logger.info(f"✅ Найдено {len(records)} записей.")
            return records
        except SQLAlchemyError as e:
            logger.error(f"❌Ошибка при получение всех записей Attribute: {e}")
            raise RuntimeError("Database error")

    async def delete_attribute_by_id(self, attribute_id: UUID) -> bool:
        """Удаляет запись Attribute по id"""

        logger.debug(f"🗑️ Удаление Attribute по id️: {attribute_id}")
        try:
            attribute = await self.get_attribute_by_id(attribute_id)

            if not attribute:
                logger.warning(f"❌ Attribute с ID {attribute_id} не найден")
                return False

            await self.session.delete(attribute)
            await self.session.flush()
            await self.session.commit()
            logger.info(f"✅ Запись Attribute с ID {attribute_id} удалена")
            return True
        except SQLAlchemyError as e:
            logger.error(f"❌Ошибка при удаление записи Attribute: {e}")
            raise RuntimeError("Database error")

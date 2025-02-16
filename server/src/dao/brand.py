from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core import logger
from models import Brand
from schemas import BrandCreate, BrandRead, BrandUpdate


class BrandDAO:
    """DAO для Brand"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_brand(self, brand: BrandCreate) -> BrandRead:
        """Создает Brand"""

        logger.debug("⚙️ Создание Brand")
        try:
            new_brand = Brand(**brand.model_dump())
            self.session.add(new_brand)

            await self.session.flush()
            await self.session.commit()

            logger.info(f"Brand создан с ID {new_brand.id}")
            return new_brand
        except IntegrityError:
            await self.session.rollback()
            logger.warning(
                f"⚠️ Запись Brand с таким именем уже существует: {brand.name}"
            )
            raise ValueError(f"Brand '{brand.name}' already exists")
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка при создание Brand: {e}")
            await self.session.rollback()

    async def get_brand_by_id(self, brand_id: UUID) -> Optional[BrandRead]:
        """Получает Brand по id"""

        logger.debug(f"🔎 Получение записи Brand с ID: {brand_id}")
        try:
            stmt = select(Brand).where(Brand.id == brand_id)
            result = await self.session.execute(stmt)
            record = result.scalar_one_or_none()
            logger.info(
                f"✅ Запись Brand с ID {brand_id} {'найдена' if record else 'не найдена'}"
            )
            return record
        except SQLAlchemyError as e:
            logger.error(f"❌Ошибка при получение записи Brand с ID {brand_id}: {e}")
            raise e

    async def get_brands(self) -> list[BrandRead]:
        """Получает всех записей Brand"""

        logger.debug("🔎 Получение всех записей Brand")
        try:
            stmt = select(Brand)
            result = await self.session.execute(stmt)
            records = result.scalars().all()
            logger.info(f"✅ Найдено {len(records)} записей")
            return records
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка при получение всех записей Brand: {e}")
            raise e

    async def delete_brand_by_id(self, brand_id: UUID) -> bool:
        """Удаляет запись Brand"""

        logger.debug(f"🗑️ Удаление записи Brand по id️: {brand_id}")
        try:
            brand = await self.get_brand_by_id(brand_id)

            if not brand:
                logger.warning(f"⚠️ Brand с ID {brand_id} не найден")
                return False

            await self.session.delete(brand)
            await self.session.flush()
            await self.session.commit()
            logger.info(f"✅ Запись Brand с ID {brand_id} удалена")
            return True
        except SQLAlchemyError as e:
            logger.error(f"❌Ошибка при удаление записи Brand: {e}")
            raise e

    async def update_brand(
        self, brand_id: UUID, brand_update: BrandUpdate
    ) -> Optional[BrandRead]:
        """Обновляет Brand по id"""

        logger.debug(f"🔄 Обновление Brand с ID {brand_id}")
        try:
            brand = await self.get_brand_by_id(brand_id)
            if not brand:
                logger.warning(f"⚠️ Brand с ID {brand_id} не найден")
                return None

            # Обновляем только переданные поля
            for field, value in brand_update.model_dump(exclude_unset=True).items():
                setattr(brand, field, value)

            await self.session.flush()
            await self.session.commit()

            await self.session.refresh(brand)
            logger.info("✅ Запись Brand обновлена")
            return BrandRead.model_validate(brand)

        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка при обновлении Brand с ID {brand_id}: {e}")
            await self.session.rollback()
            raise e

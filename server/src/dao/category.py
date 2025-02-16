from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core import logger
from models import Category
from schemas import CategoryCreate, CategoryRead


class CategoryDAO:
    """DAO для Category"""

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_category(self, category: CategoryCreate) -> CategoryRead:
        """Создает Категорию"""

        logger.debug("⚙️ Создание Brand")
        try:
            new_category = Category(**category.model_dump())
            self.session.add(new_category)

            await self.session.flush()
            await self.session.commit()

            logger.info(f"Brand создан с ID {new_category.id}")
            return CategoryRead.model_validate(new_category)
        except IntegrityError:
            await self.session.rollback()
            logger.warning(
                f"⚠️ Запись Category с таким именем уже существует: {category.name}"
            )
            raise ValueError(f"Category '{category.name}' already exists")
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка при создание Brand: {e}")
            await self.session.rollback()
            raise e

    async def get_all_categories(self) -> list[Category]:
        """Получает всех записей Category"""

        logger.debug("🔎 Получение всех записей Brand")
        try:
            stmt = select(Category)
            result = await self.session.execute(stmt)
            records = result.scalars().all()
            logger.info(f"✅ Найдено {len(records)} записей")
            return records
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка при получение всех записей Category: {e}")
            raise e

    async def get_category_by_id(self, category_id: UUID) -> CategoryRead:
        """Получает Category по id"""

        logger.debug(f"🔎 Получение записи Category с ID: {category_id}")
        try:
            stmt = select(Category).where(Category.id == category_id)
            result = await self.session.execute(stmt)
            record = result.scalar_one_or_none()
            logger.info(
                f"✅ Запись Category с ID {category_id} {'найдена' if record else 'не найдена'}"
            )
            return record
        except SQLAlchemyError as e:
            logger.error(f"❌Ошибка при получение записи Category с ID {category_id}: {e}")
            raise e

    async def get_category_by_name(self, category_name: str) -> CategoryRead:
        """Получает Category по name"""
        logger.debug(f"🔎 Получение записи Category с Name: {category_name}")
        try:
            stmt = select(Category).where(Category.name == category_name)
            result = await self.session.execute(stmt)
            record = result.scalar_one_or_none()
            logger.info(
                f"✅ Запись Category с name: {category_name} {'найдена' if record else 'не найдена'}"
            )
            return CategoryRead.model_validate(record)
        except SQLAlchemyError as e:
            logger.error(f"❌Ошибка при получение записи Category с name {category_name}: {e}")
            raise e

    async def delete_category_by_id(self, category_id: UUID) -> bool:
        """Удаляет запись Category по id"""

        logger.debug(f"🗑️ Удаление Category по id️: {category_id}")
        try:
            category = await self.get_category_by_id(category_id)

            if not category:
                logger.warning(f"❌ Category с ID {category_id} не найден")
                return False

            await self.session.delete(category)
            await self.session.flush()
            await self.session.commit()
            logger.info(f"✅ Запись Category с ID {category_id} удалена")
            return True
        except SQLAlchemyError as e:
            logger.error(f"❌Ошибка при удаление записи Category: {e}")
            raise e

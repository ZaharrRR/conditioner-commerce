from decimal import Decimal
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core import logger
from models import Brand, Category, Product
from schemas import ProductCreate, ProductRead, ProductReadWithRelations


class ProductDAO:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_product(self, data: ProductCreate) -> ProductRead:
        """Создает новый продукт"""
        logger.debug(f"🛒 Создание нового продукта: {data.name}")

        try:
            brand = await self.session.get(Brand, data.brand_id)
            if not brand:
                logger.warning(f"⚠️ Бренд с ID {data.brand_id} не найден")
                raise ValueError(f"Brand with ID {data.brand_id} not found")

            category = await self.session.get(Category, data.category_id)
            if not category:
                logger.warning(f"⚠️ Категория с ID {data.category_id} не найдена")
                raise ValueError(f"Category with ID {data.category_id} not found")

            new_product = Product(
                name=data.name,
                price=Decimal(data.price),
                brand_id=data.brand_id,
                category_id=data.category_id
            )

            self.session.add(new_product)
            await self.session.flush()
            await self.session.commit()

            logger.info(f"✅ Продукт создан с ID {new_product.id}")
            return ProductRead.model_validate(new_product)

        except IntegrityError:
            await self.session.rollback()
            logger.warning(f"⚠️ Продукт с таким именем уже существует: {data.name}")
            raise ValueError(f"Product '{data.name}' already exists")

        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка SQLAlchemy при создании продукта: {e}")
            raise RuntimeError("Database error")

    async def get_product_with_relations_by_id(self, product_id: UUID) -> Optional[ProductReadWithRelations]:
        """Получение Product по ID"""
        logger.debug(f"🔍 Поиск продукта с ID {product_id}")

        try:
            stmt = (
                select(
                    Product.id,
                    Product.name,
                    Product.price,
                    Brand.name.label("brand_name"),
                    Category.name.label("category_name"),
                    Product.created_at,
                    Product.updated_at
                )
                .join(Brand, Product.brand_id == Brand.id)
                .join(Category, Product.category_id == Category.id)
                .where(Product.id == product_id)
            )

            result = await self.session.execute(stmt)
            row = result.first()

            if not row:
                logger.warning(f"⚠️ Product с ID {product_id} не найден")
                return None

            return row

        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка SQLAlchemy при получении продукта: {e}")
            raise RuntimeError("Database error")

    async def get_all_products(self):
        """Получает все записи Product с brand_name и category_name"""
        logger.debug(f"🔎 Получение всех записей Product")
        try:
            stmt = (
                select(
                    Product.id,
                    Product.name,
                    Product.price,
                    Brand.name.label("brand_name"),
                    Category.name.label("category_name"),
                    Product.created_at,
                    Product.updated_at
                )
                .join(Brand, Product.brand_id == Brand.id)
                .join(Category, Product.category_id == Category.id)
            )

            result = await self.session.execute(stmt)
            rows = result.fetchall()

            if not rows:
                logger.warning(f"⚠️ Продукты не найдены")
                return []

            products = rows
            return products

        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка SQLAlchemy при получении списка Product: {e}")
            raise RuntimeError("Database error")

    async def get_products_by_category(self, category_id: UUID) -> list[ProductRead]:
        pass

    async def delete_product(self, product_id: UUID) -> bool:
        pass

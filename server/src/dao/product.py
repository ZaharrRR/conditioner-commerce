from typing import Optional
from uuid import UUID

from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core import logger
from models import Brand, Category, Product, ProductAttribute, Attribute
from schemas import ProductCreate, ProductRead, ProductReadWithRelations, ProductAttributeLink, ProductAttributeDelete


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

            new_product = Product(**data.model_dump())
            self.session.add(new_product)
            await self.session.flush()

            if data.attributes:
                for attribute_data in data.attributes:
                    attribute = await self.session.get(Attribute, attribute_data["attribute_id"])
                    if not attribute:
                        logger.warning(f"⚠️ Атрибут с ID {attribute_data['attribute_id']} не найден")
                        raise ValueError(f"Attribute with ID {attribute_data['attribute_id']} not found")

                    product_attribute = ProductAttribute(
                        product_id=new_product.id,
                        attribute_id=attribute.id,
                        value=attribute_data["value"]
                    )
                    self.session.add(product_attribute)

            await self.session.commit()

            logger.info(f"✅ Продукт создан с ID {new_product.id}")
            return await self.get_product_with_relations_by_id(new_product.id)

        except IntegrityError as e:
            await self.session.rollback()
            logger.warning(f"⚠️ Продукт с таким именем уже существует: {data.name}({e})_")
            raise ValueError(f"Product '{data.name}' already exists")

        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка SQLAlchemy при создании продукта: {e}")
            raise RuntimeError("Database error")

    async def get_product_with_relations_by_id(self, product_id: UUID) -> Optional[ProductReadWithRelations]:
        """Получение Product по ID с аттрибутами"""
        logger.debug(f"🔍 Поиск продукта с ID {product_id}")

        try:
            stmt = (
                select(
                    Product.id,
                    Product.name,
                    Product.price,
                    Product.photo_url,
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

            attributes = []
            stmt_attributes = (
                select(
                    Attribute.name, ProductAttribute.value
                )
                .join(ProductAttribute, ProductAttribute.attribute_id == Attribute.id)
                .where(ProductAttribute.product_id == product_id)
                .distinct()
            )

            result_attributes = await self.session.execute(stmt_attributes)

            for attribute_name, value in result_attributes:
                attributes.append({
                    "attribute_name": attribute_name,
                    "value": value
                })

            product_read_with_relations = ProductReadWithRelations(
                id=row.id,
                name=row.name,
                photo_url=row.photo_url,
                price=row.price,
                brand_name=row.brand_name,
                category_name=row.category_name,
                created_at=row.created_at,
                updated_at=row.updated_at,
                attributes=attributes
            )

            logger.info(f"✅ Продукт с ID {product_id} найден с аттрибутами")
            return product_read_with_relations

        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка SQLAlchemy при получении продукта: {e}")
            raise RuntimeError("Database error")

    async def get_new_products(self):
        logger.debug("🔎 Получение 4 новых записей Product")
        try:
            stmt = select(Product).order_by(Product.created_at.desc()).limit(4)

            result = await self.session.execute(stmt)
            rows = result.scalars().all()

            return rows

        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка SQLAlchemy при получении списка Product: {e}")
            raise RuntimeError("Database error")


    async def update_product_photo(self, product_id: UUID, photo_url: str):
        result = await self.session.execute(select(Product).where(Product.id == product_id))
        product = result.scalar_one_or_none()
        if not product:
            raise ValueError(f"Product with {product_id} not found")

        product.photo_url = photo_url

        await self.session.flush()
        await self.session.commit()

        await self.session.refresh(product)
        return await self.get_product_with_relations_by_id(product_id)

    async def get_all_products(self):
        """Получает все записи Product с brand_name и category_name"""
        logger.debug("🔎 Получение всех записей Product")
        try:
            stmt = select(
                    Product.id,
                    Product.name,
                    Product.price,
                    Product.description,
                    Product.photo_url,
                    Brand.name.label("brand_name"),
                    Category.name.label("category_name"),
                    Product.created_at,
                    Product.updated_at
                ).join(Brand, Product.brand_id == Brand.id).join(Category, Product.category_id == Category.id)


            rows = await self.session.execute(stmt)
            records = rows.mappings().all()
            if not records:
                logger.warning("⚠️ Продукты не найдены")
                return []

            return records

        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка SQLAlchemy при получении списка Product: {e}")
            raise RuntimeError("Database error")

    async def delete_product(self, product_id: UUID) -> bool:
        """Удаляет товар по ID"""
        logger.debug(f"🗑️ Удаление товара с ID: {product_id}")
        try:
            order = await self.get_product_with_relations_by_id(product_id)
            if not order:
                logger.warning(f"❌ Товар с ID {product_id} не найден")
                return False
            await self.session.delete(order)
            await self.session.flush()
            await self.session.commit()
            logger.info(f"✅ Товар с ID {product_id} удалён")
            return True
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка при удалении товара с ID {product_id}: {e}")
            raise RuntimeError("Database error")

    async def link_attributes_to_product(self, product_id: UUID,
                                         attributes_links: list[ProductAttributeLink]) -> ProductRead:
        """Привязывает аттрибуты к продукту с передачей значений через Pydantic"""
        logger.debug(f"⚙️ Привязка аттрибутов к продукту с ID {product_id}")
        try:
            stmt = select(Product).where(Product.id == product_id)
            result = await self.session.execute(stmt)
            product = result.scalar_one_or_none()

            if not product:
                logger.warning(f"⚠️ Продукт с ID {product_id} не найден")
                raise ValueError(f"Product with ID {product_id} not found")

            attribute_ids = [link.attribute_id for link in attributes_links]
            stmt = select(Attribute).where(Attribute.id.in_(attribute_ids))
            result = await self.session.execute(stmt)
            attributes = result.scalars().all()

            if len(attributes) != len(attribute_ids):
                raise ValueError("Некоторые аттрибуты не найдены.")

            for link in attributes_links:
                product_attribute = ProductAttribute(
                    product_id=product.id,
                    attribute_id=link.attribute_id,
                    value=link.value
                )
                self.session.add(product_attribute)

            await self.session.commit()
            await self.session.refresh(product)
            logger.info(f"✅ Аттрибуты привязаны к продукту с ID {product.id}")
            return product

        except IntegrityError as e:
            await self.session.rollback()
            logger.error(f"⚠️ Ошибка при привязке аттрибутов: {e}")
            raise ValueError("Error linking attributes to product")
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка при привязке аттрибутов к продукту: {e}")
            raise RuntimeError("Database error")


    async def delete_attribute_from_product(self, data: ProductAttributeDelete) -> bool:
        logger.debug(f"🗑️ Удаление аттрибута {data.name} у продукта {data.product_id}")
        try:
            stmt = (
                delete(ProductAttribute)
                .where(
                    ProductAttribute.product_id == data.product_id,
                    ProductAttribute.attribute.has(name=data.name)
                )
            )
            result = await self.session.execute(stmt)
            await self.session.commit()

            if result.rowcount == 0:
                logger.warning("⚠️ Аттрибут не найден или уже удалён")
                return False

            logger.info(f"✅ Аттрибут {data.attribute_id} удалён у продукта {data.product_id}")
            return True

        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка при удалении аттрибута: {e}")
            raise RuntimeError("Database error")
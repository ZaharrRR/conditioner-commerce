from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from schemas import ProductCreate, ProductRead


class ProductDAO:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_product(self, product: ProductCreate) -> ProductRead:
        pass

    async def get_product_by_id(self, product_id: UUID) -> ProductRead:
        pass

    async def get_all_products(self) -> list[ProductRead]:
        pass

    async def get_products_by_category(self, category_id: UUID) -> list[ProductRead]:
        pass

    async def delete_product(self, product_id: UUID) -> bool:
        pass

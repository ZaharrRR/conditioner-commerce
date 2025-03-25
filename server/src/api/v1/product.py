from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dao.product import ProductDAO
from db.database import get_session
from schemas import ProductRead, ProductCreate, ProductReadWithRelations, ProductAttributeLink

router = APIRouter(prefix="/product", tags=["Products"])


@router.post(
    "/create",
    response_model=ProductRead,
    summary="Создание Product",
    status_code=201
)
async def create_product(data: ProductCreate, session: AsyncSession = Depends(get_session)):
    product_dao = ProductDAO(session)
    try:
        new_product = await product_dao.create_product(data)
        return new_product

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    '/all',
    response_model=list[ProductReadWithRelations],
    summary="Получение всех записей Product",
    status_code=200,
)
async def get_products(session: AsyncSession = Depends(get_session)):
    product_dao = ProductDAO(session)
    try:
        products = await product_dao.get_all_products()
        return products
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get(
    "/get-by-id/{product_id}",
    status_code=200,
    response_model=ProductReadWithRelations,
    summary="Получение Product с brand и category"
)
async def get_product_by_id(product_id: UUID, session: AsyncSession = Depends(get_session)):
    product_dao = ProductDAO(session)
    try:
        product = await product_dao.get_product_with_relations_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
        return product

    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{product_id}", status_code=204, summary="Удаление товара по ID")
async def delete_order(
    product_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    product_dao = ProductDAO(session)
    deleted = await product_dao.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return None

@router.post("/{product_id}/link-attributes", summary="Привязать аттрибуты к продукту")
async def link_attributes_to_product(
    product_id: UUID,
    attributes_links: list[ProductAttributeLink],
    session: AsyncSession = Depends(get_session)
):
    product_dao = ProductDAO(session)
    try:
        updated_product = await product_dao.link_attributes_to_product(product_id, attributes_links)
        return updated_product
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError:
        raise HTTPException(status_code=500, detail="Internal server error")
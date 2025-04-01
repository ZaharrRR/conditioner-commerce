import asyncio
from uuid import UUID

from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.params import Depends, File
from sqlalchemy.ext.asyncio import AsyncSession

from core import get_api_key
from dao.product import ProductDAO
from db.database import get_session
from schemas import ProductRead, ProductCreate, ProductReadWithRelations, ProductAttributeLink, ProductAttributeDelete
from services.s3 import S3Service
from utils.utils import validate_logo

router = APIRouter(prefix="/product", tags=["Products"])

def get_s3_service() -> S3Service:
    return S3Service()


@router.post(
    "/create",
    response_model=ProductRead,
    summary="Создание Product",
    status_code=201,
    dependencies=[Depends(get_api_key)]
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

@router.post("/update-photo/{product_id}", status_code=201, response_model=ProductReadWithRelations, dependencies=[Depends(get_api_key)])
async def upload_product_photo(
        product_id: UUID,
        photo_file: UploadFile = File(...),
        session: AsyncSession = Depends(get_session),
        s3: S3Service = Depends(get_s3_service)):

    product_dao = ProductDAO(session)
    photo_url = ''
    try:
        if photo_file:
            key, content = await validate_logo(photo_file, 'products')
            photo_url = await asyncio.to_thread(s3.upload_file, content, key)
            print(photo_url)
        updated_product = await product_dao.update_product_photo(product_id, photo_url)
        return updated_product
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/new-products", status_code=200)
async def get_new_products(session: AsyncSession = Depends(get_session)):
    product_dao = ProductDAO(session)
    try:
        products = await product_dao.get_new_products()
        return products
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    '/all',
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
    summary="Получение Product с brand и category",
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


@router.delete("/{product_id}", status_code=204, summary="Удаление товара по ID", dependencies=[Depends(get_api_key)])
async def delete_order(
    product_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    product_dao = ProductDAO(session)
    deleted = await product_dao.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return None

@router.post("/{product_id}/link-attributes", summary="Привязать аттрибуты к продукту", dependencies=[Depends(get_api_key)])
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

@router.delete("/", status_code=204, summary="Удалить аттрибут у продукта", dependencies=[Depends(get_api_key)])
async def delete_product_attribute(
    data: ProductAttributeDelete,
    session: AsyncSession = Depends(get_session),
):
    dao = ProductDAO(session)
    try:
        success = await dao.delete_attribute_from_product(data)
        if not success:
            raise HTTPException(
                status_code=404,
                detail="Связь аттрибута с продуктом не найдена"
            )
    except RuntimeError:
        raise HTTPException(status_code=500, detail="Internal server error")
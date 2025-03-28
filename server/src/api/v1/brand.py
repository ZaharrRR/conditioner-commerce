import asyncio
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi.params import File, Form
from sqlalchemy.ext.asyncio import AsyncSession

from dao import BrandDAO
from db.database import get_session
from schemas import BrandCreate, BrandRead, BrandUpdate
from services.s3 import S3Service
from utils.utils import validate_logo

router = APIRouter(prefix="/brand", tags=["Brand"])


def get_s3_service() -> S3Service:
    return S3Service()


@router.post("/create", response_model=BrandRead, status_code=201)
async def create_brand(
    name: str = Form(...),
    description: str = Form(""),
    logo_file: UploadFile = File(None),
    session: AsyncSession = Depends(get_session),
    s3: S3Service = Depends(get_s3_service)
):
    brand_dao = BrandDAO(session)
    logo_url = ''
    try:
        if logo_file:
            key, content = await validate_logo(logo_file, 'brands')
            logo_url = await asyncio.to_thread(s3.upload_file, content, key)
        brand_data = BrandCreate(name=name, description=description, logo_url=logo_url)
        new_brand = await brand_dao.create_brand(brand_data)
        return new_brand

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/all",
    response_model=list[BrandRead],
    summary="Получение всех записей Brand",
    status_code=200,
)
async def get_all_brands(
    session: AsyncSession = Depends(get_session),
) -> list[BrandRead]:
    brand_dao = BrandDAO(session)
    brands = await brand_dao.get_brands()
    return brands


@router.get(
    "/get-by-id/{brand_id}",
    response_model=BrandRead,
    summary="Получение записи Brand по id",
    status_code=200,
)
async def get_brand_by_id(
    brand_id: UUID, session: AsyncSession = Depends(get_session)
) -> BrandRead:
    brand_dao = BrandDAO(session)
    brand = await brand_dao.get_brand_by_id(brand_id)
    if not brand:
        raise HTTPException(
            status_code=404, detail=f"Brand with id {brand_id} not found"
        )
    return brand


@router.patch(
    "/update-logo/{brand_id}",
    response_model=BrandRead,
    summary="Обновление logo url Brand",
)
async def update_brand_logo(session: AsyncSession = Depends(get_session)) -> BrandRead:
    pass


@router.delete(
    "/delete/{brand_id}",
    response_model=None,
    status_code=204,
    summary="Удаление записи Brand по id",
)
async def delete_brand_by_id(
    brand_id: UUID, session: AsyncSession = Depends(get_session)
) -> HTTPException:
    brand_dao = BrandDAO(session)
    deleted = await brand_dao.delete_brand_by_id(brand_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Brand not found")
    return HTTPException(status_code=204, detail="Brand has been removed")


@router.patch(
    "/update/{brand_id}",
    response_model=BrandRead,
)
async def update_brand_by_id(
    brand_id: UUID,
    brand_update: BrandUpdate,
    session: AsyncSession = Depends(get_session),
) -> BrandRead:
    brand_dao = BrandDAO(session)
    updated_brand = await brand_dao.update_brand(brand_id, brand_update)

    if not updated_brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    return updated_brand

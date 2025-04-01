import asyncio
from uuid import UUID

from fastapi import APIRouter, HTTPException, UploadFile, Depends
from fastapi.params import File, Form
from sqlalchemy.ext.asyncio import AsyncSession

from core import get_api_key
from dao.category import CategoryDAO
from db.database import get_session
from schemas import CategoryCreate, CategoryRead, CategoryUpdate
from services.s3 import S3Service
from utils.utils import validate_logo

router = APIRouter(prefix="/category", tags=["Category"])

def get_s3_service() -> S3Service:
    return S3Service()

@router.post("/create", response_model=CategoryRead, status_code=201, dependencies=[Depends(get_api_key)])
async def create_category(
    name: str = Form(...),
    logo_file: UploadFile = File(None),
    session: AsyncSession = Depends(get_session),
    s3: S3Service = Depends(get_s3_service),
):
    category_dao = CategoryDAO(session)
    logo_url = ''
    try:
        if logo_file:
            key, content = await validate_logo(logo_file, 'categories')
            logo_url = await asyncio.to_thread(s3.upload_file, content, key)
        category_data = CategoryCreate(name=name, logo_url=logo_url)
        new_category = await category_dao.create_category(category_data)
        return new_category

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/all",
    response_model=list[CategoryRead],
    summary="Получение всех записей Category",
    status_code=200,
)
async def get_all_categories(
    session: AsyncSession = Depends(get_session),
) -> list[CategoryRead]:
    category_dao = CategoryDAO(session)
    categories = await category_dao.get_all_categories()
    return categories


@router.get(
    "/get-by-id/{category_id}",
    response_model=CategoryRead,
    summary="Получение записи Category по id",
    status_code=200,
)
async def get_category_by_id(
    category_id: UUID, session: AsyncSession = Depends(get_session)
) -> CategoryRead:
    category_dao = CategoryDAO(session)
    category = await category_dao.get_category_by_id(category_id)
    if not category:
        raise HTTPException(
            status_code=404, detail=f"Category with id {category_id} not found"
        )
    return category


@router.delete(
    "/delete/{category_id}",
    response_model=None,
    status_code=204,
    summary="Удаление записи Category по id",
    dependencies=[Depends(get_api_key)]
)
async def delete_category_by_id(
    category_id: UUID, session: AsyncSession = Depends(get_session)
) -> HTTPException:
    category_dao = CategoryDAO(session)
    deleted = await category_dao.delete_category_by_id(category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return HTTPException(status_code=204, detail="Category has been removed")


@router.patch(
    "/update/{category_id}",
    response_model=CategoryRead,
    dependencies=[Depends(get_api_key)]
)
async def update_category_by_id(
    category_id: UUID,
    category_update: CategoryUpdate,
    session: AsyncSession = Depends(get_session),
) -> CategoryRead:
    category_dao = CategoryDAO(session)
    updated_category = await category_dao.update_category_by_id(category_id, category_update)

    if not updated_category:
        raise HTTPException(status_code=404, detail="Brand not found")
    return updated_category

from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dao.attribute import AttributeDAO
from db.database import get_session
from schemas import AttributeCreate, AttributeRead

router = APIRouter(
    prefix="/attribute",
    tags=["Attributes"],
)


@router.post(
    "/create",
    response_model=AttributeRead,
    status_code=201,
    summary="Создание записи Attribute",
)
async def create_attribute(
    attribute: AttributeCreate, session: AsyncSession = Depends(get_session)
) -> AttributeRead:
    attribute_dao = AttributeDAO(session)
    try:
        new_attribute = await attribute_dao.create_attribute(attribute)
        return new_attribute
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/all",
    response_model=list[AttributeRead],
    summary="Получение всех записей Attribute",
    status_code=200,
)
async def get_all_attributes(
    session: AsyncSession = Depends(get_session),
) -> list[AttributeRead]:
    attribute_dao = AttributeDAO(session)
    attributes = await attribute_dao.get_attributes()
    return attributes


@router.get(
    "/get-by-id/{attribute_id}",
    response_model=AttributeRead,
    summary="Получение Attribute по ID",
    status_code=200,
)
async def get_attribute_by_id(
    attribute_id: UUID, session: AsyncSession = Depends(get_session)
):
    attribute_dao = AttributeDAO(session)
    attribute = await attribute_dao.get_attribute_by_id(attribute_id)
    if not attribute:
        raise HTTPException(
            status_code=404, detail=f"Attribute with id {attribute_id} not found"
        )
    return attribute


@router.delete(
    "/delete/{attribute_id}",
    response_model=None,
    status_code=204,
    summary="Удаление Attribute по id",
)
async def delete_attribute_by_id(
    attribute_id: UUID, session: AsyncSession = Depends(get_session)
) -> HTTPException:
    attribute_dao = AttributeDAO(session)
    deleted = await attribute_dao.delete_attribute_by_id(attribute_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Attribute not found")
    return HTTPException(status_code=204, detail="Attribute has been removed")

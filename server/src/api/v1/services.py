import asyncio

from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from decimal import Decimal
from uuid import UUID

from core import logger, get_api_key
from dao.service import ServiceDAO
from db.database import get_session
from schemas import ServiceRead, ServiceCreate, ServiceUpdate
from services.s3 import S3Service
from utils.utils import validate_logo

router = APIRouter(prefix="/services", tags=["Services"])

def get_s3_service() -> S3Service:
    return S3Service()

@router.post("/create", response_model=ServiceRead, status_code=201, summary="Создание услуги", dependencies=[Depends(get_api_key)])
async def create_service(
    logo_file: UploadFile = File(None),
    service_type: str = Form(...),
    base_price: Decimal = Form(...),
    description: str = Form(None),
    session: AsyncSession = Depends(get_session),
    s3: S3Service = Depends(get_s3_service)
):
    service_dao = ServiceDAO(session)
    logo_url = ''
    try:
        if logo_file:
            key, content = await validate_logo(logo_file, 'services')
            logo_url = await asyncio.to_thread(s3.upload_file, content, key)
        service_data = ServiceCreate(service_type=service_type, base_price=base_price, description=description, logo_url=logo_url)
        new_service = await service_dao.create_service(service_data)
        return new_service
    except ValueError as e:
        logger.warning(f"Ошибка создания услуги: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError:
        logger.error("Ошибка БД при создании услуги")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/get-by-id/{service_id}", response_model=ServiceRead, summary="Получение услуги по ID")
async def get_service_by_id(
    service_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    service_dao = ServiceDAO(session)
    service = await service_dao.get_service_by_id(service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return ServiceRead.model_validate(service)

@router.get("/all", response_model=list[ServiceRead], summary="Получение всех услуг")
async def get_services(session: AsyncSession = Depends(get_session)):
    service_dao = ServiceDAO(session)
    try:
        services = await service_dao.get_all_services()
        return services
    except RuntimeError:
        logger.error("Ошибка БД при получении услуг")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.patch("/update/{service_id}", response_model=ServiceUpdate, summary="Обновление услуги по ID", dependencies=[Depends(get_api_key)])
async def update_service(
    service_id: UUID,
    service_data: ServiceUpdate,
    session: AsyncSession = Depends(get_session)
):
    service_dao = ServiceDAO(session)
    try:
        updated_service = await service_dao.update_service(service_id, service_data)
        if updated_service is None:
            raise HTTPException(status_code=404, detail="Service not found")
        return updated_service
    except ValueError as e:
        logger.warning(f"Ошибка обновления услуги: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError:
        logger.error("Ошибка БД при обновлении услуги")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/delete-by-id/{service_id}", status_code=204, summary="Удаление услуги по ID", dependencies=[Depends(get_api_key)])
async def delete_service(
    service_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    service_dao = ServiceDAO(session)
    deleted = await service_dao.delete_service_by_id(service_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Service not found")
    return None


@router.get("/with-logo", response_model=list[ServiceRead], summary="Получить услуги с логотипами")
async def get_services_with_logo(session: AsyncSession = Depends(get_session)):
    service_dao = ServiceDAO(session)
    try:
        return await service_dao.get_services_with_logo()
    except RuntimeError:
        logger.error("Ошибка при получении услуг с логотипом")
        raise HTTPException(status_code=500, detail="Internal server error")
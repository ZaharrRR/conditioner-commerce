from typing import Optional
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from core import logger

from models import Service
from schemas import ServiceCreate, ServiceRead, ServiceUpdate


class ServiceDAO:
    """DAO для работы со справочником услуг (Service)"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_service(self, service_data: ServiceCreate) -> ServiceRead:
        logger.debug("⚙️ Создание услуги Service")
        try:
            new_service = Service(**service_data.model_dump())
            self.session.add(new_service)
            await self.session.flush()
            await self.session.commit()
            logger.info(f"✅ Услуга Service с ID {new_service.id} создана")
            return ServiceRead.model_validate(new_service, from_attributes=True)
        except IntegrityError:
            await self.session.rollback()
            logger.warning(f"⚠️ Услуга с типом {service_data.service_type} уже существует")
            raise ValueError("Service already exists")
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка при создании услуги Service: {e}")
            raise RuntimeError("Database error")

    async def get_service_by_id(self, service_id: UUID):
        logger.debug(f"🔎 Получение услуги Service с ID: {service_id}")
        try:
            stmt = select(Service).where(Service.id == service_id)
            result = await self.session.execute(stmt)
            service = result.scalar_one_or_none()
            logger.info(f"✅ Услуга Service с ID {service_id} {'найдена' if service else 'не найдена'}")
            return service
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка при получении услуги Service с ID {service_id}: {e}")
            raise RuntimeError("Database error")

    async def get_all_services(self) -> list[ServiceRead]:
        logger.debug("🔎 Получение всех услуг Service")
        try:
            stmt = select(Service)
            result = await self.session.execute(stmt)
            services = result.scalars().all()
            logger.info(f"✅ Найдено {len(services)} услуг")
            return [ServiceRead.model_validate(service, from_attributes=True) for service in services]
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка при получении услуг: {e}")
            raise RuntimeError("Database error")

    async def update_service(self, service_id: UUID, service_update: ServiceUpdate) -> Optional[ServiceRead]:
        """Обновляет Service по ID"""
        logger.debug(f"🔄 Обновление Service с ID {service_id}")
        try:
            service = await self.get_service_by_id(service_id)
            if not service:
                logger.warning(f"⚠️ Service с ID {service_id} не найден")
                return None

            update_data = service_update.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(service, field, value)

            await self.session.flush()
            await self.session.commit()
            await self.session.refresh(service)
            logger.info(f"✅ Запись Service с ID {service_id} обновлена")
            return ServiceRead.model_validate(service, from_attributes=True)
        except IntegrityError:
            await self.session.rollback()
            logger.warning("⚠️ Service с такими данными уже существует")
            raise ValueError("Service already exists")
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка при обновлении Service с ID {service_id}: {e}")
            raise RuntimeError("Database error")

    async def delete_service_by_id(self, service_id: UUID) -> bool:
        logger.debug(f"🗑️ Удаление услуги Service с ID {service_id}")
        try:
            service = await self.get_service_by_id(service_id)
            if service is None:
                logger.warning(f"⚠️ Услуга Service с ID {service_id} не найдена")
                return False
            await self.session.delete(service)
            await self.session.flush()
            await self.session.commit()
            logger.info(f"✅ Услуга Service с ID {service_id} удалена")
            return True
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error(f"❌ Ошибка при удалении услуги Service с ID {service_id}: {e}")
            raise RuntimeError("Database error")
    async def get_services_with_logo(self):
        logger.debug("🔎 Получение услуг Service с заполненным logo_url")
        try:
            stmt = select(Service).where(Service.logo_url.isnot(None)).where(Service.logo_url != "")
            result = await self.session.execute(stmt)
            services = result.scalars().all()
            logger.info(f"✅ Найдено {len(services)} услуг с logo_url")
            return [ServiceRead.model_validate(service, from_attributes=True) for service in services]
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка при получении услуг с logo_url: {e}")
            raise RuntimeError("Database error")
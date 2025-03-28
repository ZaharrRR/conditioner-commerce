from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import Optional, Annotated

from pydantic import BaseModel, Field, ConfigDict, UUID4


class ServiceBase(BaseModel):
    description: Annotated[Optional[str], Field(max_length=300)] = None
    logo_url: Annotated[Optional[str], Field(max_length=300)] = None
    service_type: str = Field(..., description="Тип услуги (например, 'delivery' или 'installation')")
    base_price: Decimal = Field(..., description="Базовая цена услуги")

    model_config = ConfigDict(from_attributes=True)


class ServiceCreate(ServiceBase):
    """Схема для создания услуги"""
    pass


class ServiceUpdate(BaseModel):
    service_type: Optional[str] = Field(..., description="Тип услуги (например, 'delivery' или 'installation')")
    base_price: Optional[Decimal] = Field(..., description="Базовая цена услуги")


class ServiceRead(ServiceBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

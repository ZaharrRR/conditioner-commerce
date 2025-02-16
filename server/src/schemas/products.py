from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=200)]
    price: Annotated[Decimal, Field(gt=0)]
    brand_id: UUID
    category_id: UUID


class ProductCreate(ProductBase):
    """Схема для создания Attribute"""

    pass


class ProductUpdate(BaseModel):
    """Схема для обновления Product"""

    name: Annotated[Optional[str], Field(min_length=1, max_length=200)] = None
    price: Annotated[Optional[Decimal], Field(gt=0)] = None


class ProductRead(ProductBase):
    """Схема для чтения Product"""

    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProductImageBase(BaseModel):
    product_id: UUID
    image_url: Annotated[str, Field(min_length=1, max_length=500)]


class ProductImageCreate(ProductImageBase):
    """Схема для создания ProductImage"""

    pass


class ProductImageRead(ProductImageBase):
    """Схема для чтения ProductImage"""

    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

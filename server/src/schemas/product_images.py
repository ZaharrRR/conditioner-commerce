from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, UUID4


class ProductImageBase(BaseModel):
    product_id: UUID4
    image_url: Annotated[str, Field(min_length=1, max_length=500)]


class ProductImageCreate(ProductImageBase):
    """Схема для создания ProductImage"""

    pass


class ProductImageRead(ProductImageBase):
    """Схема для чтения ProductImage"""

    id: UUID4
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

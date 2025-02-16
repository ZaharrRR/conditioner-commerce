from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProductAttributeBase(BaseModel):
    value: Annotated[str, Field(min_length=1, max_length=255)]
    product_id: UUID
    attribute_id: UUID


class ProductAttributeCreate(ProductAttributeBase):
    """Схема для создания ProductAttribute"""

    pass


class ProductAttributeRead(ProductAttributeBase):
    """Схема для чтения ProductAttribute"""

    model_config = ConfigDict(from_attributes=True)

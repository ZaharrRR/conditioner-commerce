from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, UUID4


class ProductAttributeBase(BaseModel):
    value: Annotated[str, Field(min_length=1, max_length=255)]
    product_id: UUID4
    attribute_id: UUID4


class ProductAttributeCreate(ProductAttributeBase):
    """Схема для создания ProductAttribute"""

    pass

class ProductAttributeLink(BaseModel):
    attribute_id: Annotated[UUID4, Field(..., description="ID аттрибутов, которые нужно привязать")]
    value: Annotated[str, Field(..., description="Значение аттрибута для данного продукта")]


class ProductAttributeRead(BaseModel):
    attribute_name: Annotated[str, Field(..., description="Название аттрибута из модели Attribute")]
    value: Annotated[str, Field(..., description="Значение аттрибута для продукта")]
    model_config = ConfigDict(from_attributes=True)

class ProductAttributeDelete(BaseModel):
    attribute_id: UUID
    product_id: UUID
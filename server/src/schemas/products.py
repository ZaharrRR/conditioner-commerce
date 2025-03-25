from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional


from pydantic import BaseModel, ConfigDict, Field, UUID4

from schemas import ProductAttributeRead


class ProductBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=200, description="Названия продукта")]
    price: Annotated[Decimal, Field(gt=0, description="Цена продукта")]
    description: Annotated[str, Field(..., description="Описание продукта")]
    brand_id: Annotated[UUID4, Field(description="Валидный UUID для Brand")]
    category_id: Annotated[UUID4, Field(description="Валидный UUID для Category")]


class ProductCreate(ProductBase):
    """Схема для создания Attribute"""
    attributes: Annotated[Optional[list[UUID4]], Field(default_factory=list, description="Список UUID аттрибутов")] = []


class ProductUpdate(BaseModel):
    """Схема для обновления Product"""

    name: Annotated[Optional[str], Field(min_length=1, max_length=200)] = None
    price: Annotated[Optional[Decimal], Field(gt=0)] = None


class ProductRead(ProductBase):
    """Схема для чтения Product"""

    id: UUID4
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductReadWithRelations(BaseModel):
    id: UUID4
    name: Annotated[str, Field(...)]
    price: Annotated[Decimal, Field(...)]
    brand_name: Annotated[str, Field(...)]
    category_name: Annotated[str, Field(...)]
    attributes: Annotated[Optional[list[ProductAttributeRead]], Field(None, description="Список характеристик (аттрибутов) продукта")]
    created_at: datetime
    updated_at: datetime
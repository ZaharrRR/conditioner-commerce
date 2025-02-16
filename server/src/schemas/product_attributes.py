from typing import Annotated


from pydantic import BaseModel, ConfigDict, Field, UUID4


class ProductAttributeBase(BaseModel):
    value: Annotated[str, Field(min_length=1, max_length=255)]
    product_id: UUID4
    attribute_id: UUID4


class ProductAttributeCreate(ProductAttributeBase):
    """Схема для создания ProductAttribute"""

    pass


class ProductAttributeRead(ProductAttributeBase):
    """Схема для чтения ProductAttribute"""

    model_config = ConfigDict(from_attributes=True)

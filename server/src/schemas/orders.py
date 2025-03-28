import re
import uuid
from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import Field, BaseModel, ConfigDict, field_validator

from schemas import ProductReadWithRelations

PHONE_REGEX = r"^\+7\d{10}$"



class OrderBase(BaseModel):
    product_id: UUID
    customer_name: str = Field(..., min_length=2, max_length=100, description="Имя клиента")
    customer_surname: str = Field(..., min_length=2, max_length=100, description="Фамилия клиента")
    customer_phone: str = Field(..., description="Номер телефона (форматы +7XXXXXXXXXX или 8XXXXXXXXXX)"
    )
    total_price: Decimal
    address: str = Field(..., min_length=5, max_length=300, description="Адрес доставки")
    comment: Optional[str] = Field(None, description="Комментарий клиента")

    @field_validator("customer_phone", mode="before")
    def normalize_phone(cls, v: str) -> str:
        # Если номер начинается с '8', преобразуем его в формат '+7'
        if isinstance(v, str) and v.startswith("8"):
            return "+7" + v[1:]
        return v

    @field_validator("customer_phone", mode="after")
    def validate_phone(cls, v: str) -> str:
        if not re.match(PHONE_REGEX, v):
            raise ValueError("Номер телефона должен быть в формате +7XXXXXXXXXX")
        return v

    model_config = ConfigDict(from_attributes=True)






class OrderServiceRead(BaseModel):
    id: UUID = Field(..., description="ID услуги")
    service_type: str = Field(..., description="Тип услуги (например, 'delivery' или 'installation')")
    base_price: Decimal = Field(..., description="Цена услуги")
    created_at: datetime = Field(..., description="Дата создания записи услуги")

    model_config = ConfigDict(from_attributes=True)

class OrderRead(BaseModel):
    id: UUID = Field(..., description="ID заказа")
    customer_name: str = Field(..., min_length=2, max_length=100, description="Имя клиента")
    customer_surname: str = Field(..., min_length=2, max_length=100, description="Фамилия клиента")
    customer_phone: str = Field(..., description="Номер телефона (форматы +7XXXXXXXXXX или 8XXXXXXXXXX)")
    address: str = Field(..., min_length=5, max_length=300, description="Адрес доставки")
    comment: Optional[str] = Field(None, description="Комментарий клиента")
    total_price: Decimal = Field(..., description="Итоговая цена заказа с учетом услуг")
    created_at: datetime = Field(..., description="Дата создания заказа")
    services: Optional[list[OrderServiceRead]] = Field(
        default_factory=list, description="Подробная информация о дополнительных услугах"
    )
    product: "ProductReadWithRelations" = Field(description="Товары")

    model_config = ConfigDict(from_attributes=True)

class OrderServiceCreate(BaseModel):
    id: UUID


class OrderCreate(OrderBase):
    services: Optional[list[uuid.UUID]] = Field(
        default_factory=list
    )
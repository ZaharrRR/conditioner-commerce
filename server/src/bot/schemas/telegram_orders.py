from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4, ConfigDict




class TelegramOrderService(BaseModel):
    service_id: UUID4
    name: str
    price: float

class TelegramOrderCreate(BaseModel):
    customer_name: Optional[str] = None
    customer_phone: str
    address: str
    total_price: float
    services: list[]

class TelegramOrderRead(BaseModel):
    id: UUID4
    customer_name: Optional[str]
    customer_phone: str
    address: str
    total_price: float
    services: list[]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
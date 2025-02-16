from datetime import datetime
from typing import Annotated, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class AttributeBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=500)]


class AttributeCreate(AttributeBase):
    """Схема для чтения Attribute"""

    pass


class AttributeUpdate(AttributeBase):
    """Схема для обновления Attribute"""

    name: Annotated[Optional[str], Field(min_length=1, max_length=500)] = None


class AttributeRead(AttributeBase):
    """Схема для чтения Attribute"""

    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

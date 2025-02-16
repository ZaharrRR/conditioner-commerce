from datetime import datetime
from typing import Annotated, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class BrandBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=100)]
    description: Annotated[Optional[str], Field(max_length=200)] = None
    logo_url: Annotated[Optional[str], Field(max_length=300)] = None


class BrandCreate(BrandBase):
    """Схема для создания Brand"""

    pass


class BrandUpdate(BrandBase):
    """Схема для обновления Brand"""

    name: Annotated[Optional[str], Field(min_length=1, max_length=100)] = None
    description: Annotated[Optional[str], Field(max_length=200)] = None
    logo_url: Annotated[Optional[str], Field(max_length=300)] = None


class BrandRead(BrandBase):
    """Схема для чтения Brand"""

    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

from datetime import datetime
from typing import Annotated, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class CategoryBase(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=225)]
    logo_url: Annotated[Optional[str], Field(max_length=300)] = None


class CategoryCreate(CategoryBase):
    """Схема для создания Category"""

    pass


class CategoryUpdate(CategoryBase):
    """Схема для обновления Category"""

    name: Annotated[Optional[str], Field(min_length=1, max_length=225)] = None
    logo_url: Annotated[Optional[str], Field(max_length=300)] = None


class CategoryRead(CategoryBase):
    """Схема для чтения Category"""

    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

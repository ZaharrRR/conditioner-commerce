import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class ProductImage(Base):
    __tablename__ = "product_images"
    product_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("products.id"), nullable=False
    )
    image_url: Mapped[str] = mapped_column(String(500), nullable=False)

    # Связь
    product: Mapped["Product"] = relationship("Product", back_populates="images")

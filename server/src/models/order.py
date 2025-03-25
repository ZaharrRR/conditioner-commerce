from uuid import UUID

from sqlalchemy import String, Numeric, Text, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from decimal import Decimal

from db import Base


class Order(Base):
    """Модель заявки в базе данных"""
    product_id: Mapped[UUID] = mapped_column(ForeignKey('products.id'), nullable=False)
    customer_name: Mapped[str] = mapped_column(String, nullable=False)
    customer_surname: Mapped[str] = mapped_column(String, nullable=False)
    customer_phone: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)

    base_price: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    total_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    comment: Mapped[str] = mapped_column(Text, nullable=False)

    product: Mapped["Product"] = relationship("Product", back_populates="orders")

    order_services: Mapped[list["OrderService"]] = relationship(
        "OrderService", back_populates="order", cascade="all, delete-orphan"
    )
    services: Mapped[list["Service"]] = relationship(
        "Service",
        secondary="order_services",
        viewonly=True
    )
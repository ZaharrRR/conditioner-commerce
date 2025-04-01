from decimal import Decimal

from sqlalchemy import String, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column

from db import Base



class Service(Base):
    """Модель Service в БД"""
    __tablename__ = "services"
    logo_url: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    service_type: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    base_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    order_services: Mapped[list["OrderService"]] = relationship(
        "OrderService", back_populates="service", cascade="all, delete-orphan"
    )

    orders: Mapped[list["Order"]] = relationship(
        "Order",
        secondary="order_services",
        viewonly=True
    )

    telegram_order_services: Mapped[list["TelegramOrderService"]] = relationship(
        "TelegramOrderService", back_populates="service", cascade="all, delete-orphan"
    )

    telegram_orders: Mapped[list["TelegramOrder"]] = relationship(
        "TelegramOrder",
        secondary="telegram_order_services",
        viewonly=True
    )
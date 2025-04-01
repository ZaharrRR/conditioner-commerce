from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Base


class TelegramOrder(Base):

    __tablename__ = "telegram_orders"

    customer_name: Mapped[str] = mapped_column(String(100), nullable=True)
    customer_phone: Mapped[str] = mapped_column(String(15), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    total_price: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)

    telegram_order_services: Mapped[list["TelegramOrderService"]] = relationship(
        "TelegramOrderService", back_populates="telegram_order", cascade="all, delete-orphan")

    services: Mapped[list["Service"]] = relationship(
        "Service",
        secondary="telegram_order_services",
        viewonly=True
    )
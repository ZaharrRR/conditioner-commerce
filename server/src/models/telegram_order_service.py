from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from db import Base


class TelegramOrderService(Base):
    __tablename__ = "telegram_order_services"

    order_id: Mapped[UUID] = mapped_column(
        ForeignKey("telegram_orders.id"), primary_key=True
    )
    service_id: Mapped[UUID] = mapped_column(
        ForeignKey("services.id"), primary_key=True
    )
    total_price: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=True)


    telegram_order: Mapped["TelegramOrder"] = relationship(
        "TelegramOrder", back_populates="telegram_order_services"
    )

    service: Mapped["Service"] = relationship(
        "Service", back_populates="telegram_order_services"
    )
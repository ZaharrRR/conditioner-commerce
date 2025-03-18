from decimal import Decimal

from uuid import UUID

from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from db import Base


class OrderService(Base):
    """Модель дополнительных услуг в заказе"""

    __tablename__ = "order_services"
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"), primary_key=True)
    service_id: Mapped[UUID] = mapped_column(ForeignKey("services.id"), primary_key=True)
    custom_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=True)

    order: Mapped["Order"] = relationship("Order", back_populates="order_services")
    service: Mapped["Service"] = relationship("Service", back_populates="order_services")
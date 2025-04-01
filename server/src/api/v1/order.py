from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from bot.notify.notify import notify_orders_admins
from core import logger, get_api_key
from dao.order import OrderDAO
from db.database import get_session
from schemas.orders import OrderRead, OrderCreate

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", status_code=201, summary="Создание заказа")
async def create_order(
    order_data: OrderCreate,
    session: AsyncSession = Depends(get_session)
):
    order_dao = OrderDAO(session)
    try:
        new_order = await order_dao.create_order(order_data)
        await notify_orders_admins(new_order)
        return new_order
    except ValueError as e:
        logger.warning(f"Ошибка создания заказа: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError:
        logger.error("Ошибка БД при создании заказа")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{order_id}", response_model=OrderRead, summary="Получение заказа по ID")
async def get_order(
    order_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    order_dao = OrderDAO(session)
    order = await order_dao.get_order_by_id(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/", summary="Получение всех заказов")
async def get_orders(session: AsyncSession = Depends(get_session)):
    order_dao = OrderDAO(session)
    try:
        orders = await order_dao.get_orders()
        return orders
    except RuntimeError:
        logger.error("Ошибка БД при получении заказов")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{order_id}", status_code=204, summary="Удаление заказа по ID", dependencies=[Depends(get_api_key)])
async def delete_order(
    order_id: UUID,
    session: AsyncSession = Depends(get_session)
):
    order_dao = OrderDAO(session)
    deleted = await order_dao.delete_order_by_id(order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return None
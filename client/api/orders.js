import { handleError, api } from "~/api/http";

const fetchAllOrders = async () => {
  try {
    const response = await api.get("/orders/");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки заказов");
  }
};

const createOrder = async (orderData) => {
  try {
    const response = await api.post("/orders/", orderData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания заказа");
  }
};

const getOrderById = async (orderId) => {
  try {
    const response = await api.get(`/orders/${orderId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки заказа");
  }
};

const deleteOrder = async (orderId) => {
  try {
    const response = await api.delete(`/orders/${orderId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка удаления заказа");
  }
};

export { fetchAllOrders, getOrderById, createOrder, deleteOrder };

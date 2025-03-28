import axios from "axios";

import { handleError } from "~/api/http/errorHandler";

const api = axios.create({
  baseURL: "http://localhost:3000/orders",
  headers: {
    "Content-Type": "application/json",
  },
});

const fetchAllOrders = async () => {
  try {
    const response = await api.get("/");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки заказов");
  }
};

const createOrder = async (orderData) => {
  try {
    const response = await api.post("/", orderData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания заказа");
  }
};

const getOrderById = async (orderId) => {
  try {
    const response = await api.get(`/${orderId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки заказа");
  }
};

const deleteOrder = async (orderId) => {
  try {
    const response = await api.delete(`/${orderId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка удаления заказа");
  }
};

export { fetchAllOrders, getOrderById, createOrder, deleteOrder };

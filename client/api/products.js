import axios from "axios";

import { handleError } from "~/api/http/errorHandler";

const api = axios.create({
  baseURL: "http://localhost:3000/product",
  headers: {
    "Content-Type": "application/json",
  },
});

const createProduct = async (productData) => {
  try {
    const response = await api.post("/create", productData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания продукта");
  }
};

const updateProductPhoto = async (productId, file) => {
  try {
    const response = await api.post(`/update-photo/${productId}`, file);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка обновления фото продукта");
  }
};

const fetchAllProducts = async () => {
  try {
    const response = await api.get("/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки продуктов");
  }
};

const getProductById = async (productId) => {
  try {
    const response = await api.get(`/get-by-id/${productId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения продукта");
  }
};

const getNewProducts = async () => {
  try {
    const response = await api.get(`/new-products`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения новых продуктов");
  }
};

const deleteProduct = async (productId) => {
  try {
    const response = await api.delete(`/${productId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка удаления продукта");
  }
};

const linkProductAttributes = async (productId, attributesData) => {
  try {
    const response = await api.post(
      `/${productId}/link-attributes`,
      attributesData
    );
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка привязки атрибутов");
  }
};

export {
  fetchAllProducts,
  getProductById,
  getNewProducts,
  createProduct,
  updateProductPhoto,
  deleteProduct,
  linkProductAttributes,
};

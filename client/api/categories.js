import axios from "axios";

import { handleError } from "~/api/http/errorHandler";

const api = axios.create({
  baseURL: "http://localhost:3000/category",
  headers: {
    "Content-Type": "application/json",
  },
});

const fetchAllCategories = async () => {
  try {
    const response = await api.get("/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки категорий");
  }
};

const createCategory = async (categoryData) => {
  try {
    const response = await api.post("/create", categoryData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания категории");
  }
};

const getCategoryById = async (categoryId) => {
  try {
    const response = await api.get(`/get-by-id/${categoryId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения категории");
  }
};

const updateCategory = async (categoryId, updateData) => {
  try {
    const response = await api.patch(`/update/${categoryId}`, updateData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка обновления категории");
  }
};

const deleteCategory = async (categoryId) => {
  try {
    await api.delete(`/delete/${categoryId}`);
  } catch (error) {
    return handleError(error, "Ошибка удаления категории");
  }
};

export {
  fetchAllCategories,
  getCategoryById,
  createCategory,
  updateCategory,
  deleteCategory,
};

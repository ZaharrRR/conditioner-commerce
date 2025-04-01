import { apiMulti, handleError, api } from "~/api/http";

const fetchAllCategories = async () => {
  try {
    const response = await api.get("/category/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки категорий");
  }
};

const createCategory = async (categoryData) => {
  try {
    const response = await apiMulti.post(`/category/create`, categoryData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания категории");
  }
};

const getCategoryById = async (categoryId) => {
  try {
    const response = await api.get(`/category/get-by-id/${categoryId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения категории");
  }
};

const updateCategory = async (categoryId, updateData) => {
  try {
    const response = await api.patch(
      `/category/update/${categoryId}`,
      updateData
    );
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка обновления категории");
  }
};

const deleteCategory = async (categoryId) => {
  try {
    await api.delete(`/category/delete/${categoryId}`);
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

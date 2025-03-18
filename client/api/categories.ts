import type { ICategory } from "@/types/category";

import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:3000/",
  headers: {
    "Content-Type": "application/json",
  },
});

const handleError = (error: unknown, defaultMessage: string): Error => {
  if (axios.isAxiosError(error)) {
    return new Error(
      error.response?.data?.message ||
        error.response?.data?.error ||
        defaultMessage
    );
  }
  return new Error(defaultMessage);
};

export const fetchAllCategories = async (): Promise<ICategory[] | Error> => {
  try {
    const response = await api.get<ICategory[]>("/category/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки категорий");
  }
};

export const createCategory = async (
  categoryData: Omit<ICategory, "id" | "created_at" | "updated_at">
): Promise<ICategory | Error> => {
  try {
    const response = await api.post<ICategory>(
      "/category/create",
      categoryData
    );
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания категории");
  }
};

export const getCategoryById = async (
  categoryId: string
): Promise<ICategory | Error> => {
  try {
    const response = await api.get<ICategory>(
      `/category/get-by-id/${categoryId}`
    );
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения категории");
  }
};

export const updateCategory = async (
  categoryId: string,
  updateData: Partial<ICategory>
): Promise<ICategory | Error> => {
  try {
    const response = await api.patch<ICategory>(
      `/category/update/${categoryId}`,
      updateData
    );
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка обновления категории");
  }
};

export const deleteCategory = async (
  categoryId: string
): Promise<void | Error> => {
  try {
    await api.delete(`/category/delete/${categoryId}`);
  } catch (error) {
    return handleError(error, "Ошибка удаления категории");
  }
};

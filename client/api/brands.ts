import type { IBrand } from "@/types/brand";

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

// Получение всех брендов
export const fetchAllBrands = async (): Promise<IBrand[] | Error> => {
  try {
    const response = await api.get<IBrand[]>("/brand/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки брендов");
  }
};

// Создание нового бренда
export const createBrand = async (
  brandData: Omit<IBrand, "id" | "created_at" | "updated_at">
): Promise<IBrand | Error> => {
  try {
    const response = await api.post<IBrand>("/brand/create", brandData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания бренда");
  }
};

// Получение бренда по ID
export const getBrandById = async (
  brandId: string
): Promise<IBrand | Error> => {
  try {
    const response = await api.get<IBrand>(`/brand/get-by-id/${brandId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения бренда");
  }
};

// Обновление бренда
export const updateBrand = async (
  brandId: string,
  updateData: Partial<IBrand>
): Promise<IBrand | Error> => {
  try {
    const response = await api.patch<IBrand>(
      `/brand/update/${brandId}`,
      updateData
    );
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка обновления бренда");
  }
};

// Обновление логотипа бренда
export const updateBrandLogo = async (
  brandId: string,
  logoUrl: string
): Promise<IBrand | Error> => {
  try {
    const response = await api.patch<IBrand>(`/brand/update-logo/${brandId}`, {
      logoUrl,
    });
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка обновления логотипа");
  }
};

// Удаление бренда
export const deleteBrand = async (brandId: string): Promise<void | Error> => {
  try {
    await api.delete(`/brand/delete/${brandId}`);
  } catch (error) {
    return handleError(error, "Ошибка удаления бренда");
  }
};

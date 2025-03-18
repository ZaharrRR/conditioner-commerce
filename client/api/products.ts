import type { IProduct } from "@/types/product";
import type { IBrand } from "@/types/brand";
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

export const createProduct = async (
  productData: Omit<IProduct, "id" | "created_at" | "updated_at">
): Promise<IProduct | Error> => {
  try {
    const response = await api.post<IProduct>("/product/create", productData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания продукта");
  }
};

export const fetchAllProducts = async (): Promise<IProduct[] | Error> => {
  try {
    const response = await api.get<IProduct[]>("/product/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки продуктов");
  }
};

export const getProductById = async (
  productId: string
): Promise<
  | (IProduct & {
      brand: IBrand;
      category: ICategory;
    })
  | Error
> => {
  try {
    const response = await api.get<
      IProduct & {
        brand: IBrand;
        category: ICategory;
      }
    >(`/product/get-by-id/${productId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения продукта");
  }
};

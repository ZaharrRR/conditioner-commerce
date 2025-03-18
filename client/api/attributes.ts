import type { IAttribute } from "@/types/attribute";

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

export const fetchAllAttributes = async (): Promise<IAttribute[] | Error> => {
  try {
    const response = await api.get<IAttribute[]>("/attribute/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки атрибутов");
  }
};

export const createAttribute = async (
  name: string
): Promise<IAttribute | Error> => {
  try {
    const response = await api.post<IAttribute>("/attribute/create", { name });
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания атрибута");
  }
};

export const deleteAttribute = async (id: string): Promise<void | Error> => {
  try {
    await api.delete(`/attribute/delete/${id}`);
  } catch (error) {
    return handleError(error, "Ошибка удаления атрибута");
  }
};

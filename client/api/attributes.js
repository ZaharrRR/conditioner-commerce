import axios from "axios";

import { handleError } from "@/api/http/errorHandler";

const api = axios.create({
  baseURL: "http://localhost:3000/attribute",
  headers: {
    "Content-Type": "application/json",
  },
});

const fetchAllAttributes = async () => {
  try {
    const response = await api.get("/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки атрибутов");
  }
};

const getAttributeById = async (attributeId) => {
  try {
    const response = await api.get(`/get-by-id/${attributeId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки атрибутов");
  }
};

const createAttribute = async (name) => {
  try {
    const response = await api.post("/create", { name });
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания атрибута");
  }
};

const deleteAttribute = async (attributeId) => {
  try {
    await api.delete(`/delete/${attributeId}`);
  } catch (error) {
    return handleError(error, "Ошибка удаления атрибута");
  }
};

export {
  fetchAllAttributes,
  getAttributeById,
  createAttribute,
  deleteAttribute,
};

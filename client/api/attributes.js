import { api, handleError, adminApiKey } from "~/api/http";

const fetchAllAttributes = async () => {
  try {
    const response = await api.get("/attribute/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки атрибутов");
  }
};

const getAttributeById = async (attributeId) => {
  try {
    const response = await api.get(`/attribute/get-by-id/${attributeId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки атрибутов");
  }
};

const createAttribute = async (name) => {
  try {
    const response = await api.post("/attribute/create", { name });
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания атрибута");
  }
};

const deleteAttribute = async (attributeId) => {
  try {
    await api.delete(`/attribute/delete/${attributeId}`);
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

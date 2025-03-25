import axios from "axios";
import { handleError } from "~/api/http/errorHandler";

const api = axios.create({
  baseURL: "http://localhost:3000/services",
  headers: {
    "Content-Type": "application/json",
  },
});

const fetchAllServices = async () => {
  try {
    const response = await api.get("/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения списка услуг");
  }
};

const getServiceById = async (serviceId) => {
  try {
    const response = await api.get(`/get-by-id/${serviceId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения услуги");
  }
};

const createService = async (serviceData) => {
  try {
    const response = await api.post("/create", serviceData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания услуги");
  }
};

const updateService = async (serviceId, updateData) => {
  try {
    const response = await api.patch(`/update/${serviceId}`, updateData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка обновления услуги");
  }
};

const deleteService = async (serviceId) => {
  try {
    const response = await api.delete(`/delete-by-id/${serviceId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка удаления услуги");
  }
};

export {
  createService,
  getServiceById,
  fetchAllServices,
  updateService,
  deleteService,
};

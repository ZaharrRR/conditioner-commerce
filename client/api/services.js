import { handleError, api, apiMulti } from "~/api/http";

const fetchAllServices = async () => {
  try {
    const response = await api.get("/services/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения списка услуг");
  }
};

const getServiceWithLogo = async () => {
  try {
    const response = await api.get(`/services/with-logo`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения услуг");
  }
};

const getServiceById = async (serviceId) => {
  try {
    const response = await api.get(`/services/get-by-id/${serviceId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения услуги");
  }
};

const createService = async (serviceData) => {
  try {
    const response = await apiMulti.post(`/services/create`, serviceData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания услуги");
  }
};

const updateService = async (serviceId, updateData) => {
  try {
    const response = await api.patch(
      `/services/update/${serviceId}`,
      updateData
    );
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка обновления услуги");
  }
};

const deleteService = async (serviceId) => {
  try {
    const response = await api.delete(`/services/delete-by-id/${serviceId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка удаления услуги");
  }
};

export {
  createService,
  getServiceById,
  getServiceWithLogo,
  fetchAllServices,
  updateService,
  deleteService,
};

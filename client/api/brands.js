import { handleError, api, apiMulti } from "~/api/http";

const fetchAllBrands = async () => {
  try {
    const response = await api.get("/brand/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки брендов");
  }
};

const createBrand = async (brandData) => {
  try {
    const response = await apiMulti.post(`/brand/create`, brandData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания бренда");
  }
};

const getBrandById = async (brandId) => {
  try {
    const response = await api.get(`/brand/get-by-id/${brandId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения бренда");
  }
};

const updateBrand = async (brandId, updateData) => {
  try {
    const response = await api.patch(`/brand/update/${brandId}`, updateData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка обновления бренда");
  }
};

const updateBrandLogo = (brandId, formData) => {
  return apiMulti.patch(`/brand/update-logo/${brandId}`, formData);
};

const deleteBrand = async (brandId) => {
  try {
    await api.delete(`/brand/delete/${brandId}`);
  } catch (error) {
    return handleError(error, "Ошибка удаления бренда");
  }
};

export {
  fetchAllBrands,
  getBrandById,
  createBrand,
  updateBrand,
  updateBrandLogo,
  deleteBrand,
};

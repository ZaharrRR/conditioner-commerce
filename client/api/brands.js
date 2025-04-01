import axios from "axios";

import { handleError } from "~/api/http/errorHandler";

const api = axios.create({
  baseURL: "http://localhost:3000/",
  headers: {
    "Content-Type": "application/json",
  },
});

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
    const response = await api.post("/brand/create", brandData);
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
  return axios.patch(
    `http://localhost:3000/brand/update-logo/${brandId}`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data", // Важно!
      },
    }
  );
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

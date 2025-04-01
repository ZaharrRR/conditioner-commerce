import { handleError, api, apiMulti } from "~/api/http";

const createProduct = async (productData) => {
  try {
    const response = await api.post("/product/create", productData);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка создания продукта");
  }
};

const updateProductPhoto = (productId, formData) => {
  return apiMulti.post(`/product/update-photo/${productId}`, formData);
};

const fetchAllProducts = async () => {
  try {
    const response = await api.get("/product/all");
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка загрузки продуктов");
  }
};

const getProductById = async (productId) => {
  try {
    const response = await api.get(`/product/get-by-id/${productId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения продукта");
  }
};

const getNewProducts = async () => {
  try {
    const response = await api.get(`/product/new-products`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка получения новых продуктов");
  }
};

const deleteProduct = async (productId) => {
  try {
    const response = await api.delete(`/product/${productId}`);
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка удаления продукта");
  }
};

const deleteProductAttribut = async (productId, attribute_name) => {
  try {
    console.log(productId);
    console.log(attribute_name);

    const response = await api.delete(`/product/`, {
      name: attribute_name,
      product_id: productId,
    });
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка удаления атрибута");
  }
};

const linkProductAttributes = async (productId, attributesData) => {
  try {
    const response = await api.post(
      `/product/${productId}/link-attributes`,
      attributesData
    );
    return response.data;
  } catch (error) {
    return handleError(error, "Ошибка привязки атрибутов");
  }
};

export {
  fetchAllProducts,
  getProductById,
  getNewProducts,
  createProduct,
  updateProductPhoto,
  deleteProduct,
  deleteProductAttribut,
  linkProductAttributes,
};

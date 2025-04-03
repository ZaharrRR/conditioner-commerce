import axios from "axios";

export let adminApiKey = null;

export const host = "https://api.xn--80acj1aaqbbwm7a3h.xn--p1ai";

export const setAdminApiKey = (key) => {
  adminApiKey = key;
};

export const getAdminApiKey = () => {
  return adminApiKey;
};

export const clearAdminApiKey = () => {
  adminApiKey = null;
};

export const checkApiKey = async (apiKey) => {
  try {
    const response = await axios.get(
      `${host}/auth/check-key`,

      {
        headers: {
          "X-API-KEY": apiKey,
        },
      }
    );
    return response;
  } catch (error) {
    return handleError(error, "Ошибка проверки ключа");
  }
};

export const handleError = (error, defaultMessage) => {
  if (axios.isAxiosError(error)) {
    return new Error(
      error.response?.data?.message ||
        error.response?.data?.error ||
        defaultMessage
    );
  }
  return new Error(defaultMessage);
};

export const api = axios.create({
  baseURL: `${host}`,
  headers: {
    "Content-Type": "application/json",
  },
});

export const apiMulti = axios.create({
  baseURL: `${host}`,
  headers: {
    "Content-Type": "multipart/form-data",
  },
});

// Добавляем перехватчик для всех запросов
const addApiKeyInterceptor = (instance) => {
  instance.interceptors.request.use((config) => {
    if (adminApiKey) {
      config.headers["X-API-KEY"] = adminApiKey;
    }
    return config;
  });
};

addApiKeyInterceptor(api);
addApiKeyInterceptor(apiMulti);

<template>
  <div v-if="isVisible" class="modal-overlay">
    <div class="modal-container">
      <div class="modal-header">
        <h3>Введите API-ключ для доступа</h3>
      </div>

      <div class="modal-body">
        <form @submit.prevent="handleSubmit">
          <div class="input-group">
            <label for="apiKey">API-ключ:</label>
            <input
              id="apiKey"
              v-model="apiKey"
              type="password"
              placeholder="Введите ваш API-ключ"
              required
              autocomplete="off"
            />
          </div>

          <div v-if="errorMessage" class="error-message">
            {{ errorMessage }}
          </div>

          <div class="modal-footer">
            <button type="submit" class="submit-button" :disabled="isLoading">
              <span v-if="isLoading">Проверка...</span>
              <span v-else>Подтвердить</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  isVisible: {
    type: Boolean,
    required: true,
  },
});

const emit = defineEmits(["success"]);

import { checkApiKey, setAdminApiKey } from "~/api/http";

const apiKey = ref("");
const errorMessage = ref("");
const isLoading = ref(false);

const handleSubmit = async () => {
  if (!apiKey.value) {
    errorMessage.value = "Пожалуйста, введите API-ключ";
    return;
  }

  isLoading.value = true;
  errorMessage.value = "";

  try {
    const response = await checkApiKey(apiKey.value);

    const isValid = response.status == 200;

    if (isValid) {
      setAdminApiKey(apiKey.value);
      localStorage.setItem("adminApiKey", apiKey.value);

      emit("success");
    } else {
      errorMessage.value = "Неверный API-ключ";
    }
  } catch (error) {
    errorMessage.value = "Ошибка при проверке ключа";
    console.error("API key verification error:", error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-container {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 450px;
  overflow: hidden;
}

.modal-header {
  padding: 16px 20px;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  margin: 0;
  font-size: 1.2rem;
  color: #333;
}

.close-button {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #666;
  padding: 0;
  line-height: 1;
}

.close-button:hover {
  color: #333;
}

.modal-body {
  padding: 20px;
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #444;
}

.input-group input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.input-group input:focus {
  outline: none;
  border-color: #4a90e2;
  box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2);
}

.error-message {
  color: #e74c3c;
  margin-bottom: 16px;
  font-size: 0.9rem;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
}

.submit-button {
  background-color: #4a90e2;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.submit-button:hover:not(:disabled) {
  background-color: #3a7bc8;
}

.submit-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>

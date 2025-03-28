<template>
  <NuxtLayout name="admin-layout" class="service-management">
    <h1 class="service-management__title">Управление услугами</h1>

    <div class="service-management__create-form">
      <h2 class="service-management__form-title">Добавить услугу</h2>
      <div class="service-management__form-content">
        <input
          v-model="newService.service_type"
          placeholder="Тип услуги"
          class="service-management__input"
        />
        <input
          v-model="newService.base_price"
          type="number"
          step="0.01"
          placeholder="Базовая цена"
          class="service-management__input"
        />
        <button @click="handleCreate" class="service-management__submit-btn">
          Добавить
        </button>
      </div>
    </div>

    <div v-if="error" class="service-management__error">{{ error }}</div>

    <div v-else class="service-management__list">
      <div
        v-for="service in services"
        :key="service.id"
        class="service-management__item"
      >
        <div class="service-management__info">
          <span class="service-management__type">{{
            service.service_type
          }}</span>
          <span class="service-management__price"
            >{{ service.base_price }} ₽</span
          >
        </div>

        <div class="service-management__actions">
          <button
            @click="editService = { ...service }"
            class="service-management__edit-btn"
          >
            Изменить
          </button>
          <button
            @click="handleDelete(service.id)"
            class="service-management__delete-btn"
          >
            Удалить
          </button>
        </div>
      </div>
    </div>

    <div v-if="editService" class="service-management__modal">
      <div class="service-management__modal-content">
        <h2 class="service-management__modal-title">Редактирование услуги</h2>
        <input
          v-model="editService.service_type"
          class="service-management__modal-input"
        />
        <input
          v-model="editService.base_price"
          type="number"
          step="0.01"
          class="service-management__modal-input"
        />
        <div class="service-management__modal-actions">
          <button @click="handleUpdate" class="service-management__modal-save">
            Сохранить
          </button>
          <button
            @click="editService = null"
            class="service-management__modal-cancel"
          >
            Отмена
          </button>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import {
  fetchAllServices,
  createService,
  updateService,
  deleteService,
} from "@/api/services";

const services = ref([]);
const editService = ref(null);
const error = ref(null);

const newService = reactive({
  service_type: "",
  base_price: "",
});

const loadServices = async () => {
  try {
    error.value = null;
    const result = await fetchAllServices();
    services.value = result;
  } catch (err) {
    error.value = "Ошибка загрузки услуг";
  }
};

const handleCreate = async () => {
  try {
    const result = await createService({
      ...newService,
      base_price: parseFloat(newService.base_price),
    });

    services.value.push(result);
    newService.service_type = "";
    newService.base_price = "";
  } catch (err) {
    error.value = err.message || "Ошибка создания услуги";
  }
};

const handleUpdate = async () => {
  if (!editService.value) return;

  try {
    const result = await updateService(editService.value.id, {
      ...editService.value,
      base_price: parseFloat(editService.value.base_price),
    });

    const index = services.value.findIndex((s) => s.id === result.id);
    if (index !== -1) services.value.splice(index, 1, result);
    editService.value = null;
  } catch (err) {
    error.value = err.message || "Ошибка обновления";
  }
};

const handleDelete = async (id) => {
  try {
    await deleteService(id);
    services.value = services.value.filter((s) => s.id !== id);
  } catch (err) {
    error.value = err.message || "Ошибка удаления";
  }
};

onMounted(() => loadServices());
</script>

<style lang="scss" scoped>
.service-management {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;

  &__title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 2rem;
    color: #1a1a1a;
    text-align: center;
  }

  &__create-form {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 2rem;
  }

  &__form-title {
    font-size: 1.25rem;
    margin-bottom: 1rem;
    color: #2d3748;
  }

  &__form-content {
    display: grid;
    gap: 1rem;
    grid-template-columns: 1fr 1fr auto;
  }

  &__input {
    padding: 0.75rem;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    font-size: 1rem;

    &:focus {
      outline: none;
      border-color: #4299e1;
      box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.1);
    }
  }

  &__submit-btn {
    padding: 0.75rem 1.5rem;
    background: #4299e1;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #3182ce;
    }
  }

  &__list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  &__item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  }

  &__info {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  &__type {
    font-weight: 600;
    font-size: 1.125rem;
  }

  &__price {
    color: #4a5568;
    font-size: 0.875rem;
  }

  &__actions {
    display: flex;
    gap: 0.5rem;
  }

  &__edit-btn {
    padding: 0.5rem 1rem;
    background: #ecc94b;
    color: #1a202c;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: opacity 0.2s;

    &:hover {
      opacity: 0.9;
    }
  }

  &__delete-btn {
    @extend .service-management__edit-btn;
    background: #f56565;
    color: white;
  }

  &__modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  &__modal-content {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    width: 100%;
    max-width: 400px;
  }

  &__modal-title {
    font-size: 1.25rem;
    margin-bottom: 1.5rem;
  }

  &__modal-input {
    @extend .service-management__input;
    width: 100%;
    margin-bottom: 1rem;
  }

  &__modal-actions {
    display: flex;
    gap: 0.5rem;
    margin-top: 1rem;
  }

  &__modal-save {
    @extend .service-management__submit-btn;
    background: #48bb78;

    &:hover {
      background: #38a169;
    }
  }

  &__modal-cancel {
    @extend .service-management__submit-btn;
    background: #a0aec0;

    &:hover {
      background: #718096;
    }
  }

  &__error {
    padding: 1rem;
    background: #fed7d7;
    color: #c53030;
    border-radius: 6px;
    margin-bottom: 1rem;
    text-align: center;
  }
}
</style>

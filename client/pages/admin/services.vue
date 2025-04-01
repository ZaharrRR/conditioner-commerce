<template>
  <NuxtLayout name="admin-layout" class="service-management">
    <h1 class="title">Управление услугами</h1>

    <GenericForm
      title="Добавить услугу"
      :form-config="createFormConfig"
      :form-data="newService"
      :submit-handler="handleCreate"
      submit-button-text="Добавить"
    />

    <div v-if="error" class="error-message">{{ error }}</div>

    <div class="section service-list">
      <h2>Список услуг</h2>
      <DataTable
        v-if="services.length > 0"
        :columns="tableColumns"
        :rows="services"
      >
        <template #base_price="{ row }">
          {{ formatPrice(row.base_price) }}
        </template>
        <template #actions="{ row }">
          <div class="action-buttons">
            <button class="edit-button" @click="openEditModal(row)">
              Изменить
            </button>
            <button class="delete-button" @click="handleDelete(row.id)">
              Удалить
            </button>
          </div>
        </template>
      </DataTable>
      <div v-else class="empty-state">Нет доступных услуг</div>
    </div>

    <div
      v-if="editService"
      class="edit-modal-overlay"
      @click.self="closeModal"
      @keyup.esc="closeModal"
    >
      <div class="edit-modal-content">
        <GenericForm
          title="Редактирование услуги"
          :form-config="editFormConfig"
          :form-data="editService"
          :submit-handler="handleUpdate"
          submit-button-text="Сохранить"
          cancel-button-text="Отмена"
          @submitted="handleEditSubmit"
          @cancel="closeModal"
          class="edit-modal-form"
        />
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

import DataTable from "@/components/admin/DataTable.vue";
import GenericForm from "@/components/admin/GenericForm.vue";

const services = ref([]);
const editService = ref(null);

const error = ref(null);

const newService = reactive({
  service_type: "",
  base_price: "",
  description: "",
});

const createFormConfig = [
  {
    title: "Добавить услугу",
    fields: [
      {
        type: "input",
        label: "Тип услуги",
        key: "service_type",
        required: true,
        placeholder: "Введите тип услуги",
      },
      {
        type: "number",
        label: "Базовая цена",
        key: "base_price",
        required: true,
        step: "0.01",
        placeholder: "Введите стоимость",
      },
      {
        type: "input",
        label: "Описание услуги",
        key: "description",
        required: true,
        placeholder: "Введите описание товара",
      },
    ],
  },
];

const editFormConfig = [
  {
    title: "Редактирование услуги",
    fields: [
      {
        type: "input",
        label: "Тип услуги",
        key: "service_type",
        required: true,
      },
      {
        type: "number",
        label: "Базовая цена",
        key: "base_price",
        required: true,
        step: "0.01",
      },
    ],
  },
];

const tableColumns = [
  { title: "Изображение", key: "logo_url", width: "100px", type: "image" },
  { title: "Тип услуги", key: "service_type" },
  { title: "Стоимость", key: "base_price" },
  { title: "Описание", key: "description" },
  { title: "Действия", key: "actions", width: "150px" },
];

const formatPrice = (price) => {
  return new Intl.NumberFormat("ru-RU", {
    style: "currency",
    currency: "RUB",
  }).format(price);
};

const handleCreate = async (formData) => {
  if (!formData.service_type.trim()) throw new Error("Тип услуги обязателен");

  const response = await createService({
    ...formData,
    base_price: parseFloat(formData.base_price),
  });

  Object.assign(newService, {
    service_type: "",
    base_price: "",
    description: "",
  });

  services.value.unshift(response);

  return response;
};

const openEditModal = (service) => {
  editService.value = { ...service };
};

const handleUpdate = async (formData) => {
  if (!formData.service_type.trim()) throw new Error("Тип услуги обязателен");
  return await updateService(formData.id, {
    ...formData,
    base_price: parseFloat(formData.base_price),
  });
};

const handleEditSubmit = () => {
  editService.value = null;
  loadServices();
};

const handleDelete = async (id) => {
  try {
    await deleteService(id);
    await loadServices();
  } catch (err) {
    error.value = "Ошибка при удалении услуги";
  }
};

const loadServices = async () => {
  try {
    error.value = null;
    services.value = await fetchAllServices();
  } catch (err) {
    error.value = "Ошибка загрузки услуг";
  }
};

const closeModal = () => {
  editService.value = null;
};

onMounted(() => {
  loadServices();
});
</script>

<style lang="scss" scoped>
.service-management {
  .title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    color: #1a1a1a;
  }

  .error-message {
    padding: 1rem;
    background: #fed7d7;
    color: #c53030;
    border-radius: 6px;
    margin-bottom: 1rem;
  }

  .section {
    margin-top: 2rem;

    h2 {
      font-size: 1.25rem;
      margin-bottom: 1rem;
      color: #2d3748;
    }
  }

  .action-buttons {
    display: flex;
    gap: 0.5rem;

    .edit-button {
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

    .delete-button {
      @extend .edit-button;
      background: #f56565;
      color: white;
    }
  }

  .empty-state {
    padding: 1.5rem;
    background: #f8f9fa;
    border-radius: 8px;
    text-align: center;
    color: #6c757d;
  }

  .edit-modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    backdrop-filter: blur(2px);
    cursor: pointer;

    .edit-modal-content {
      background: white;
      padding: 2rem;
      border-radius: 8px;
      width: 100%;
      max-width: 600px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      cursor: default;
      position: relative;
    }
  }

  .edit-modal-form {
    :deep(.form-section) {
      padding: 0;
      margin: 0;
    }

    :deep(.form-title) {
      font-size: 1.5rem;
      margin-bottom: 1.5rem;
    }

    :deep(input) {
      width: 100%;
      padding: 0.75rem;
      margin-bottom: 1rem;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
    }

    :deep(.form-actions) {
      margin-top: 1.5rem;
      display: flex;
      gap: 0.5rem;
      justify-content: flex-end;
    }
  }
}
</style>

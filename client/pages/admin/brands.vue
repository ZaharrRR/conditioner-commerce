<template>
  <NuxtLayout name="admin-layout" class="brand-management">
    <h1 class="title">Управление брендами</h1>

    <div class="create-form">
      <h2 class="form-title">Добавить бренд</h2>
      <div class="form-content">
        <input
          v-model="newBrand.name"
          placeholder="Название"
          class="form-input"
        />
        <textarea
          v-model="newBrand.description"
          placeholder="Описание"
          class="form-textarea"
        ></textarea>
        <input
          v-model="newBrand.logo"
          placeholder="Ссылка на лого"
          class="form-input"
        />
        <button @click="handleCreate" class="submit-button">Добавить</button>
      </div>
    </div>

    <div v-if="error" class="error-message">{{ error }}</div>
    <div v-else class="brand-list">
      <div v-for="brand in brands" :key="brand.id" class="brand-item">
        <div class="brand-info">
          <img v-if="brand.logo" :src="brand.logo" class="brand-logo" />
          <div class="brand-details">
            <h3 class="brand-name">{{ brand.name }}</h3>
            <p class="brand-description">{{ brand.description }}</p>
          </div>
        </div>

        <div class="action-buttons">
          <button @click="editBrand = { ...brand }" class="edit-button">
            Изменить
          </button>
          <button @click="handleDelete(brand.id)" class="delete-button">
            Удалить
          </button>
        </div>
      </div>
    </div>

    <div v-if="editBrand" class="edit-modal">
      <div class="modal-content">
        <h2 class="modal-title">Редактирование бренда</h2>
        <input v-model="editBrand.name" class="modal-input" />
        <textarea
          v-model="editBrand.description"
          class="modal-textarea"
        ></textarea>
        <input v-model="editBrand.logo" class="modal-input" />
        <div class="modal-actions">
          <button @click="handleUpdate" class="save-button">Сохранить</button>
          <button @click="editBrand = null" class="cancel-button">
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
  fetchAllBrands,
  createBrand,
  updateBrand,
  deleteBrand,
} from "@/api/brands";

const brands = ref([]);
const editBrand = ref(null);

const error = ref(null);

const newBrand = reactive({
  name: "",
  description: "",
  logo: "",
});

const loadBrands = async () => {
  try {
    error.value = null;
    const result = await fetchAllBrands();

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    brands.value = result;
  } finally {
  }
};

const handleCreate = async () => {
  try {
    error.value = null;
    const result = await createBrand(newBrand);

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    brands.value.push(result);
    newBrand.name = "";
    newBrand.description = "";
    newBrand.logo = "";
  } catch (err) {
    error.value = "Неизвестная ошибка при создании бренда";
  }
};

const handleUpdate = async () => {
  if (!editBrand.value) return;

  try {
    error.value = null;
    const result = await updateBrand(editBrand.value.id, editBrand.value);

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    const index = brands.value.findIndex((b) => b.id === result.id);
    if (index !== -1) brands.value.splice(index, 1, result);
    editBrand.value = null;
  } catch (err) {
    error.value = "Неизвестная ошибка при обновлении";
  }
};

const handleDelete = async (id) => {
  try {
    error.value = null;
    const result = await deleteBrand(id);

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    brands.value = brands.value.filter((b) => b.id !== id);
  } catch (err) {
    error.value = "Неизвестная ошибка при удалении";
  }
};

onMounted(() => {
  loadBrands();
});
</script>

<style lang="scss" scoped>
.brand-management {
  .title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    color: #1a1a1a;
  }

  .create-form {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 2rem;

    .form-title {
      font-size: 1.25rem;
      margin-bottom: 1rem;
      color: #2d3748;
    }

    .form-content {
      display: flex;
      flex-direction: column;
      gap: 1rem;

      .form-input {
        padding: 0.75rem;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        font-size: 1rem;
        transition: border-color 0.2s;

        &:focus {
          outline: none;
          border-color: #4299e1;
          box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.1);
        }
      }

      .form-textarea {
        @extend .form-input;
        height: 6rem;
        resize: vertical;
      }

      .submit-button {
        align-self: flex-start;
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
    }
  }

  .brand-list {
    .brand-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem;
      margin-bottom: 1rem;
      background: white;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);

      .brand-info {
        display: flex;
        align-items: center;
        gap: 1rem;

        .brand-logo {
          width: 4rem;
          height: 4rem;
          object-fit: contain;
        }

        .brand-name {
          font-size: 1.125rem;
          font-weight: 600;
          margin-bottom: 0.25rem;
        }

        .brand-description {
          color: #718096;
          font-size: 0.875rem;
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
    }
  }

  .edit-modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;

    .modal-content {
      background: white;
      padding: 1.5rem;
      border-radius: 8px;
      width: 32rem;

      .modal-title {
        font-size: 1.25rem;
        margin-bottom: 1rem;
      }

      .modal-input {
        @extend .form-input;
        width: 100%;
        margin-bottom: 1rem;
      }

      .modal-textarea {
        @extend .form-textarea;
        width: 100%;
        margin-bottom: 1rem;
      }

      .modal-actions {
        display: flex;
        gap: 0.5rem;

        .save-button {
          @extend .submit-button;
          background: #48bb78;
          &:hover {
            background: #38a169;
          }
        }

        .cancel-button {
          @extend .submit-button;
          background: #a0aec0;
          &:hover {
            background: #718096;
          }
        }
      }
    }
  }

  .error-message {
    padding: 1rem;
    background: #fed7d7;
    color: #c53030;
    border-radius: 6px;
    margin-bottom: 1rem;
  }
}
</style>

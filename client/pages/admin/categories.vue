<script setup lang="ts">
import { ref, reactive, onMounted } from "vue";

import type { ICategory } from "@/types/category";

import {
  fetchAllCategories,
  createCategory,
  updateCategory,
  deleteCategory,
} from "@/api/categories";

const categories = ref<ICategory[]>([]);
const loading = ref(false);
const error = ref<string | null>(null);
const editCategory = ref<ICategory | null>(null);

const newCategory = reactive({
  name: "",
  logo_url: "",
});

const loadCategories = async () => {
  try {
    loading.value = true;
    error.value = null;
    const result = await fetchAllCategories();

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    categories.value = result;
  } finally {
    loading.value = false;
  }
};

const handleCreate = async () => {
  try {
    error.value = null;
    const result = await createCategory(newCategory);

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    categories.value.push(result);
    newCategory.name = "";
    newCategory.logo_url = "";
  } catch (err) {
    error.value = "Неизвестная ошибка при создании категории";
  }
};

const handleUpdate = async () => {
  if (!editCategory.value) return;

  try {
    error.value = null;
    const result = await updateCategory(
      editCategory.value.id,
      editCategory.value
    );

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    const index = categories.value.findIndex((c) => c.id === result.id);
    if (index !== -1) categories.value.splice(index, 1, result);
    editCategory.value = null;
  } catch (err) {
    error.value = "Неизвестная ошибка при обновлении";
  }
};

const handleDelete = async (id: string) => {
  try {
    error.value = null;
    const result = await deleteCategory(id);

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    categories.value = categories.value.filter((c) => c.id !== id);
  } catch (err) {
    error.value = "Неизвестная ошибка при удалении";
  }
};

onMounted(() => {
  loadCategories();
});
</script>

<template>
  <NuxtLayout name="admin-layout" class="category-management">
    <h1 class="title">Управление категориями</h1>

    <!-- Форма создания -->
    <div class="create-form">
      <h2 class="form-title">Добавить категорию</h2>
      <div class="form-content">
        <input
          v-model="newCategory.name"
          placeholder="Название"
          class="form-input"
        />
        <input
          v-model="newCategory.logo_url"
          placeholder="Ссылка на лого"
          class="form-input"
        />
        <button @click="handleCreate" class="submit-button">Добавить</button>
      </div>
    </div>

    <!-- Список категорий -->
    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else-if="error" class="error-message">{{ error }}</div>
    <div v-else class="category-list">
      <div
        v-for="category in categories"
        :key="category.id"
        class="category-item"
      >
        <div class="category-info">
          <img
            v-if="category.logo_url"
            :src="category.logo_url"
            class="category-logo"
          />
          <span class="category-name">{{ category.name }}</span>
        </div>

        <div class="action-buttons">
          <button @click="editCategory = { ...category }" class="edit-button">
            Изменить
          </button>
          <button @click="handleDelete(category.id)" class="delete-button">
            Удалить
          </button>
        </div>
      </div>
    </div>

    <!-- Модалка редактирования -->
    <div v-if="editCategory" class="edit-modal">
      <div class="modal-content">
        <h2 class="modal-title">Редактирование категории</h2>
        <input v-model="editCategory.name" class="modal-input" />
        <input v-model="editCategory.logo_url" class="modal-input" />
        <div class="modal-actions">
          <button @click="handleUpdate" class="save-button">Сохранить</button>
          <button @click="editCategory = null" class="cancel-button">
            Отмена
          </button>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<style lang="scss" scoped>
.category-management {
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
      gap: 1rem;
      align-items: center;

      .form-input {
        flex: 1;
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

      .submit-button {
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

  .category-list {
    .category-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem;
      margin-bottom: 1rem;
      background: white;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);

      .category-info {
        display: flex;
        align-items: center;
        gap: 1rem;

        .category-logo {
          width: 4rem;
          height: 4rem;
          object-fit: contain;
        }

        .category-name {
          font-size: 1.125rem;
          font-weight: 600;
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

  .loading {
    text-align: center;
    padding: 2rem;
    color: #718096;
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

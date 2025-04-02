<template>
  <NuxtLayout name="admin-layout" class="category-management">
    <h1 class="title">Управление категориями</h1>

    <GenericForm
      title="Добавить категорию"
      :form-config="createFormConfig"
      :form-data="newCategory"
      :submit-handler="handleCreate"
      submit-button-text="Добавить"
    />

    <div v-if="error" class="error-message">{{ error }}</div>

    <div class="section category-list">
      <h2>Список категорий</h2>
      <DataTable
        v-if="categories.length > 0"
        :columns="tableColumns"
        :rows="categories"
      >
        <template #logo_url="{ row }">
          <img v-if="row.logo_url" :src="row.logo_url" class="category-logo" />
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
      <div v-else class="empty-state">Нет доступных категорий</div>
    </div>

    <div
      v-if="editCategory"
      class="edit-modal-overlay"
      @click.self="closeModal"
      @keyup.esc="closeModal"
    >
      <div class="edit-modal-content">
        <GenericForm
          title="Редактирование категории"
          :form-config="editFormConfig"
          :form-data="editCategory"
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
import { ref, reactive, onMounted, onBeforeUnmount } from "vue";
import {
  fetchAllCategories,
  createCategory,
  updateCategory,
  deleteCategory,
} from "@/api/categories";
import DataTable from "@/components/admin/DataTable.vue";
import GenericForm from "@/components/admin/GenericForm.vue";

const categories = ref([]);
const editCategory = ref(null);
const error = ref(null);

const newCategory = reactive({
  name: "",
});

const createFormConfig = [
  {
    title: "Добавление категории",
    fields: [
      {
        type: "input",
        label: "Название категории",
        key: "name",
        required: true,
        placeholder: "Введите название",
      },
    ],
  },
];

const editFormConfig = [
  {
    title: "Редактирование категории",
    fields: [
      {
        type: "input",
        label: "Название категории",
        key: "name",
        required: true,
      },
    ],
  },
];

const tableColumns = [
  { title: "Лого", key: "logo_url", width: "100px", type: "image" },
  { title: "Название", key: "name" },
  { title: "Действия", key: "actions", width: "150px" },
];

const handleCreate = async (formData) => {
  if (!formData.name.trim()) throw new Error("Название обязательно");

  const response = await createCategory(formData);
  newCategory.name = "";
  categories.value.unshift(response);

  return response;
};

const openEditModal = (category) => {
  editCategory.value = { ...category };
};

const handleUpdate = async (formData) => {
  if (!formData.name.trim()) throw new Error("Название обязательно");
  return await updateCategory(formData.id, formData);
};

const handleEditSubmit = () => {
  editCategory.value = null;
  loadCategories();
};

const handleDelete = async (id) => {
  try {
    await deleteCategory(id);
    await loadCategories();
  } catch (err) {
    error.value = "Ошибка при удалении категории";
  }
};

const loadCategories = async () => {
  try {
    error.value = null;
    categories.value = await fetchAllCategories();
  } catch (err) {
    error.value = "Ошибка загрузки категорий";
  }
};

const closeModal = () => {
  editCategory.value = null;
};

onMounted(() => {
  loadCategories();
});
</script>

<style lang="scss" scoped>
.category-management {
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

  .category-logo {
    width: 60px;
    height: 60px;
    object-fit: contain;
    border-radius: 4px;
  }

  .action-buttons {
    display: flex;
    gap: 0.5rem;
    justify-content: center;

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

<template>
  <NuxtLayout name="admin-layout" class="admin-attributes">
    <h1 class="header">Управление атрибутами</h1>

    <GenericForm
      :form-config="formConfig"
      :form-data="form"
      :submit-handler="handleCreate"
      submit-button-text="Добавить"
    />

    <div v-if="error" class="error">{{ error }}</div>

    <div class="section attributes-list">
      <h2>Список продуктов</h2>
      <DataTable
        v-if="attributes.length > 0"
        :columns="tableColumns"
        :rows="attributes"
      >
        <template #actions="{ row }">
          <div class="action-buttons">
            <button class="delete-btn" @click="handleDelete(row.id)">
              Удалить
            </button>
          </div>
        </template>
      </DataTable>
      <div v-else class="empty-state">Нет доступных атрибутов</div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";

import {
  fetchAllAttributes,
  createAttribute,
  deleteAttribute,
} from "@/api/attributes";

import DataTable from "@/components/admin/DataTable.vue";
import GenericForm from "@/components/admin/GenericForm.vue";

const attributes = ref([]);
const error = ref(null);

const form = reactive({
  name: "",
});

const formConfig = [
  {
    title: "Добавить атрибут",
    fields: [
      {
        type: "input",
        label: "Название атрибута",
        key: "name",
        required: true,
        placeholder: "Введите название атрибута",
      },
    ],
  },
];

const tableColumns = [
  { title: "Название", key: "name" },
  { title: "Действия", key: "actions" },
];

const handleCreate = async (formData) => {
  const name = formData.name.trim();
  if (!name) throw new Error("Название атрибута обязательно");

  const result = await createAttribute(name);
  form.name = "";
  attributes.value.unshift(result);
};

const handleDelete = async (id) => {
  try {
    error.value = null;
    await deleteAttribute(id);
  } catch (err) {
    error.value = "Неизвестная ошибка при удалении";
  }
};

const loadAttributes = async () => {
  try {
    error.value = null;
    const result = await fetchAllAttributes();
    attributes.value = result;
  } catch (err) {
    error.value = "Ошибка загрузки атрибутов";
  }
};

onMounted(() => {
  loadAttributes();
});
</script>

<style lang="scss" scoped>
.section {
  margin-top: 2rem;

  h2 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
    color: #2d3748;
  }
}

.admin-attributes {
  .header {
    font-size: 2rem;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 1.5rem;
  }

  .create-form {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 2rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }

  .error {
    padding: 1rem;
    background: #fee2e2;
    color: #dc2626;
    border-radius: 6px;
    border: 1px solid #fca5a5;
    margin-bottom: 1rem;
  }

  .section {
    margin-top: 2rem;

    h2 {
      font-size: 1.25rem;
      margin-bottom: 1rem;
      color: #2c3e50;
    }
  }

  .empty-state {
    padding: 1.5rem;
    background: #f8f9fa;
    border-radius: 8px;
    text-align: center;
    color: #6c757d;
  }

  .action-buttons {
    display: flex;
    gap: 0.5rem;
    justify-content: center;

    .delete-btn {
      padding: 0.5rem 1rem;
      background: #dc2626;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: opacity 0.2s;
      font-weight: 500;

      &:hover {
        opacity: 0.9;
      }
    }
  }
}
</style>

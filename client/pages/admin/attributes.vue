<template>
  <NuxtLayout name="admin-layout" class="admin-attributes">
    <h1 class="header">Управление атрибутами</h1>

    <div class="create-form">
      <h2 class="form-title">Добавить атрибут</h2>
      <div class="form-content">
        <input
          v-model="newAttribute"
          placeholder="Название атрибута"
          class="form-input"
          @keyup.enter="handleCreate"
        />
        <button class="form-button" @click="handleCreate">Добавить</button>
      </div>
    </div>

    <div v-if="error" class="error">{{ error }}</div>
    <div v-else class="attributes-list">
      <div
        v-for="attribute in attributes"
        :key="attribute.id"
        class="attribute-item"
      >
        <span class="attribute-name">{{ attribute.name }}</span>
        <button class="delete-button" @click="handleDelete(attribute.id)">
          Удалить
        </button>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, onMounted } from "vue";

import {
  fetchAllAttributes,
  createAttribute,
  deleteAttribute,
} from "@/api/attributes";

const attributes = ref([]);
const newAttribute = ref("");

const error = ref(null);

const loadAttributes = async () => {
  try {
    error.value = null;
    const result = await fetchAllAttributes();

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    attributes.value = result;
  } finally {
  }
};

const handleCreate = async () => {
  const name = newAttribute.value.trim();
  if (!name) return;

  try {
    error.value = null;
    const result = await createAttribute(name);

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    attributes.value.push(result);
    newAttribute.value = "";
  } catch (err) {
    error.value = "Неизвестная ошибка при создании";
  }
};

const handleDelete = async (id) => {
  try {
    error.value = null;
    const result = await deleteAttribute(id);

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    attributes.value = attributes.value.filter((a) => a.id !== id);
  } catch (err) {
    error.value = "Неизвестная ошибка при удалении";
  }
};

onMounted(() => {
  loadAttributes();
});
</script>

<style lang="scss" scoped>
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

    .form-title {
      font-size: 1.25rem;
      margin-bottom: 1rem;
      color: #2c3e50;
    }

    .form-content {
      display: flex;
      gap: 1rem;
      align-items: center;

      .form-input {
        flex: 1;
        padding: 0.75rem;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        font-size: 1rem;
        transition: all 0.3s ease;

        &:focus {
          outline: none;
          border-color: #3498db;
          box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
        }
      }

      .form-button {
        padding: 0.75rem 1.5rem;
        background: #3498db;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background 0.2s;
        font-weight: 500;

        &:hover {
          background: #2980b9;
        }
      }
    }
  }

  .error {
    padding: 1rem;
    background: #fee2e2;
    color: #dc2626;
    border-radius: 6px;
    border: 1px solid #fca5a5;
    margin-bottom: 1rem;
  }

  .attributes-list {
    .attribute-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem;
      background: white;
      border: 1px solid #e0e0e0;
      border-radius: 6px;
      margin-bottom: 0.5rem;
      transition: box-shadow 0.2s;

      &:hover {
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
      }

      .attribute-name {
        font-size: 1.1rem;
        color: #2c3e50;
      }

      .delete-button {
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
}
</style>

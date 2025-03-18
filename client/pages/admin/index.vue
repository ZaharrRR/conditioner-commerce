<script setup lang="ts">
import { ref, reactive, onMounted, computed } from "vue";
import { createProduct, fetchAllProducts } from "@/api/products";
import { fetchAllBrands } from "~/api/brands";
import { fetchAllCategories } from "~/api/categories";
import type { IBrand } from "@/types/brand";
import type { ICategory } from "@/types/category";
import type { IProduct } from "@/types/product";

const brands = ref<IBrand[]>([]);
const categories = ref<ICategory[]>([]);
const products = ref<IProduct[]>([]);
const loading = ref(false);
const error = ref<string | null>(null);

const form = reactive({
  name: "",
  price: "",
  brand_id: "",
  category_id: "",
});

// Загрузка данных
const loadData = async () => {
  try {
    loading.value = true;
    error.value = null;

    const [brandsRes, categoriesRes, productsRes] = await Promise.all([
      fetchAllBrands(),
      fetchAllCategories(),
      fetchAllProducts(),
    ]);

    if (
      brandsRes instanceof Error ||
      categoriesRes instanceof Error ||
      productsRes instanceof Error
    ) {
      error.value = "Ошибка загрузки данных";
      return;
    }

    brands.value = brandsRes;
    categories.value = categoriesRes;
    products.value = productsRes;
  } catch (err) {
    error.value = "Неизвестная ошибка";
  } finally {
    loading.value = false;
  }
};

// Создание продукта
const submit = async () => {
  try {
    error.value = null;

    const numericPrice = parseFloat(form.price);
    if (isNaN(numericPrice)) {
      throw new Error("Некорректная цена");
    }

    const result = await createProduct({
      ...form,
      price: numericPrice,
    });

    if (result instanceof Error) {
      error.value = result.message;
      return;
    }

    // Обновляем список товаров
    products.value.push(result);

    // Сброс формы
    Object.assign(form, {
      name: "",
      price: "",
      brand_id: "",
      category_id: "",
    });

    alert("Товар успешно создан!");
  } catch (err) {
    error.value = "Ошибка создания товара";
  }
};

onMounted(() => loadData());
</script>

<template>
  <NuxtLayout name="admin-layout" class="product-create">
    <h1>Создание нового товара</h1>

    <div v-if="loading">Загрузка данных...</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <form v-else @submit.prevent="submit">
      <div class="form-group">
        <label>Название товара:</label>
        <input v-model="form.name" required />
      </div>

      <div class="form-group">
        <label>Цена:</label>
        <input v-model="form.price" type="number" step="0.01" required />
      </div>

      <div class="form-group">
        <label>Бренд:</label>
        <select v-model="form.brand_id" required>
          <option value="">Выберите бренд</option>
          <option v-for="brand in brands" :key="brand.id" :value="brand.id">
            {{ brand.name }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Категория:</label>
        <select v-model="form.category_id" required>
          <option value="">Выберите категорию</option>
          <option
            v-for="category in categories"
            :key="category.id"
            :value="category.id"
          >
            {{ category.name }}
          </option>
        </select>
      </div>

      <button type="submit">Создать товар</button>
    </form>

    <div class="section product-list">
      <h2>Список товаров</h2>

      <div v-if="loading">Загрузка товаров...</div>
      <div v-else-if="error" class="error">{{ error }}</div>

      <div v-else class="table-container">
        <table class="product-table">
          <thead>
            <tr>
              <th>Название</th>
              <th>Цена</th>
              <th>Бренд</th>
              <th>Категория</th>
              <th>Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="product in products" :key="product.id">
              <td>{{ product.name }}</td>
              <td>{{ product.price }} ₽</td>
              <td>{{ product.brand_name }}</td>
              <td>{{ product.category_name }}</td>
              <td class="actions">
                <button class="edit-btn">Изменить</button>
                <button class="delete-btn">Удалить</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </NuxtLayout>
</template>

<style scoped>
/* Стили остаются без изменений */
.product-create {
}

h1 {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

input,
select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-size: 1rem;
}

select {
  background: white;
  appearance: none;
}

button {
  background: #3b82f6;
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  width: 100%;
  font-size: 1rem;
  transition: background 0.2s;
}

button:hover {
  background: #2563eb;
}

.error {
  color: #dc2626;
  padding: 1rem;
  background: #fee2e2;
  border-radius: 0.375rem;
  margin-bottom: 1rem;
}

.section {
  margin-bottom: 3rem;
  padding: 1.5rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.product-list h2 {
  font-size: 1.25rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.table-container {
  overflow-x: auto;
}

.product-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

.product-table th,
.product-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.product-table th {
  background-color: #f8f9fa;
  font-weight: 600;
}

.actions {
  display: flex;
  gap: 0.5rem;
}

.edit-btn {
  padding: 0.5rem 1rem;
  background: #ecc94b;
  color: #1a202c;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s;
}

.delete-btn {
  padding: 0.5rem 1rem;
  background: #f56565;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s;
}

.edit-btn:hover,
.delete-btn:hover {
  opacity: 0.9;
}
</style>

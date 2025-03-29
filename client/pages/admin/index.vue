<template>
  <NuxtLayout name="admin-layout" class="product-create">
    <h1 class="product-create__title">Создание нового товара</h1>

    <div v-if="error" class="product-create__error">{{ error }}</div>

    <form v-else class="product-create__form" @submit.prevent="submit">
      <div class="product-create__form-group">
        <label class="product-create__label">Название товара:</label>
        <input v-model="form.name" class="product-create__input" required />
      </div>

      <div class="product-create__form-group">
        <label class="product-create__label">Цена:</label>
        <input
          v-model="form.price"
          type="number"
          step="0.01"
          class="product-create__input"
          required
        />
      </div>

      <div class="product-create__form-group">
        <label class="product-create__label">Бренд:</label>
        <select v-model="form.brand_id" class="product-create__select" required>
          <option value="">Выберите бренд</option>
          <option v-for="brand in brands" :key="brand.id" :value="brand.id">
            {{ brand.name }}
          </option>
        </select>
      </div>

      <div class="product-create__form-group">
        <label class="product-create__label">Категория:</label>
        <select
          v-model="form.category_id"
          class="product-create__select"
          required
        >
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

      <div class="product-create__attributes">
        <h3 class="product-create__subtitle">Атрибуты товара</h3>
        <div
          v-for="(attribute, index) in form.attributes"
          :key="index"
          class="product-create__attribute-group"
        >
          <select
            v-model="attribute.attribute_id"
            class="product-create__select"
            required
          >
            <option value="">Выберите атрибут</option>
            <option v-for="attr in attributes" :key="attr.id" :value="attr.id">
              {{ attr.name }}
            </option>
          </select>
          <input
            v-model="attribute.value"
            class="product-create__input"
            placeholder="Значение"
            required
          />
        </div>
        <button
          type="button"
          class="product-create__add-btn"
          @click="addAttributeField"
        >
          Добавить атрибут
        </button>
      </div>

      <button type="submit" class="product-create__submit-btn">
        Создать товар
      </button>
    </form>

    <div class="section product-list">
      <h2>Список товаров</h2>

      <div v-if="error" class="error">{{ error }}</div>

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
                <NuxtLink
                  :to="`/admin/products/edit/${product.id}`"
                  class="edit-btn"
                >
                  Изменить
                </NuxtLink>

                <button class="delete-btn">Удалить</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import { createProduct, fetchAllProducts } from "@/api/products";
import { fetchAllBrands } from "@/api/brands";
import { fetchAllCategories } from "@/api/categories";
import { fetchAllAttributes } from "@/api/attributes";

const brands = ref([]);
const categories = ref([]);
const attributes = ref([]);
const products = ref([]);
const error = ref(null);

const form = reactive({
  name: "",
  price: "",
  brand_id: "",
  category_id: "",
  attributes: [{ attribute_id: "", value: "" }],
});

const addAttributeField = () => {
  form.attributes.push({ attribute_id: "", value: "" });
};

// В loadData добавить загрузку атрибутов
const loadData = async () => {
  try {
    error.value = null;
    const [brandsRes, categoriesRes, productsRes, attributesRes] =
      await Promise.all([
        fetchAllBrands(),
        fetchAllCategories(),
        fetchAllProducts(),
        fetchAllAttributes(),
      ]);

    brands.value = brandsRes;
    categories.value = categoriesRes;
    products.value = productsRes;
    attributes.value = attributesRes;
  } catch (err) {
    error.value = "Ошибка загрузки данных";
  }
};

// В submit добавить отправку атрибутов
const submit = async () => {
  try {
    const numericPrice = parseFloat(form.price);
    if (isNaN(numericPrice)) throw new Error("Некорректная цена");

    const productData = {
      ...form,
      price: numericPrice,
      attributes: form.attributes.filter(
        (attr) => attr.attribute_id && attr.value
      ),
    };

    const result = await createProduct(productData);
    products.value.push(result);
    Object.assign(form, {
      name: "",
      price: "",
      brand_id: "",
      category_id: "",
      attributes: [{ attribute_id: "", value: "" }],
    });
    alert("Товар успешно создан!");
  } catch (err) {
    error.value = err.message || "Ошибка создания товара";
  }
};

onMounted(loadData);
</script>

<style lang="scss" scoped>
.product-create {
  &__title {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    text-align: center;
  }

  &__error {
    color: #dc2626;
    padding: 1rem;
    background: #fee2e2;
    border-radius: 0.375rem;
    margin-bottom: 1rem;
  }

  &__form {
    max-width: 600px;
    margin: 0 auto;
  }

  &__form-group {
    margin-bottom: 1.5rem;
  }

  &__label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
  }

  &__input {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
    font-size: 1rem;

    &:focus {
      border-color: #3b82f6;
      outline: none;
    }
  }

  &__select {
    @extend .product-create__input;
    appearance: none;
    background: white
      url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e")
      no-repeat right 0.75rem center;
    background-size: 1em;
  }

  &__attributes {
    margin: 2rem 0;
    padding: 1.5rem;
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
  }

  &__subtitle {
    font-size: 1.1rem;
    margin-bottom: 1rem;
    color: #4a5568;
  }

  &__attribute-group {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;

    select {
      flex: 1;
    }

    input {
      flex: 2;
    }
  }

  &__add-btn {
    background: #e2e8f0;
    color: #4a5568;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.375rem;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #cbd5e0;
    }
  }

  &__submit-btn {
    background: #3b82f6;
    color: white;
    padding: 0.75rem 1.5rem;
    width: 100%;
    border: none;
    border-radius: 0.375rem;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #2563eb;
    }
  }
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

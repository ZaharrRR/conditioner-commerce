<template>
  <NuxtLayout name="admin-layout" class="product-management">
    <h1 class="title">Создание нового товара</h1>

    <div v-if="error" class="error-message">{{ error }}</div>

    <template v-if="brands.length > 0 && categories.length > 0">
      <GenericForm
        :form-config="formConfig"
        :form-data="form"
        :external-data="{
          brands: brands,
          categories: categories,
        }"
        :submit-handler="submitProduct"
        submit-button-text="Создать товар"
      />
    </template>

    <div class="product-list">
      <div v-if="error" class="error">{{ error }}</div>

      <DataTable v-else :columns="tableColumns" :rows="products">
        <template #actions="{ row }">
          <div class="action-buttons">
            <NuxtLink :to="`/admin/products/edit/${row.id}`" class="edit-btn">
              Изменить
            </NuxtLink>

            <button class="delete-btn">Удалить</button>
          </div>
        </template>
      </DataTable>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";

import { createProduct, fetchAllProducts } from "@/api/products";
import { fetchAllBrands } from "@/api/brands";
import { fetchAllCategories } from "@/api/categories";

import DataTable from "@/components/admin/DataTable.vue";
import GenericForm from "@/components/admin/GenericForm.vue";

const brands = ref([]);
const categories = ref([]);
const products = ref([]);

const error = ref(null);

const form = reactive({
  name: "",
  price: "",
  brand_id: "",
  category_id: "",
});

const formConfig = [
  {
    title: "Добавить товар",
    fields: [
      {
        type: "input",
        label: "Название товара",
        key: "name",
        required: true,
      },
      {
        type: "number",
        label: "Цена",
        key: "price",
        required: true,
        step: "0.01",
      },
      {
        type: "select",
        label: "Бренд",
        key: "brand_id",
        required: true,
        options: "brands",
      },
      {
        type: "select",
        label: "Категория",
        key: "category_id",
        required: true,
        options: "categories",
      },
    ],
  },
];

const tableColumns = [
  { title: "Название", key: "name" },
  { title: "Цена", key: "price" },
  { title: "Бренд", key: "brand_name" },
  { title: "Категория", key: "category_name" },
  { title: "Действия", key: "actions" },
];

async function submitProduct(formData) {
  const numericPrice = parseFloat(formData.price);
  if (isNaN(numericPrice)) throw new Error("Некорректная цена");

  const productData = {
    ...formData,
    price: numericPrice,
  };

  await createProduct(productData);
  Object.assign(form, { name: "", price: "", brand_id: "", category_id: "" });
  alert("Товар успешно создан!");
}

const loadData = async () => {
  try {
    error.value = null;
    const [brandsRes, categoriesRes, productsRes] = await Promise.all([
      fetchAllBrands(),
      fetchAllCategories(),
      fetchAllProducts(),
    ]);

    brands.value = brandsRes;
    categories.value = categoriesRes;
    products.value = productsRes;
  } catch (err) {
    error.value = "Ошибка загрузки данных";
  }
};

onMounted(loadData);
</script>

<style lang="scss" scoped>
.product-management {
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

  .action-buttons {
    display: flex;
    gap: 0.5rem;
    justify-content: center;

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
  }
}
</style>

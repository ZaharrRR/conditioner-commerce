<template>
  <NuxtLayout name="page-layout">
    <div class="products-page">
      <Filters
        :categories="categories"
        :brands="brands"
        @filter="applyFilters"
      />

      <div class="products">
        <div class="sorting">
          <select v-model="sortBy">
            <option value="">Выберите сортировку</option>
            <option value="high-price">Сначала дорогие</option>
            <option value="low-price">Сначала недорогие</option>
          </select>
        </div>

        <div v-if="loading" class="loading">Загрузка товаров...</div>
        <div v-else-if="error" class="error">{{ error }}</div>
        <ProductGrid v-else :products="filteredProducts" />
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";

import Filters from "@/components/Filters.vue";
import ProductGrid from "@/components/ProductGrid.vue";

import { fetchAllProducts } from "@/api/products";
import { fetchAllBrands } from "@/api/brands";
import { fetchAllCategories } from "@/api/categories";

const products = ref([]);
const categories = ref([]);
const brands = ref([]);

const loading = ref(false);
const error = ref(null);

const selectedCategories = ref([]);
const selectedBrands = ref([]);
const priceRange = ref({ min: null, max: null });
const sortBy = ref("");

const loadData = async () => {
  try {
    loading.value = true;
    error.value = null;

    const [productsRes, brandsRes, categoriesRes] = await Promise.all([
      fetchAllProducts(),
      fetchAllBrands(),
      fetchAllCategories(),
    ]);

    if (
      productsRes instanceof Error ||
      brandsRes instanceof Error ||
      categoriesRes instanceof Error
    ) {
      throw new Error("Ошибка загрузки данных");
    }

    products.value = productsRes;
    brands.value = brandsRes;
    categories.value = categoriesRes;
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

const filteredProducts = computed(() => {
  let filtered = products.value;

  if (selectedCategories.value.length > 0) {
    filtered = filtered.filter((p) =>
      selectedCategories.value.some((cat) => cat.name === p.category_name)
    );
  }

  if (selectedBrands.value.length > 0) {
    filtered = filtered.filter((p) =>
      selectedBrands.value.some((brand) => brand.name === p.brand_name)
    );
  }
  if (priceRange.value.min || priceRange.value.max) {
    filtered = filtered.filter(
      (p) =>
        p.price >= (priceRange.value.min || 0) &&
        p.price <= (priceRange.value.max || Infinity)
    );
  }

  if (sortBy.value === "high-price") {
    return [...filtered].sort((a, b) => b.price - a.price);
  }
  if (sortBy.value === "low-price") {
    return [...filtered].sort((a, b) => a.price - b.price);
  }
  return filtered;
});

const applyFilters = (filters) => {
  selectedCategories.value = filters.categories;
  selectedBrands.value = filters.brands;
  priceRange.value = filters.priceRange;
};

onMounted(() => loadData());
</script>

<style scoped>
.products-page {
  display: flex;
  gap: 24px;
}

.products {
  flex-grow: 1;
}

.sorting {
  margin-bottom: 20px;
}

select {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
  background-color: #f9f9f9;
  font-size: 16px;
  cursor: pointer;
}

select:focus {
  outline: none;
  border-color: #007bff;
}

.loading {
  padding: 20px;
  text-align: center;
  color: #666;
}

.error {
  color: #dc2626;
  padding: 1rem;
  background: #fee2e2;
  border-radius: 0.375rem;
  margin-bottom: 1rem;
}
</style>

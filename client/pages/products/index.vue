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
  padding: 20px;
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
  width: 100%;
  max-width: 250px;
}

@media (max-width: 1280px) {
  .products-page {
    gap: 20px;
    padding: 15px;
  }

  select {
    max-width: 200px;
    font-size: 14px;
  }
}

@media (max-width: 720px) {
  .products-page {
    flex-direction: column;
  }

  .filters {
    width: 100%;
    order: -1;
  }

  .product-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  select {
    max-width: 100%;
  }
}

@media (max-width: 480px) {
  .product-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .products-page {
    padding: 10px;
    gap: 15px;
  }

  .product-grid {
    grid-template-columns: 1fr;
  }

  .card__content {
    height: auto;
    padding: 12px;
  }
}
</style>

<template>
  <NuxtLayout name="page-layout">
    <Breadcrumbs
      :items="[
        { name: 'Главная', path: '/' },
        { name: 'Каталог', path: '/products' },
      ]"
    />

    <div class="products-page">
      <Filters
        :categories="categories"
        :brands="brands"
        @filter="applyFilters"
      />

      <div class="products">
        <div class="sorting">
          <select v-model="sortBy" aria-label="Сортировка товаров">
            <option value="">Выберите сортировку</option>
            <option value="high-price">Сначала дорогие</option>
            <option value="low-price">Сначала недорогие</option>
          </select>
        </div>

        <ProductGrid :products="filteredProducts" />
      </div>
    </div>

    <SeoText :text="seoText" />
  </NuxtLayout>
</template>

<script setup>
import { ref, computed } from "vue";
import { fetchAllBrands } from "~/api/brands";
import { fetchAllCategories } from "~/api/categories";
import { fetchAllProducts } from "~/api/products";
import Breadcrumbs from "~/components/common/Breadcrumbs.vue";
import SeoText from "~/components/common/SeoText.vue";

const { data: products } = await useAsyncData("products", fetchAllProducts);
const { data: brands } = await useAsyncData("brands", fetchAllBrands);
const { data: categories } = await useAsyncData(
  "categories",
  fetchAllCategories
);

const selectedCategories = ref([]);
const selectedBrands = ref([]);
const priceRange = ref({ min: null, max: null });
const sortBy = ref("");

const filteredProducts = computed(() => {
  let filtered = [...products.value];

  // Фильтрация по категориям
  if (selectedCategories.value.length > 0) {
    filtered = filtered.filter((p) =>
      selectedCategories.value.some((cat) => cat.name === p.category_name)
    );
  }

  // Фильтрация по брендам
  if (selectedBrands.value.length > 0) {
    filtered = filtered.filter((p) =>
      selectedBrands.value.some((brand) => brand.name === p.brand_name)
    );
  }

  // Фильтрация по цене
  if (priceRange.value.min || priceRange.value.max) {
    filtered = filtered.filter(
      (p) =>
        p.price >= (priceRange.value.min || 0) &&
        p.price <= (priceRange.value.max || Infinity)
    );
  }

  // Сортировка
  if (sortBy.value === "high-price")
    return filtered.sort((a, b) => b.price - a.price);
  if (sortBy.value === "low-price")
    return filtered.sort((a, b) => a.price - b.price);
  return filtered;
});

const applyFilters = (filters) => {
  selectedCategories.value = filters.categories;
  selectedBrands.value = filters.brands;
  priceRange.value = filters.priceRange;
};

// SEO оптимизация
const breadcrumbs = computed(() => [
  { name: "Главная", path: "/" },
  { name: "Каталог", path: "/products" },
]);

const seoText = computed(
  () => `
  Широкий выбор кондиционеров в Тюмени от ведущих брендов: ${brands.value
    .map((b) => b.name)
    .join(", ")}. 
  ${categories.value
    .map((c) => `Купить ${c.name} по выгодной цене с установкой.`)
    .join(" ")}
`
);

useSeoMeta({
  title: "Купить кондиционеры в Тюмени | Каталог сплит-систем с ценами",
  description:
    "Большой выбор кондиционеров и сплит-систем от ведущих производителей. Профессиональная установка, гарантия до 5 лет!",
  ogTitle: "Каталог кондиционеров с ценами в Тюмени",
  ogDescription:
    "Широкий ассортимент климатической техники с бесплатной доставкой и монтажом",
});

useHead({
  script: [
    {
      type: "application/ld+json",
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "ItemList",
        itemListElement: filteredProducts.value
          .slice(0, 50)
          .map((product, index) => ({
            "@type": "ListItem",
            position: index + 1,
            item: {
              "@type": "Product",
              name: product.name,
              url: `${useRuntimeConfig().public.siteUrl}/products/${
                product.id
              }`,
              image: product.photo_url || "/images/hisense.png",
              brand: {
                "@type": "Brand",
                name: product.brand_name,
              },
              offers: {
                "@type": "Offer",
                priceCurrency: "RUB",
                price: product.price,
                availability: "https://schema.org/InStock",
              },
            },
          })),
      }),
    },
  ],
});
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
  background-color: white;
  font-size: 16px;
  cursor: pointer;
  width: 100%;
  max-width: 250px;
}

/* Общие стили для всех инпутов */
select,
input[type="text"],
input[type="number"],
input[type="checkbox"] {
  transition: border-color 0.3s ease;
}

/* Стили при фокусе */
select:focus,
input[type="text"]:focus,
input[type="number"]:focus {
  outline: none;
  border-color: var(--blue);
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2); /* Необязательно: мягкая тень */
}

/* Для чекбоксов можно сделать кастомный стиль */
input[type="checkbox"]:focus {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}

/* Стиль при активном состоянии (если нужно) */
select:active,
input[type="text"]:active,
input[type="number"]:active {
  border-color: var(--blue);
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

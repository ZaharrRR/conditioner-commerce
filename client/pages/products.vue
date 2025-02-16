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
            <option value="low-price">Сначала дорогие</option>
            <option value="hight-price">Сначала недорогие</option>
          </select>
        </div>
        <ProductGrid :products="filteredProducts" />
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import { ref, computed } from "vue";
import Filters from "~/components/Filters.vue";
import ProductGrid from "~/components/ProductGrid.vue";

const categories = [
  "Настенные",
  "Мобильные",
  "Оконные",
  "Кассетные",
  "Канальные",
];
const brands = ["Daikin", "Mitsubishi", "LG", "Toshiba", "Hisense", "Gree"];

const products = ref([
  {
    id: 1,
    name: "Daikin FTXS35K / RXS35K",
    description: "Настенный кондиционер с инверторным управлением",
    price: 85000,
    brand: "Daikin",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 2,
    name: "Mitsubishi Electric MSZ-LN25VG / MUZ-LN25VG",
    description: "Энергоэффективный настенный кондиционер",
    price: 72000,
    brand: "Mitsubishi",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 3,
    name: "LG P09EP2",
    description: "Мобильный кондиционер с функцией осушения",
    price: 25000,
    brand: "LG",
    category: "Мобильные",
    image: "/images/hisense.png",
  },
  {
    id: 4,
    name: "Toshiba RAS-10EKV-EE / RAS-10EAV-EE",
    description: "Настенный кондиционер с Wi-Fi управлением",
    price: 68000,
    brand: "Toshiba",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 5,
    name: "Hisense AS-09HR4SYDTE",
    description: "Настенный кондиционер с низким уровнем шума",
    price: 35000,
    brand: "Hisense",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 6,
    name: "Gree GWH09QA-K3DNA2A",
    description: "Мобильный кондиционер с функцией обогрева",
    price: 28000,
    brand: "Gree",
    category: "Мобильные",
    image: "/images/hisense.png",
  },
  {
    id: 7,
    name: "Daikin ATXN35M / ARXN35M",
    description: "Кассетный кондиционер для больших помещений",
    price: 120000,
    brand: "Daikin",
    category: "Кассетные",
    image: "/images/hisense.png",
  },
  {
    id: 8,
    name: "Mitsubishi Heavy SRK20ZSPR-S",
    description: "Оконный кондиционер с простым управлением",
    price: 40000,
    brand: "Mitsubishi",
    category: "Оконные",
    image: "/images/hisense.png",
  },
  {
    id: 9,
    name: "LG S09EQ",
    description: "Мобильный кондиционер с ионизатором воздуха",
    price: 30000,
    brand: "LG",
    category: "Мобильные",
    image: "/images/hisense.png",
  },
  {
    id: 10,
    name: "Toshiba RAS-13EKV-EE / RAS-13EAV-EE",
    description: "Настенный кондиционер с функцией самоочистки",
    price: 75000,
    brand: "Toshiba",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 11,
    name: "Hisense AS-12HR4SYDTE",
    description: "Настенный кондиционер с Wi-Fi управлением",
    price: 38000,
    brand: "Hisense",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 12,
    name: "Gree GWH12QC-K3DNA2A",
    description: "Мобильный кондиционер с таймером",
    price: 32000,
    brand: "Gree",
    category: "Мобильные",
    image: "/images/hisense.png",
  },
  {
    id: 13,
    name: "Daikin FTXS25K / RXS25K",
    description: "Настенный кондиционер с низким энергопотреблением",
    price: 78000,
    brand: "Daikin",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 14,
    name: "Mitsubishi Electric MSZ-LN35VG / MUZ-LN35VG",
    description: "Настенный кондиционер с функцией обогрева",
    price: 82000,
    brand: "Mitsubishi",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 15,
    name: "LG P12EP2",
    description: "Мобильный кондиционер с пультом управления",
    price: 27000,
    brand: "LG",
    category: "Мобильные",
    image: "/images/hisense.png",
  },
  {
    id: 16,
    name: "Toshiba RAS-16EKV-EE / RAS-16EAV-EE",
    description: "Настенный кондиционер с функцией турбо-режима",
    price: 90000,
    brand: "Toshiba",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 17,
    name: "Hisense AS-18HR4SYDTE",
    description: "Настенный кондиционер для больших помещений",
    price: 42000,
    brand: "Hisense",
    category: "Настенные",
    image: "/images/hisense.png",
  },
  {
    id: 18,
    name: "Gree GWH18QC-K3DNA2A",
    description: "Мобильный кондиционер с функцией осушения",
    price: 35000,
    brand: "Gree",
    category: "Мобильные",
    image: "/images/hisense.png",
  },
  {
    id: 19,
    name: "Daikin ATXN50M / ARXN50M",
    description: "Кассетный кондиционер для коммерческих помещений",
    price: 150000,
    brand: "Daikin",
    category: "Кассетные",
    image: "/images/hisense.png",
  },
  {
    id: 20,
    name: "Mitsubishi Heavy SRK25ZSPR-S",
    description: "Оконный кондиционер с низким уровнем шума",
    price: 45000,
    brand: "Mitsubishi",
    category: "Оконные",
    image: "/images/hisense.png",
  },
]);

const selectedCategories = ref([]);
const selectedBrands = ref([]);
const priceRange = ref({ min: null, max: null });
const sortBy = ref("");

const filteredProducts = computed(() => {
  let filtered = products.value;

  if (selectedCategories.value.length > 0) {
    filtered = filtered.filter((product) =>
      selectedCategories.value.includes(product.category)
    );
  }

  if (selectedBrands.value.length > 0) {
    filtered = filtered.filter((product) =>
      selectedBrands.value.includes(product.brand)
    );
  }

  if (priceRange.value.min || priceRange.value.max) {
    filtered = filtered.filter(
      (product) =>
        product.price >= (priceRange.value.min ? priceRange.value.min : 0) &&
        product.price <= (priceRange.value.max ? priceRange.value.max : 9999999)
    );
  }

  if (sortBy.value) {
    if (sortBy.value === "low-price") {
      filtered.sort((a, b) => b.price - a.price);
    } else if (sortBy.value === "hight-price") {
      filtered.sort((a, b) => a.price - b.price);
    }
  }

  return filtered;
});

const applyFilters = (filters) => {
  selectedCategories.value = filters.categories;
  selectedBrands.value = filters.brands;
  priceRange.value = filters.priceRange;
};
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
</style>

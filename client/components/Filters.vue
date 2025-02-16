<template>
  <div class="filters">
    <h3>Категории</h3>
    <ul>
      <li v-for="category in categories" :key="category">
        <input
          type="checkbox"
          :id="category"
          :value="category"
          v-model="selectedCategories"
        />
        <label :for="category">{{ category }}</label>
      </li>
    </ul>

    <hr />

    <h3>Цена</h3>
    <div class="price-range">
      <input type="number" v-model="priceRange.min" placeholder="От 0 " />
      <input type="number" v-model="priceRange.max" placeholder="До 99999" />
    </div>

    <hr />

    <h3>Бренды</h3>
    <ul>
      <li v-for="brand in brands" :key="brand">
        <input
          type="checkbox"
          :id="brand"
          :value="brand"
          v-model="selectedBrands"
        />
        <label :for="brand">{{ brand }}</label>
      </li>
    </ul>

    <button @click="applyFilters">Применить фильтры</button>
    <button @click="resetFilters">Сбросить фильтры</button>
  </div>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  categories: Array,
  brands: Array,
});

const selectedCategories = ref([]);
const selectedBrands = ref([]);
const priceRange = ref({ min: null, max: null });

const emit = defineEmits(["filter"]);

const applyFilters = () => {
  emit("filter", {
    categories: selectedCategories.value,
    brands: selectedBrands.value,
    priceRange: priceRange.value,
  });
};

const resetFilters = () => {
  (selectedCategories.value = []),
    (selectedBrands.value = []),
    (priceRange.value = { min: null, max: null });

  applyFilters();
};
</script>

<style scoped>
.filters {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 300px;

  border: 2px solid var(--blue);
  padding: 20px;
  border-radius: 12px;
}

h3 {
  margin-bottom: 10px;
  font-size: 18px;
  color: var(--blue);
  font-weight: 700;
}

hr {
  height: 3px;
  background-color: var(--blue);
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 10px;
}

input[type="checkbox"] {
  margin-right: 10px;
}

.price-range {
  display: flex;
  gap: 10px;
}

input[type="number"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
}

button {
  padding: 10px;
  background-color: var(--blue);
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}
</style>

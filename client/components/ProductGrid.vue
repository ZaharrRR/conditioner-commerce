<template>
  <div class="product-grid">
    <CardProduct
      v-for="(product, index) in products"
      :key="index"
      :product="product"
    />
  </div>
</template>

<script setup>
import CardProduct from "./CardProduct.vue";

const props = defineProps({
  products: Array,
});
</script>

<style scoped>
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
  gap: 20px;
}
</style>

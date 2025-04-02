<template>
  <div class="product-grid" itemscope itemtype="http://schema.org/ItemList">
    <CardProduct
      v-for="(product, index) in products"
      :key="product.id"
      :product="product"
      :index="index"
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

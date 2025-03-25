<template>
  <RouterLink :to="`/products/${product.id}`" class="card">
    <img
      :src="product.image ? product.image : `/images/hisense.png`"
      :alt="product.name"
      class="card__image"
      loading="lazy"
    />

    <div class="card__content">
      <h3 class="card__content-title">{{ product.name }}</h3>
      <p class="card__content-description">
        {{ product.description ? product.description : "Описание..." }}
      </p>
      <p class="card__content-price">{{ product.price }} ₽</p>
    </div>
  </RouterLink>
</template>

<script setup>
import { RouterLink } from "vue-router";

defineProps({
  product: Object,
});
</script>

<style lang="scss" scoped>
.card {
  background-color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;

  &:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
  }

  &__image {
    width: 100%;
    height: 192px;
    object-fit: cover;
  }

  &__content {
    display: flex;
    flex-direction: column;
    height: 200px;
    padding: 16px;

    &-title {
      font-size: 18px;
      font-weight: 600;
      color: #1a202c;
    }

    &-description {
      font-size: 14px;
      color: #4a5568;
      margin-top: 8px;
      flex-grow: 1;
    }

    &-price {
      font-size: 20px;
      font-weight: bold;
      color: var(--blue);
      margin-top: 8px;
    }
  }
}
</style>

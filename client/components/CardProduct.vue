<template>
  <RouterLink :to="`/products/${product.id}`" class="card">
    <div class="card__image-container">
      <img
        :src="product.photo_url ? product.photo_url : `/images/hisense.png`"
        :alt="product.name"
        class="card__image"
        loading="lazy"
      />
    </div>

    <div class="card__content">
      <h3 class="card__content-title">{{ product.name }}</h3>
      <p class="card__content-description">
        {{ product.description ? product.description : "Описание..." }}
      </p>
      <p class="card__content-price">{{ product.price }} ₽</p>
    </div>
  </RouterLink>
</template>

<script setup lang="ts">
import { RouterLink } from "vue-router";

interface Product {
  id: number;
  name: string;
  description?: string;
  price: number;
  photo_url?: string;
}

defineProps<{
  product: Product;
}>();
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

  &__image-container {
    width: 100%;
    height: 192px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
  }

  &__image {
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
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

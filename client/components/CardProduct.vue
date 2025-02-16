<template>
  <div class="card">
    <img
      :src="product.image"
      :alt="product.name"
      class="card__image"
      loading="lazy"
    />
    <div class="card__content">
      <h3 class="card__title">{{ product.name }}</h3>
      <p class="card__description">{{ product.description }}</p>
      <p class="card__price">{{ product.price }} ₽</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  product: Object,
});
</script>

<style scoped>
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

  .card__image {
    width: 100%;
    height: 192px;
    object-fit: cover;
  }

  .card__content {
    display: flex;
    flex-direction: column;
    height: 200px;
    padding: 16px;

    .card__title {
      font-size: 18px;
      font-weight: 600;
      color: #1a202c;
    }

    .card__description {
      font-size: 14px;
      color: #4a5568;
      margin-top: 8px;
      flex-grow: 1;
    }

    .card__price {
      font-size: 20px;
      font-weight: bold;
      color: var(--blue);
      margin-top: 8px;
    }
  }
}
</style>

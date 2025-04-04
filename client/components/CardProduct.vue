<template>
  <RouterLink
    :to="`/products/${product.id}`"
    class="card"
    itemscope
    itemtype="http://schema.org/Product"
  >
    <img
      :src="product.photo_url || '/images/hisense.png'"
      :alt="`Купить ${product.name} в Тюмени`"
      class="card__image"
      loading="lazy"
      itemprop="image"
      width="300"
      height="200"
    />

    <div class="card__content">
      <h3 class="card__content-title" itemprop="name">{{ product.name }}</h3>
      <div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
        <p class="card__content-price" itemprop="price">
          {{ product.price }} ₽
        </p>
        <meta itemprop="priceCurrency" content="RUB" />
      </div>
      <p class="card__content-description" itemprop="description">
        {{ product.description || "Профессиональная установка кондиционеров" }}
      </p>
    </div>
  </RouterLink>
</template>

<script setup>
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
  display: flex;
  flex-direction: column;
  height: 100%;

  &:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
  }

  &__image {
    padding: 0 12px;
    width: 100%;
    height: 200px;
    object-fit: contain;
  }

  &__content {
    display: flex;
    flex-direction: column;
    padding: 16px;
    flex-grow: 1;
    position: relative;

    &-title {
      font-size: 18px;
      font-weight: 600;
      color: #1a202c;
      margin-bottom: 8px;
    }

    &-description {
      font-size: 14px;
      color: #4a5568;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 8px;
      flex-grow: 1;
      min-height: 60px;
      position: relative;

      // Градиентная тень внизу текста
      &::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 20px;
        background: linear-gradient(
          to bottom,
          rgba(255, 255, 255, 0) 0%,
          rgba(255, 255, 255, 0.9) 100%
        );
      }
    }

    &-price {
      font-size: 20px;
      font-weight: bold;
      color: var(--blue);
      margin-top: auto;
    }
  }

  @media (max-width: 768px) {
    &__image {
      height: 160px;
    }

    &__content {
      padding: 12px;

      &-title {
        font-size: 16px;
      }

      &-description {
        font-size: 13px;
        min-height: 54px;

        &::after {
          height: 15px;
        }
      }

      &-price {
        font-size: 18px;
      }
    }
  }

  @media (max-width: 480px) {
    &__image {
      height: 140px;
    }

    &__content {
      padding: 10px;

      &-title {
        font-size: 15px;
      }

      &-description {
        font-size: 12px;
        -webkit-line-clamp: 2;
        min-height: 48px;

        &::after {
          height: 12px;
        }
      }

      &-price {
        font-size: 16px;
      }
    }
  }
}
</style>

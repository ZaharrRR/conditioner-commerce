<template>
  <Section label="Новинки">
    <div class="new">
      <div class="new__cards">
        <div class="card" v-for="(product, index) in products" :key="index">
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
      </div>

      <div class="new__more-button">
        <UButton @click="loadMore">Показать больше</UButton>
      </div>
    </div>
  </Section>
</template>

<script setup lang="ts">
import Section from "./Section.vue";
import UButton from "~/components/UI/UButton.vue";

const products = [
  {
    name: "Hisense AS-24HR4SBADC005",
    description: "Кондиционер (настенная сплит система) серии NEO Classic A",
    price: "66,890",
    image: "/images/hisense.png",
  },
  {
    name: "Hisense AS-24HR4SBADC005",
    description: "Кондиционер (настенная сплит система) серии NEO Classic A",
    price: "66,890",
    image: "/images/hisense.png",
  },
  {
    name: "Hisense AS-24HR4SBADC005",
    description: "Кондиционер (настенная сплит система) серии NEO Classic A",
    price: "66,890",
    image: "/images/hisense.png",
  },
  {
    name: "Hisense AS-24HR4SBADC005",
    description: "Кондиционер (настенная сплит система) серии NEO Classic A",
    price: "66,890",
    image: "/images/hisense.png",
  },
];

const loadMore = () => {
  // Логика для загрузки дополнительных товаров
  console.log("Загрузить больше товаров");
};
</script>

<style lang="scss" scoped>
.new {
  @apply flex flex-col items-center;

  .new__cards {
    @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 w-full;

    .card {
      @apply bg-white shadow-lg rounded-lg overflow-hidden transition-transform transform hover:scale-105;

      .card__image {
        @apply w-full h-48 object-cover;
      }

      .card__content {
        @apply p-4;

        .card__title {
          @apply text-lg font-semibold text-gray-800;
        }

        .card__description {
          @apply text-sm text-gray-600 mt-2;
        }

        .card__price {
          @apply text-xl font-bold text-[var(--blue)] mt-2;
        }
      }
    }
  }

  .new__more-button {
    @apply mt-8;
  }
}
</style>

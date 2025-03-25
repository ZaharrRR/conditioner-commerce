<template>
  <Section label="Новинки">
    <div class="new">
      <div class="new__cards">
        <RouterLink
          to="/products/1"
          class="card"
          v-for="(product, index) in products"
          :key="index"
        >
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
        </RouterLink>
      </div>

      <div class="new__more-button">
        <RouterLink to="/products">
          <UButton>Показать больше</UButton></RouterLink
        >
      </div>
    </div>
  </Section>
</template>

<script setup>
import Section from "./Section.vue";
import UButton from "~/components/UI/UButton.vue";

const products = [
  {
    name: "Hisense AS-24HR4SBADC005",
    description: "Кондиционер (настенная сплит система) серии NEO Classic A",
    price: 63314,
    rating: 4,
    brand: "Samsung",
    category: "Электроника",
    image: "/images/hisense.png",
  },
  {
    name: "Hisense AS-24HR4SBADC005",
    description: "Кондиционер (настенная сплит система) серии NEO Classic A",
    price: 2134,
    rating: 4.3,
    brand: "Balu",
    category: "Кондеи",
    image: "/images/hisense.png",
  },
  {
    name: "Hisense AS-24HR4SBADC005",
    description: "Кондиционер (настенная сплит система) серии NEO Classic A",
    price: 6689,
    rating: 3,
    brand: "Balu",
    category: "Электроника",
    image: "/images/hisense.png",
  },
  {
    name: "Hisense AS-24HR4SBADC005",
    description: "Кондиционер (настенная сплит система) серии NEO Classic A",
    price: 5346,
    rating: 4.9,
    brand: "Samsung",
    category: "Электроника",
    image: "/images/hisense.png",
  },
];
</script>

<style lang="scss" scoped>
.new {
  display: flex;
  flex-direction: column;
  align-items: center;

  .new__cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    width: 100%;

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
        }

        .card__price {
          font-size: 20px;
          font-weight: bold;
          color: var(--blue);
          margin-top: 8px;
        }
      }
    }
  }

  .new__more-button {
    margin-top: 32px;
  }
}
</style>

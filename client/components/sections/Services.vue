<template>
  <Section label="Услуги">
    <div class="services">
      <div class="services__cards">
        <div class="card" v-for="(service, index) in services" :key="index">
          <img
            :src="service.image"
            :alt="service.title"
            class="card__image"
            loading="lazy"
          />
          <div class="card__content">
            <h3 class="card__title">{{ service.title }}</h3>
            <p class="card__description">{{ service.description }}</p>
            <p class="card__price">{{ service.price }} ₽</p>
          </div>
        </div>
      </div>
    </div>
  </Section>
</template>

<script setup lang="ts">
import Section from "./Section.vue";

const services = [
  {
    title: "Установка сплит системы",
    description:
      "Профессиональная установка сплит-системы с гарантией качества.",
    price: "1,499",
    image: "/images/install.png",
  },
  {
    title: "Обслуживание кондиционеров",
    description:
      "Регулярное техническое обслуживание для поддержания работоспособности.",
    price: "999",
    image: "/images/maintenance.png",
  },
  {
    title: "Ремонт холодильного оборудования",
    description: "Быстрый и качественный ремонт холодильных установок.",
    price: "2,499",
    image: "/images/repair.png",
  },
];
</script>

<style lang="scss" scoped>
.services {
  @apply flex flex-col items-center;

  .services__cards {
    @apply grid grid-cols-1 md:grid-cols-3 gap-6 w-full;

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
}
</style>

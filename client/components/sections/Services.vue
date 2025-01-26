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
  display: flex;
  flex-direction: column;
  align-items: center;

  .services__cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
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
}
</style>

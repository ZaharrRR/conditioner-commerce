<template>
  <Section label="Услуги">
    <div class="services" itemscope itemtype="https://schema.org/ItemList">
      <div class="services__cards">
        <div
          v-for="(service, index) in services"
          :key="index"
          class="card"
          itemprop="itemListElement"
          itemscope
          itemtype="https://schema.org/Service"
        >
          <meta itemprop="serviceType" content="Монтаж кондиционеров" />
          <img
            :src="service.logo_url"
            :alt="`${service.service_type} в Тюмени`"
            class="card__image"
            loading="lazy"
            itemprop="image"
          />
          <div class="card__content">
            <h3 class="card__title" itemprop="name">
              {{ service.service_type }}
            </h3>
            <p class="card__description" itemprop="description">
              {{ service.description }}
            </p>
            <div
              itemprop="offers"
              itemscope
              itemtype="https://schema.org/Offer"
            >
              <p class="card__price" itemprop="price">
                {{ service.base_price }} ₽
              </p>
              <meta itemprop="priceCurrency" content="RUB" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </Section>
</template>

<script setup>
import Section from "./Section.vue";

import { getServiceWithLogo } from "~/api/services";

const services = ref([]);

onMounted(async () => {
  services.value = await getServiceWithLogo();
});
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

    @media (max-width: 720px) {
      grid-template-columns: repeat(2, 1fr); // 2 колонки
      gap: 16px;

      .card {
        .card__image {
          height: 160px; // Уменьшаем высоту изображения
        }

        .card__content {
          padding: 12px;

          .card__title {
            font-size: 16px; // Корректируем размер шрифта
          }

          .card__description {
            font-size: 13px; // Уменьшаем описание
            -webkit-line-clamp: 3; // Ограничиваем текст
            display: -webkit-box;
            -webkit-box-orient: vertical;
            overflow: hidden;
          }

          .card__price {
            font-size: 18px; // Меньший размер цены
          }
        }
      }
    }

    @media (max-width: 480px) {
      grid-template-columns: 1fr; // 1 колонка
      gap: 12px;
      padding: 0 8px; // Боковые отступы

      .card {
        .card__image {
          height: 140px; // Дополнительное уменьшение
        }

        .card__content {
          padding: 10px;

          .card__title {
            font-size: 15px;
          }

          .card__description {
            font-size: 12px;
            -webkit-line-clamp: 4; // Больше строк для узкого экрана
          }

          .card__price {
            font-size: 16px;
          }
        }
      }
    }

    .card {
      background-color: white;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease;

      &:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 12px rgba(156, 140, 140, 0.2);
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

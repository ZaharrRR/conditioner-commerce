<template>
  <Section label="Новинки">
    <div class="new">
      <div class="new__cards">
        <RouterLink
          v-for="(product, index) in products"
          :key="index"
          :to="`/products/${product.id}`"
          class="card"
          itemprop="itemListElement"
          itemscope
          itemtype="https://schema.org/Product"
        >
          <img
            :src="product.photo_url || '/images/hisense.png'"
            :alt="`Купить ${product.name} в Тюмени`"
            class="card__image"
            loading="lazy"
            itemprop="image"
          />
          <div class="card__content">
            <h3 class="card__title" itemprop="name">{{ product.name }}</h3>

            <meta itemprop="brand" content="Hisense" />
            <p class="card__price" itemprop="price">{{ product.price }} ₽</p>
            <meta itemprop="priceCurrency" content="RUB" />
            <link itemprop="availability" href="https://schema.org/InStock" />
            <p class="card__description" itemprop="description">
              {{ product.description }}
            </p>
            <div
              itemprop="offers"
              itemscope
              itemtype="https://schema.org/Offer"
            ></div>
          </div>
        </RouterLink>
      </div>
    </div>
  </Section>
</template>

<script setup>
import { ref, onMounted } from "vue";

import Section from "./Section.vue";

import { getNewProducts } from "@/api/products";

const products = ref([]);

onMounted(async () => {
  products.value = await getNewProducts();
});
</script>

<style lang="scss" scoped>
.card {
  max-height: 400px;

  .card__content {
    max-height: 200px;
  }
}

.new {
  display: flex;
  flex-direction: column;
  align-items: center;

  .new__cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    width: 100%;

    .card__image {
      padding: 0 12px;
      max-width: 100%;
      max-height: 100%;
      margin: 0 auto;
      width: auto;
      height: 200px;
      object-fit: contain;
    }

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
            font-size: 16px; // Уменьшаем размер заголовка
          }

          .card__description {
            font-size: 13px; // Уменьшаем размер описания
          }

          .card__price {
            font-size: 18px; // Уменьшаем размер цены
          }
        }
      }
    }

    @media (max-width: 480px) {
      grid-template-columns: 1fr; // 1 колонка
      gap: 12px;

      .card {
        .card__image {
          height: 140px; // Дополнительное уменьшение высоты
        }

        .card__content {
          padding: 10px;

          .card__title {
            font-size: 15px;
          }

          .card__description {
            font-size: 12px;
            display: -webkit-box; // Ограничиваем текст до 3 строк
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
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

    @media (max-width: 720px) {
      margin-top: 24px;
    }

    @media (max-width: 480px) {
      margin-top: 20px;

      // Если нужно изменить размер кнопки
      .u-button {
        padding: 10px 20px;
        font-size: 14px;
      }
    }
  }
}
</style>

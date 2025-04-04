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
    display: flex;
    flex-direction: column;
    height: 100%;

    &:hover {
      transform: translateY(-10px);
      box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
    }

    .card__image {
      padding: 0 12px;
      width: 100%;
      height: 200px;
      object-fit: contain;
    }

    .card__content {
      padding: 16px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      position: relative; // Для градиентной тени

      .card__title {
        font-size: 18px;
        font-weight: 600;
        color: #1a202c;
        margin-bottom: 8px;
      }

      .card__description {
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

      .card__price {
        font-size: 20px;
        font-weight: bold;
        color: var(--blue);
        margin-top: auto;
      }
    }
  }

  @media (max-width: 1024px) {
    grid-template-columns: repeat(3, 1fr);
  }

  @media (max-width: 720px) {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;

    .card {
      .card__image {
        height: 160px;
      }

      .card__content {
        padding: 12px;

        .card__title {
          font-size: 16px;
        }

        .card__description {
          font-size: 13px;
          min-height: 54px;

          &::after {
            height: 15px;
          }
        }

        .card__price {
          font-size: 18px;
        }
      }
    }
  }

  @media (max-width: 480px) {
    grid-template-columns: 1fr;
    gap: 12px;

    .card {
      .card__image {
        height: 140px;
      }

      .card__content {
        padding: 10px;

        .card__title {
          font-size: 15px;
        }

        .card__description {
          font-size: 12px;
          -webkit-line-clamp: 2;
          min-height: 48px;

          &::after {
            height: 12px;
          }
        }

        .card__price {
          font-size: 16px;
        }
      }
    }
  }
}
</style>

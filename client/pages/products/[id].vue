<template>
  <NuxtLayout name="page-layout">
    <div class="product-box" v-if="product">
      <img
        :src="product.photo_url ? product.photo_url : `/images/hisense.png`"
        :alt="product.name"
      />
      <div class="product-info">
        <h1>{{ product.name }}</h1>
        <p>{{ product.price }} ₽</p>
        <UButton>Оставить заявку</UButton>

        <div class="product-spec">
          <h2>Характеристики</h2>
          <div class="spec-icons">
            <div class="spec-icon" v-if="hasAttribute('Площадь помещения')">
              <Icon name="mdi:cube-outline" class="icon" />
              <p>Площадь помещения</p>
              <p>{{ getAttributeValue("Площадь помещения") }}</p>
            </div>
            <div class="spec-icon" v-if="hasAttribute('Мощность охлаждения')">
              <Icon name="ri:snowflake-fill" class="icon" />
              <p>Мощность охлаждения</p>
              <p>{{ getAttributeValue("Мощность охлаждения") }}</p>
            </div>
            <div class="spec-icon" v-if="hasAttribute('Гарантия')">
              <Icon name="material-symbols:settings" class="icon" />
              <p>Гарантия</p>
              <p>{{ getAttributeValue("Гарантия") }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="product-content" v-if="product">
      <div class="description">
        <h2>Описание</h2>
        <h3>{{ product.name }}</h3>
        <p>
          {{ product.description }}
        </p>
      </div>

      <div class="characteristics">
        <h2>Характеристики</h2>
        <ul>
          <li v-for="attr in product.attributes" :key="attr.attribute_name">
            <strong>{{ attr.attribute_name }}:</strong> {{ attr.value }}
          </li>
        </ul>
      </div>
    </div>
    <Services />
  </NuxtLayout>
</template>

<script setup>
import { onMounted, ref } from "vue";

import { getProductById } from "~/api/products";

import { useRoute } from "vue-router";

const router = useRoute();

import UButton from "~/components/UI/UButton.vue";
import Services from "~/components/sections/Services.vue";

const product = ref(null);

const hasAttribute = (name) => {
  return product.value?.attributes?.some(
    (attr) => attr.attribute_name === name
  );
};

const getAttributeValue = (name) => {
  const attr = product.value?.attributes?.find(
    (attr) => attr.attribute_name === name
  );
  return attr ? attr.value : "";
};

onMounted(async () => {
  product.value = await getProductById(router.params.id);
});
</script>

<style scoped>
.product-box {
  border: solid 5px var(--blue);
  border-radius: 10px;
  padding: 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: white;
}

.product-box img {
  width: 400px;
  height: auto;
  object-fit: contain;
}

.product-info {
  width: 50%;
}

.product-info h1 {
  font-size: 36px;
  font-weight: 500;
  margin-bottom: 10px;
}

.product-info p {
  font-size: 30px;
  font-weight: 700;
  color: var(--blue);
  margin-bottom: 15px;
}

.product-spec {
  margin-top: 20px;
  background-color: var(--blue);
  border-radius: 10px;
  padding: 5px 10px;
}

.product-spec h2 {
  color: white;
  font-weight: 600;
  font-size: 24px;
  padding-left: 10px;
}

.spec-icons {
  display: flex;
  justify-content: space-around;
}

.spec-icon {
  text-align: center;
  max-width: 100px;
}

.spec-icon p {
  font-size: 18px;
  font-weight: 600;
  color: white;
  line-height: 1;
}

.icon {
  width: 75px;
  height: 75px;
  color: white;
}

.product-content {
  display: flex;
  justify-content: space-between;
  padding-top: 30px;
}

.description,
.characteristics {
  width: 48%;
}

.description h2,
.characteristics h2 {
  font-size: 22px;
  font-weight: 600;
  border-bottom: 2px solid var(--blue);
  padding-bottom: 5px;
  margin-bottom: 15px;
}

.description p {
  font-size: 14px;
  line-height: 1.5;
  color: #555;
}

.characteristics ul {
  list-style: none;
  padding: 0;
}

.characteristics li {
  font-size: 14px;
  line-height: 1.6;
  color: #333;
  margin-bottom: 5px;
}

.characteristics a,
.description a {
  display: inline-block;
  margin-top: 10px;
  color: #007bff;
  text-decoration: none;
  font-size: 14px;
}

.characteristics a:hover,
.description a:hover {
  text-decoration: underline;
}

@media (max-width: 1280px) {
  .product-box {
    padding: 30px;
    gap: 30px;
  }

  .product-box img {
    width: 350px;
  }

  .product-info h1 {
    font-size: 32px;
  }

  .product-info p {
    font-size: 26px;
  }

  .spec-icon .icon {
    width: 60px;
    height: 60px;
  }

  .spec-icon p {
    font-size: 16px;
  }
}

@media (max-width: 720px) {
  .product-box {
    flex-direction: column;
    padding: 20px;
  }

  .product-box img {
    width: 100%;
    max-width: 400px;
    margin-bottom: 20px;
  }

  .product-info {
    width: 100%;
  }

  .product-info .u-button {
    width: 100%;
  }

  .product-content {
    flex-direction: column;
  }

  .description,
  .characteristics {
    width: 100%;
    margin-bottom: 30px;
  }

  .spec-icons {
    flex-wrap: wrap;
    gap: 20px;
  }
}

@media (max-width: 480px) {
  .product-box {
    padding: 15px;
    border-width: 3px;
  }

  .product-info h1 {
    font-size: 24px;
  }

  .product-info p {
    font-size: 22px;
  }

  .spec-icons {
    flex-direction: column;
    align-items: center;
    gap: 15px;
  }

  .spec-icon {
    margin-bottom: 10px;
  }

  .product-spec {
    padding: 10px 5px;
  }

  .product-spec h2 {
    font-size: 20px;
  }

  .description h3 {
    font-size: 18px;
  }

  .description p,
  .characteristics li {
    font-size: 14px;
  }

  .characteristics a,
  .description a {
    font-size: 13px;
  }
}
</style>

<template>
  <NuxtLayout name="page-layout">
    <div class="page-wrapper">
      <div class="order-layout">
        <!-- Форма заказа -->
        <div class="order-container">
          <div class="header-row">
            <h1>Оставить заявку</h1>
            <!-- <UButton
              color="gray"
              variant="ghost"
              class="close-btn"
              @click="closeForm"
            >
              <span class="close-icon">×</span>
            </UButton> -->
          </div>

          <div class="order-inputs">
            <div class="name-row">
              <input
                type="text"
                placeholder="Имя"
                class="name"
                v-model="formData.firstName"
              />
              <input
                type="text"
                placeholder="Фамилия"
                class="surname"
                v-model="formData.lastName"
              />
            </div>
            <input
              type="tel"
              placeholder="+7(___)-___-__-__"
              class="tel"
              v-model="formData.phone"
            />
            <input
              type="text"
              placeholder="Адрес доставки"
              class="adress"
              v-model="formData.address"
            />
            <textarea
              placeholder="Комментарий"
              class="comment"
              rows="4"
              v-model="formData.comment"
            ></textarea>

            <div class="services-checkboxes">
              <label
                v-for="service in services"
                :key="service.id"
                class="checkbox-label"
              >
                <input
                  type="checkbox"
                  v-model="selectedServices"
                  :value="service.id"
                  class="checkbox-input"
                />
                <span class="checkbox-custom"></span>
                {{ service.service_type }} (+{{ service.base_price }} ₽)
              </label>
            </div>
          </div>
          <div class="action-row">
            <UButton class="submit-btn" @click.prevent="submitForm()"
              >Оставить заявку</UButton
            >
            <input
              type="text"
              class="price-display"
              :value="Math.floor(calculatedPrice)"
              readonly
            />
          </div>
        </div>

        <!-- Карточка товара -->
        <CardProduct v-if="product" :product="product" class="product-card" />
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import UButton from "~/components/UI/UButton.vue";
import CardProduct from "~/components/CardProduct.vue";
import { ref, computed } from "vue";

import { useRoute } from "vue-router";
import { getProductById } from "~/api/products";
import { createOrder } from "~/api/orders";
import { getServiceWithLogo } from "~/api/services";

const route = useRoute();

const product = ref();

const services = ref([]);

const formData = ref({
  firstName: "",
  lastName: "",
  phone: "",
  address: "",
  comment: "",
});

const selectedServices = ref([]);

const calculatedPrice = computed(() => {
  const productPrice = product.value?.price || 0;

  const servicesPrice = selectedServices.value.reduce((sum, serviceId) => {
    const service = services.value.find((s) => s.id === serviceId);
    return sum + (service ? Number(service.base_price) : 0);
  }, 0);

  return Number(productPrice) + servicesPrice;
});

const closeForm = () => {
  console.log("Форма закрыта");
};

const submitForm = async () => {
  const orderData = {
    product_id: product.value.id,
    customer_name: formData.value.firstName,
    customer_surname: formData.value.lastName,
    customer_phone: formData.value.phone,
    total_price: calculatedPrice.value,
    address: formData.value.address,
    comment: formData.value.comment,
    services: selectedServices.value,
  };

  const response = await createOrder(orderData);

  if (response.status == 200) {
    formData.value = {
      firstName: "",
      lastName: "",
      phone: "",
      address: "",
      comment: "",
    };

    selectedServices.value = [];
  }
};

onMounted(async () => {
  product.value = await getProductById(route.params.id);
  services.value = await getServiceWithLogo();
});
</script>

<style lang="scss" scoped>
:root {
  --blue: #2563eb;
  --blue-hover: #1d4ed8;
  --blue-rgb: 37, 99, 235;
}

.page-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 80px);
  padding: 20px;
}

.order-layout {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
  width: 100%;
  max-width: 1200px;
}

.order-container {
  flex: 1;
  min-width: 300px;
  max-width: 600px;
  border: 4px solid var(--blue);
  border-radius: 20px;
  padding: 20px;

  .header-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;

    h1 {
      font-size: 24px;
      font-weight: 600;
      margin: 0;
    }
  }

  .close-btn {
    padding: 0;
    width: 32px;
    height: 32px;
    min-width: auto;

    .close-icon {
      font-size: 24px;
      line-height: 1;
    }
  }

  input,
  textarea {
    background-color: #e8eaed;
    border-radius: 10px;
    padding: 12px;
    box-sizing: border-box;
    width: 100%;
    border: 1px solid #d1d5db;
    font-family: inherit;
    font-size: 14px;

    &:focus {
      outline: none;
      border-color: var(--blue);
    }
  }

  textarea.comment {
    min-height: 100px;
    resize: vertical;
  }

  input::placeholder,
  textarea::placeholder {
    font-weight: 700;
    color: #6b7280;
  }

  .order-inputs {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 20px;
  }

  .name-row {
    display: flex;
    flex-direction: column;
    gap: 12px;

    input {
      width: 100%;
    }
  }

  .action-row {
    display: flex;
    flex-direction: column;
    gap: 12px;

    .price-display {
      flex-grow: 1;
      height: auto;
      padding: 12px 10px;
      background-color: rgba(var(--blue-rgb), 0.1);
      color: var(--blue);
      font-weight: bold;
      text-align: center;
      cursor: default;
      border: 1px solid var(--blue);
      font-size: 22px;
      border-radius: 10px;

      &:focus {
        border-color: var(--blue);
      }
    }

    .submit-btn {
      padding: 14px 24px;
      height: auto;
      font-size: 16px;
      font-weight: 600;
      border-radius: 10px;
      white-space: nowrap;
      transition: all 0.3s ease;
      background-color: var(--blue);
      color: white;
      border: 1px solid var(--blue);

      &:hover {
        background-color: var(--blue-hover);
      }
    }
  }

  .services-checkboxes {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 10px;
  }

  .checkbox-label {
    display: flex;
    align-items: center;
    cursor: pointer;
    font-size: 14px;
    user-select: none;
    gap: 8px;
  }

  .checkbox-input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;

    &:checked ~ .checkbox-custom {
      background-color: var(--blue);
      border-color: var(--blue);

      &::after {
        display: block;
      }
    }
  }

  .checkbox-custom {
    position: relative;
    height: 18px;
    width: 18px;
    background-color: #fff;
    border: 2px solid #d1d5db;
    border-radius: 4px;
    transition: all 0.2s;

    &::after {
      content: "";
      position: absolute;
      display: none;
      left: 5px;
      top: 1px;
      width: 4px;
      height: 10px;
      border: solid white;
      border-width: 0 2px 2px 0;
      transform: rotate(45deg);
    }
  }

  .checkbox-label:hover .checkbox-input ~ .checkbox-custom {
    border-color: var(--blue);
  }
}

.product-card {
  flex: 1;
  min-width: 300px;
  max-width: 400px;
  align-self: center;
}

/* Адаптация для 480px */
@media (max-width: 480px) {
  .order-layout {
    flex-direction: column;
    align-items: center;
  }

  .product-card {
    width: 100%;
    max-width: 350px;
    margin: 20px auto 0;
    order: 2;
  }

  .order-container {
    order: 1;
    width: 100%;
    max-width: 350px;
  }
}

/* Адаптация для 720px */
@media (min-width: 481px) and (max-width: 720px) {
  .order-layout {
    flex-direction: column;
    align-items: center;
  }

  .product-card {
    width: 100%;
    max-width: 500px;
    margin: 30px auto 0;
    order: 2;
  }

  .order-container {
    order: 1;
    width: 100%;
    max-width: 500px;
  }
}

/* Десктопная версия (выше 720px) */
@media (min-width: 721px) {
  .order-layout {
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
  }

  .product-card {
    position: sticky;
    top: 20px;
    margin-left: 30px;
    margin-top: 0;
    align-self: flex-start;
  }

  .order-container {
    margin-right: 30px;
  }
}

/* Дополнительные адаптивные стили */
@media (min-width: 480px) {
  .order-container {
    padding: 24px;

    .header-row h1 {
      font-size: 26px;
    }

    .action-row {
      .price-display {
        font-size: 24px;
      }
    }
  }
}

@media (min-width: 720px) {
  .order-container {
    .name-row {
      flex-direction: row;
      gap: 15px;
    }

    .action-row {
      flex-direction: row;
      align-items: stretch;

      .submit-btn {
        width: 60%;
      }

      .price-display {
        font-size: 26px;
        width: 40%;
      }
    }
  }
}

@media (min-width: 1280px) {
  .order-container {
    padding: 32px;

    .header-row h1 {
      font-size: 32px;
    }

    .order-inputs {
      gap: 15px;
    }

    input,
    textarea {
      padding: 14px;
      font-size: 15px;
    }

    .action-row {
      .submit-btn {
        font-size: 17px;
      }

      .price-display {
        font-size: 28px;
      }
    }

    .services-checkboxes {
      gap: 15px;
    }

    .checkbox-label {
      font-size: 15px;
    }
  }

  .product-card {
    max-width: 450px;
  }
}
</style>

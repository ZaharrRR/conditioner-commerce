<template>
  <NuxtLayout name="page-layout">
    <div class="delivery-page">
      <h1>Доставка кондиционеров и климатического оборудования</h1>
      <p class="intro-text">
        Мы заботимся о вашем комфорте и предлагаем быструю и удобную доставку
        кондиционеров и сопутствующих товаров по вашему адресу.
      </p>

      <div class="delivery-options">
        <div class="delivery-card">
          <Icon name="mdi:truck-delivery" class="icon" />
          <h2>Доставка по городу</h2>
          <p><strong>Срок:</strong> 1–2 рабочих дня</p>
          <p>
            <strong>Стоимость:</strong> Бесплатно при заказе от 10 000 руб.,
            иначе – 500 руб.
          </p>
        </div>

        <div class="delivery-card">
          <Icon name="mdi:rocket-launch" class="icon" />
          <h2>Экспресс-доставка</h2>
          <p><strong>Срок:</strong> 1–2 рабочих дня</p>
          <p>
            <strong>Стоимость:</strong> Бесплатно при заказе от 10 000 руб.,
            иначе – 500 руб.
          </p>
        </div>

        <div class="delivery-card">
          <Icon name="mdi:package-variant" class="icon" />
          <h2>Самовывоз</h2>
          <p><strong>Срок:</strong> 1–2 рабочих дня</p>
          <p>
            <strong>Стоимость:</strong> Бесплатно при заказе от 10 000 руб.,
            иначе – 500 руб.
          </p>
        </div>
      </div>

      <div class="installation-info">
        <h2>Установка в день доставки</h2>
        <p>
          Если вы заказали установку кондиционера, наши мастера могут установить
          его сразу после доставки.
        </p>
      </div>

      <button class="order-button" @click="orderDelivery">
        Заказать доставку
      </button>
    </div>
  </NuxtLayout>
</template>

<script setup>
const orderDelivery = () => {
  // Логика для заказа доставки
  alert("Заказ доставки оформлен!");
};
</script>

<style lang="scss" scoped>
.delivery-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  color: #333;

  h1 {
    font-size: 32px;
    margin-bottom: 20px;
    color: #007bff;
  }

  .intro-text {
    font-size: 18px;
    margin-bottom: 40px;
    line-height: 1.6;
  }

  .delivery-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 40px;

    .delivery-card {
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      text-align: center;

      &:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
      }

      .icon {
        font-size: 48px;
        color: #007bff;
        margin-bottom: 15px;
      }

      h2 {
        font-size: 24px;
        margin-bottom: 15px;
        color: #007bff;
      }

      p {
        font-size: 16px;
        margin: 10px 0;
        color: #555;
      }
    }
  }

  .installation-info {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 40px;

    h2 {
      font-size: 24px;
      margin-bottom: 15px;
      color: #007bff;
    }

    p {
      font-size: 16px;
      color: #555;
      line-height: 1.6;
    }
  }

  .order-button {
    display: block;
    width: 100%;
    max-width: 300px;
    margin: 0 auto;
    padding: 15px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: #0056b3;
    }
  }
}
</style>

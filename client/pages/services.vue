<template>
  <NuxtLayout name="page-layout">
    <div class="services-page">
      <div class="services-intro">
        <h1>Наши услуги</h1>
        <p class="intro-text">
          Обеспечьте своему оборудованию долгую и надёжную работу с помощью
          наших профессиональных услуг.
        </p>
      </div>

      <div class="services-overview">
        <div
          class="service-card"
          style="background-image: url('/images/install.png')"
        >
          <div class="card-content">
            <h2>Установка сплит-системы</h2>
            <p>
              Профессиональная установка сплит-системы с гарантией качества. Мы
              обеспечиваем правильный монтаж и настройку оборудования для его
              долгой и надежной работы.
            </p>
            <button
              class="service-button"
              @click="orderService('Установка сплит-системы')"
            >
              Заказать услугу
            </button>
          </div>
        </div>

        <div
          class="service-card"
          style="background-image: url('/images/maintenance.png')"
        >
          <div class="card-content">
            <h2>Обслуживание кондиционеров</h2>
            <p>
              Регулярное техническое обслуживание для поддержания
              работоспособности вашего кондиционера. Мы проводим чистку,
              диагностику и профилактику для предотвращения поломок.
            </p>
            <button
              class="service-button"
              @click="orderService('Обслуживание кондиционеров')"
            >
              Заказать услугу
            </button>
          </div>
        </div>

        <div
          class="service-card"
          style="background-image: url('/images/repair.png')"
        >
          <div class="card-content">
            <h2>Ремонт холодильного оборудования</h2>
            <p>
              Быстрый и качественный ремонт холодильных установок. Наши
              специалисты оперативно устраняют неисправности и возвращают
              оборудование в рабочее состояние.
            </p>
            <button
              class="service-button"
              @click="orderService('Ремонт холодильного оборудования')"
            >
              Заказать услугу
            </button>
          </div>
        </div>
      </div>

      <div class="process-info">
        <h2>Как мы работаем</h2>
        <div class="process-steps">
          <div class="step">
            <h3>1. Заявка</h3>
            <p>Вы оставляете заявку на сайте или звоните нам.</p>
          </div>
          <div class="step">
            <h3>2. Диагностика</h3>
            <p>
              Специалист выезжает к вам, проводит диагностику и определяет объём
              работ.
            </p>
          </div>
          <div class="step">
            <h3>3. Ремонт и обслуживание</h3>
            <p>Выполняем необходимые работы в кратчайшие сроки.</p>
          </div>
          <div class="step">
            <h3>4. Проверка и гарантия</h3>
            <p>
              Проверяем работоспособность оборудования и предоставляем гарантию
              на выполненные работы.
            </p>
          </div>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
const orderService = (serviceName) => {
  // Логика для заказа услуги
  alert(`Заказ услуги "${serviceName}" оформлен!`);
};
</script>

<style lang="scss" scoped>
.services-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;

  .services-intro {
    text-align: center;
    margin-bottom: 40px;

    h1 {
      font-size: 48px;
      font-weight: 700;
      margin-bottom: 20px;
    }

    .intro-text {
      font-size: 24px;
      color: #555;
      line-height: 1.6;
    }
  }

  .services-overview {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 40px;

    .service-card {
      background-size: cover;
      background-position: center;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      position: relative;
      overflow: hidden;
      min-height: 300px;
      display: flex;
      align-items: flex-end;

      &::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.5);
        z-index: 1;
      }

      .card-content {
        position: relative;
        z-index: 2;
        color: #fff;
        text-align: center;
        width: 100%;

        h2 {
          font-size: 24px;
          font-weight: 700;
          margin-bottom: 15px;
        }

        p {
          font-size: 16px;
          line-height: 1.6;
          margin-bottom: 20px;
        }

        .service-button {
          padding: 10px 20px;
          background-color: #007bff;
          color: #fff;
          border: none;
          border-radius: 5px;
          font-size: 16px;
          cursor: pointer;
          transition: background-color 0.3s ease;

          &:hover {
            background-color: #0056b3;
          }
        }
      }

      &:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
      }
    }
  }

  .process-info {
    background-color: #f9f9f9;
    padding: 40px;
    border-radius: 10px;
    text-align: center;

    h2 {
      font-size: 32px;
      margin-bottom: 40px;
      color: #007bff;
    }

    .process-steps {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;

      .step {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);

        h3 {
          font-size: 20px;
          font-weight: 700;
          margin-bottom: 15px;
        }

        p {
          font-size: 16px;
          color: #555;
          line-height: 1.6;
        }
      }
    }
  }
}
</style>

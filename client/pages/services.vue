<template>
  <NuxtLayout name="page-layout">
    <div class="services-page">
      <div class="services-intro">
        <h1 class="intro-text">
          Обеспечьте своему оборудованию долгую и надёжную работу.
        </h1>
        <div class="process-info">
          <div class="process-steps">
            <div class="step">
              <h3><span>1.</span> Заявка</h3>
              <p>Вы оставляете заявку на сайте или звоните нам.</p>
            </div>
            <div class="step">
              <h3><span>2.</span> Диагностика</h3>
              <p>
                Специалист выезжает к вам, проводит диагностику и определяет
                объём работ.
              </p>
            </div>
            <div class="step">
              <h3><span>3.</span> Ремонт и обслуживание</h3>
              <p>Выполняем необходимые работы в кратчайшие сроки.</p>
            </div>
            <div class="step">
              <h3><span>4.</span> Проверка и гарантия</h3>
              <p>
                Проверяем работоспособность оборудования и предоставляем
                гарантию на выполненные работы.
              </p>
            </div>
            <button
              class="service-button"
              @click="orderService('Установка сплит-системы')"
            >
              Заказать услугу
            </button>
          </div>
        </div>
      </div>

      <div class="services-overview">
        <div
          class="service-card-install"
          style="background-image: url('/images/install.png')"
        >
          <div class="card-content">
            <h2>УСТАНОВКА СПЛИТ-СИСТЕМЫ</h2>
            <p>
              Профессиональная установка сплит-системы с гарантией качества.
            </p>
          </div>
        </div>

        <div
          class="service-card"
          style="background-image: url('/images/maintenance.png')"
        >
          <div class="card-content">
            <h2>ОБСЛУЖИВАНИЕ КОНДИЦИОНЕРОВ</h2>
            <p>
              Регулярное техническое обслуживание для поддержания
              работоспособности вашего кондиционера.
            </p>
          </div>
        </div>

        <div
          class="service-card"
          style="background-image: url('/images/repair.png')"
        >
          <div class="card-content">
            <h2>РЕМОНТ ХОЛОДИЛЬНОГО ОБОРУДОВАНИЯ</h2>
            <p>Быстрый и качественный ремонт холодильных установок.</p>
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
  font-family: Arial, sans-serif;
  display: flex;

  .services-intro {
    text-align: left;
    padding: 20px;
    max-width: 350px;
    margin-bottom: 40px;
    border: solid;
    border-color: #007bff;
    border-width: 5px;
    border-radius: 20px;

    h1 {
      font-size: 48px;
      font-weight: 700;
      margin-bottom: 20px;
    }

    .intro-text {
      font-size: 36px;
      color: black;
      line-height: 1;
    }

    button {
      background-color: blue($color: #6896eb);
      border-radius: 15px;
    }
  }

  .services-overview {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto auto;
    gap: 20px;
    margin-left: 20px;
    margin-bottom: 40px;
  }

  /* Первая карточка на всю ширину */
  .service-card-install {
    grid-column: 1 / 3;
    background-size: cover;
    background-position: center;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
    min-height: 100px;
    display: flex;
    align-items: flex-end;
  }

  /* Остальные карточки */
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
  }

  .service-card::before,
  .service-card-install::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(
      180deg,
      rgba(217, 217, 217, 0) 0%,
      rgba(104, 150, 235, 0.8) 80%
    );
    z-index: 1;
  }

  .card-content {
    position: relative;
    z-index: 2;
    color: #fff;
    width: 100%;
  }

  .card-content h2 {
    font-size: 36px;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 5px;
  }

  .card-content p {
    font-size: 16px;
    line-height: 1.4;
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
  }

  .service-button:hover {
    background-color: #0056b3;
  }

  .service-card:hover,
  .service-card-install:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }

  .process-info {
    text-align: left;

    .process-steps {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));

      .step {
        padding: 20px;

        span {
          color: #007bff;
          font-weight: 900;
        }

        h3 {
          font-size: 20px;
          font-weight: 700;
          margin-bottom: 5px;
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

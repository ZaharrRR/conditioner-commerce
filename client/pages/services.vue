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
            <button class="service-button" @click="orderService()">
              Оставить заявку
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
const orderService = () => {
  location.href = "https://t.me/conditioner_comm_bot";
};
</script>

<style lang="scss" scoped>
.services-page {
  max-width: 1200px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;

  .services-intro {
    flex: 1 1 350px;
    min-width: 300px;
    padding: 20px;
    margin-bottom: 40px;
    border: 5px solid #007bff;
    border-radius: 20px;

    .intro-text {
      font-size: 36px;
      font-weight: 700;
      color: black;
      line-height: 1.2;
      margin-bottom: 30px;
    }

    .process-info {
      .process-steps {
        display: grid;
        gap: 15px;

        .step {
          padding: 10px;

          h3 {
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 8px;

            span {
              color: #007bff;
              margin-right: 5px;
            }
          }

          p {
            font-size: 16px;
            color: #555;
            line-height: 1.5;
          }
        }

        .service-button {
          width: 100%;
          padding: 15px 25px;
          background-color: #6896eb;
          color: white;
          border: none;
          border-radius: 15px;
          font-size: 18px;
          cursor: pointer;
          transition: background-color 0.3s;
          margin-top: 20px;

          &:hover {
            background-color: #5078b5;
          }
        }
      }
    }
  }

  .services-overview {
    flex: 2 1 600px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    min-width: 300px;

    .service-card-install {
      grid-column: 1 / -1;
      background-size: cover;
      background-position: center;
      border-radius: 10px;
      padding: 25px;
      min-height: 300px;
      display: flex;
      align-items: flex-end;
      position: relative;
      overflow: hidden;
      transition: transform 0.3s;

      &::before {
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
        color: white;

        h2 {
          font-size: 36px;
          font-weight: 700;
          line-height: 1.1;
          margin-bottom: 10px;
        }

        p {
          font-size: 16px;
          line-height: 1.4;
        }
      }
    }

    .service-card {
      background-size: cover;
      background-position: center;
      border-radius: 10px;
      padding: 25px;
      min-height: 250px;
      display: flex;
      align-items: flex-end;
      position: relative;
      overflow: hidden;
      transition: transform 0.3s;

      &::before {
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
        color: white;

        h2 {
          font-size: 28px;
          font-weight: 700;
          line-height: 1.1;
          margin-bottom: 10px;
        }

        p {
          font-size: 16px;
          line-height: 1.4;
        }
      }

      &:hover {
        transform: translateY(-5px);
      }
    }
  }

  @media (max-width: 1280px) {
    .services-intro {
      .intro-text {
        font-size: 32px;
      }

      .process-steps {
        .step {
          h3 {
            font-size: 18px;
          }
          p {
            font-size: 15px;
          }
        }
      }
    }

    .services-overview {
      .service-card-install {
        .card-content h2 {
          font-size: 32px;
        }
      }

      .service-card .card-content h2 {
        font-size: 24px;
      }
    }
  }

  @media (max-width: 720px) {
    flex-direction: column;

    .services-intro {
      max-width: 100%;
      margin-right: 0;

      .intro-text {
        font-size: 28px;
      }

      .service-button {
        font-size: 16px;
      }
    }

    .services-overview {
      grid-template-columns: 1fr;

      .service-card-install {
        .card-content h2 {
          font-size: 28px;
        }

        .card-content p {
          font-size: 14px;
        }
      }

      .service-card {
        min-height: 200px;

        .card-content h2 {
          font-size: 22px;
        }

        .card-content p {
          font-size: 14px;
        }
      }
    }
  }

  @media (max-width: 480px) {
    padding: 10px;

    .services-intro {
      padding: 15px;
      border-width: 3px;

      .intro-text {
        font-size: 22px;
      }

      .process-steps {
        .step {
          padding: 8px;

          h3 {
            font-size: 16px;
          }

          p {
            font-size: 14px;
          }
        }

        .service-button {
          padding: 12px;
          font-size: 14px;
        }
      }
    }

    .services-overview {
      gap: 15px;

      .service-card-install {
        padding: 15px;
        min-height: 200px;

        .card-content h2 {
          font-size: 24px;
        }
      }

      .service-card {
        padding: 15px;
        min-height: 180px;

        .card-content h2 {
          font-size: 20px;
        }
      }
    }
  }
}
</style>

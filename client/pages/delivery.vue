<template>
  <NuxtLayout name="page-layout">
    <Breadcrumbs
      :items="[
        { name: 'Главная', path: '/' },
        { name: 'Доставка', path: '/delivery' },
      ]"
    />

    <div class="delivery-page">
      <div class="delivery-intro">
        <div>
          <h1>Доставка кондиционеров в Тюмени с установкой</h1>
          <p class="intro-text">
            Мы заботимся о вашем комфорте и предлагаем быструю и удобную
            доставку кондиционеров и сопутствующих товаров по вашему адресу.
          </p>
        </div>
        <Icon name="game-icons:cardboard-box-closed" class="icon" />
      </div>

      <div class="delivery-options">
        <div class="delivery-card">
          <Icon
            name="mdi:truck-delivery"
            class="icon"
            aria-label="Иконка доставки грузовиком"
          />
          <h2>Доставка по городу</h2>
          <p><strong>Срок:</strong> 1–2 рабочих дня</p>
          <p>
            <strong>Стоимость:</strong> Бесплатно при заказе от 10 000 руб.,
            иначе – 500 руб.
          </p>
        </div>

        <div class="delivery-card">
          <Icon
            name="material-symbols:delivery-truck-bolt-outline-rounded"
            class="icon"
            aria-label="Иконка быстрой доставки грузовиком"
          />
          <h2>Экспресс-доставка</h2>
          <p><strong>Срок:</strong> 1–2 рабочих дня</p>
          <p>
            <strong>Стоимость:</strong> Бесплатно при заказе от 10 000 руб.,
            иначе – 500 руб.
          </p>
        </div>

        <div class="delivery-card">
          <Icon
            name="mdi:package-variant"
            class="icon"
            aria-label="Иконка коробки самовывоза"
          />
          <h2>Самовывоз</h2>
          <p><strong>Срок:</strong> 1–2 рабочих дня</p>
          <p>
            <strong>Стоимость:</strong> Бесплатно при заказе от 10 000 руб.,
            иначе – 500 руб.
          </p>
        </div>
      </div>

      <div class="installation-info">
        <Icon name="iconamoon:lightning-1" class="icon" />
        <div>
          <h2>Установка в день доставки</h2>
          <p>
            Если вы заказали установку кондиционера, наши мастера могут
            установить его сразу после доставки.
          </p>
          <button
            class="order-button"
            @click="orderDelivery"
            itemprop="potentialAction"
            itemscope
            itemtype="https://schema.org/OrderAction"
          >
            <a
              href="https://t.me/conditioner_comm_bot"
              itemprop="url"
              itemscope
              itemtype="https://schema.org/ContactPoint"
            >
              <meta itemprop="contactType" content="sales" />
              <meta itemprop="telegram" content="conditioner_comm_bot" />
              Заказать в Telegram
            </a>
          </button>
        </div>
      </div>

      <FaqSection
        title="Частые вопросы о доставке"
        :items="[
          {
            question: 'Можно ли изменить адрес доставки?',
            answer:
              'Да, для изменения адреса свяжитесь с нами по телефону +7 (912) 243-33-33',
          },
        ]"
      />

      <SeoText
        text="Быстрая и надежная доставка кондиционеров по Тюмени и области.
        Профессиональные грузчики, аккуратная транспортировка оборудования.
        Самовывоз со склада в центре города."
      />
    </div>
  </NuxtLayout>
</template>

<script setup>
import Breadcrumbs from "~/components/common/Breadcrumbs.vue";
import FaqSection from "~/components/common/FaqSection.vue";
import SeoText from "~/components/common/SeoText.vue";

const orderDelivery = () => {
  location.href = "https://t.me/conditioner_comm_bot";
};

useSeoMeta({
  title:
    "Доставка кондиционеров в Тюмени | Бесплатно от 10 000₽ | Установка в день доставки",
  description:
    "🚚 Быстрая доставка сплит-систем по Тюмени: 1-2 дня. Бесплатно при заказе от 10 000₽. Самовывоз или монтаж в день получения. Официальная гарантия на технику и работы.",
  keywords:
    "доставка кондиционеров Тюмень, стоимость доставки сплит-систем, самовывоз кондиционеров, установка в день доставки, бесплатная доставка кондиционеров",
  ogTitle: "Условия доставки кондиционеров в Тюмени | Бесплатно от 10 000₽",
  ogDescription:
    "✅ Закажите доставку с установкой за 1 день! ✅ Бесплатный подъем на этаж. ✅ 3 варианта получения заказа. Работаем по всей Тюмени и области.",
  ogType: "website",
  ogUrl: "https://абсолютхолод.рф/delivery",
  ogImage: "https://абсолютхолод.рф/images/og.jpg",
});

useHead({
  link: [{ rel: "canonical", href: "https://абсолютхолод.рф/delivery" }],
  script: [
    {
      type: "application/ld+json",
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "ShippingDeliveryTime",
        name: "Доставка кондиционеров",
        areaServed: {
          "@type": "City",
          name: "Тюмень",
        },
        deliveryTime: {
          "@type": "QuantitativeValue",
          minValue: 1,
          maxValue: 2,
          unitCode: "DAY",
        },
        eligibleTransactionVolume: {
          "@type": "PriceSpecification",
          price: 10000,
          priceCurrency: "RUB",
        },
        hasDeliveryMethod: ["ParcelService", "OnSitePickup"],
      }),
    },
    {
      type: "application/ld+json",
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        mainEntity: [
          {
            "@type": "Question",
            name: "Как отследить статус заказа?",
            acceptedAnswer: {
              "@type": "Answer",
              text: "После оформления заказа вы получите SMS с номером для отслеживания",
            },
          },
        ],
      }),
    },
  ],
});
</script>

<style lang="scss" scoped>
.delivery-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;

  .delivery-intro {
    display: flex;
    gap: 48px;
    align-items: center;

    h1 {
      font-size: 48px;
      font-weight: 700;
      margin-bottom: 20px;
    }

    .intro-text {
      font-size: 24px;
      margin-bottom: 40px;
      line-height: 1.6;
    }

    .icon {
      font-size: 400px;
      color: var(--blue);
    }
  }

  .delivery-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 40px;

    .delivery-card {
      background-color: #fff;
      border: 4px solid var(--blue);
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      text-align: center;

      .icon {
        font-size: 100px;
        color: var(--blue);
      }

      h2 {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 15px;
      }

      p {
        font-size: 16px;
        margin: 10px 0;
        color: #555;
      }
    }
  }

  .installation-info {
    display: flex;
    gap: 20px;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 40px;
    text-align: center;

    h2 {
      font-size: 48px;
      font-weight: 700;
      margin-bottom: 15px;
    }

    p {
      font-size: 20px;
      color: #555;
      line-height: 1.6;
      width: 60%;
      margin: 0 auto;
    }

    .icon {
      font-size: 250px;
      color: var(--blue);
    }
  }

  .order-button {
    display: block;
    width: 200px;
    max-width: 300px;
    margin: 0 auto;
    margin-top: 32px;
    padding: 10px;
    background-color: var(--blue);
    color: #fff;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
}

@media (max-width: 1280px) {
  .delivery-page {
    .delivery-intro {
      h1 {
        font-size: 40px;
      }

      .intro-text {
        font-size: 20px;
      }

      .icon {
        font-size: 300px;
      }
    }

    .delivery-options {
      .delivery-card {
        h2 {
          font-size: 22px;
        }
      }
    }

    .installation-info {
      h2 {
        font-size: 36px;
      }

      p {
        font-size: 18px;
        width: 70%;
      }

      .icon {
        font-size: 200px;
      }
    }
  }
}

@media (max-width: 720px) {
  .delivery-page {
    padding: 15px;

    .delivery-intro {
      flex-direction: column;
      gap: 30px;
      text-align: center;

      h1 {
        font-size: 32px;
      }

      .intro-text {
        font-size: 18px;
        margin-bottom: 30px;
      }

      .icon {
        font-size: 200px;
      }
    }

    .delivery-options {
      grid-template-columns: 1fr;
      gap: 15px;

      .delivery-card {
        padding: 15px;

        .icon {
          font-size: 80px;
        }

        h2 {
          font-size: 20px;
        }

        p {
          font-size: 14px;
        }
      }
    }

    .installation-info {
      flex-direction: column;
      align-items: center;
      padding: 15px;

      h2 {
        font-size: 28px;
      }

      p {
        width: 100%;
        font-size: 16px;
      }

      .icon {
        font-size: 150px;
      }
    }

    .order-button {
      width: 100%;
      max-width: none;
      margin-top: 20px;
    }
  }
}

@media (max-width: 480px) {
  .delivery-page {
    .delivery-intro {
      h1 {
        font-size: 24px;
      }

      .intro-text {
        font-size: 16px;
      }

      .icon {
        display: none;
      }
    }

    .delivery-options {
      .delivery-card {
        .icon {
          font-size: 60px;
        }

        h2 {
          font-size: 18px;
        }
      }
    }

    .installation-info {
      h2 {
        font-size: 24px;
      }

      p {
        font-size: 14px;
      }

      .icon {
        font-size: 100px;
      }
    }

    .order-button {
      font-size: 16px;
      padding: 8px;
    }
  }
}
</style>

<template>
  <NuxtLayout name="page-layout">
    <Breadcrumbs
      :items="[
        { name: 'Главная', path: '/' },
        { name: 'Контакты', path: '/contacts' },
      ]"
    />

    <div class="items">
      <div class="map-container">
        <h1>
          <Icon
            name="material-symbols:location-on-outline"
            class="geo-icon"
          ></Icon
          >Наш офис и магазин
        </h1>
        <div style="position: relative; overflow: hidden">
          <a
            href="https://yandex.ru/maps/55/tyumen/?utm_medium=mapframe&utm_source=maps"
            style="color: #eee; font-size: 12px; position: absolute; top: 0px"
            >Тюмень</a
          ><a
            href="https://yandex.ru/maps/55/tyumen/house/ulitsa_fedyuninskogo_60k1/YkwYcwFmQU0EQFttfX1xcX9kZg==/?indoorLevel=1&ll=65.566882%2C57.100372&utm_medium=mapframe&utm_source=maps&z=17"
            style="color: #eee; font-size: 12px; position: absolute; top: 14px"
            >Улица Федюнинского, 60к1 на карте Тюмени — Яндекс Карты</a
          ><iframe
            src="https://yandex.ru/map-widget/v1/?indoorLevel=1&ll=65.566882%2C57.100372&mode=whatshere&whatshere%5Bpoint%5D=65.566883%2C57.100372&whatshere%5Bzoom%5D=17&z=17"
            width="560"
            height="400"
            frameborder="1"
            allowfullscreen="true"
            style="position: relative"
          ></iframe>
        </div>
        <p>
          <Icon
            name="material-symbols:nest-clock-farsight-analog-outline-rounded"
            class="time-icon"
          ></Icon
          >Режим работы: ежедневно c 8:00 до 20:00
        </p>
        <p>
          <Icon
            name="material-symbols:location-on-outline"
            class="locate-icon"
          ></Icon
          >625042, Россия, Тюмень, улица Федюнинского, 60к1
        </p>
      </div>
      <div class="contacts-container">
        <h1>
          <Icon
            name="material-symbols:call-outline-rounded"
            class="phone-icon"
          ></Icon
          >Контакты
        </h1>
        <p>
          Мы всегда на связи и готовы помочь вам выбрать, купить и установить
          кондиционер!<br />Свяжитесь с нами удобным способом.
        </p>
        <div class="contact-buttons">
          <a href="https://t.me/conditioner_comm_bot" class="contact-button">
            <Icon name="mdi:telegram" class="telegam-icon"></Icon>
            <UButton>Написать</UButton>
          </a>
          <a href="tel:89124303333" class="contact-button">
            <Icon
              name="material-symbols:phone-in-talk"
              class="call-icon"
            ></Icon>
            <UButton>Позвонить</UButton>
          </a>
        </div>
      </div>
    </div>

    <div class="goodbye">
      <h1>
        <Icon
          name="material-symbols:rocket-launch-outline"
          class="rocket-icon"
        ></Icon>
        Ждем вас в нашем офисе или на связи!
      </h1>
    </div>

    <FaqSection
      title="Частые вопросы"
      :items="[
        {
          question: 'Есть ли парковка у офиса?',
          answer: 'Да, перед зданием есть парковочные места',
        },
        {
          question: 'Можно ли приехать без записи?',
          answer:
            'Да, мы принимаем клиентов в рабочее время без предварительной записи',
        },
      ]"
    />

    <SeoText
      text="Контакты магазина климатической техники в Тюмени. Адрес: ул. Федюнинского
      60к1, телефон +7 (912) 430-33-33. Режим работы без выходных с 8:00 до
      20:00. Бесплатная консультация по подбору и установке кондиционеров."
    />
  </NuxtLayout>
</template>

<script setup>
import Breadcrumbs from "~/components/common/Breadcrumbs.vue";
import FaqSection from "~/components/common/FaqSection.vue";
import SeoText from "~/components/common/SeoText.vue";
import UButton from "~/components/UI/UButton.vue";

useSeoMeta({
  title:
    "Контакты магазина кондиционеров в Тюмени | Адрес, телефон, схема проезда",
  description:
    "Наш офис в Тюмени: ул. Федюнинского 60к1. ☎ +7 (912) 430-33-33. Режим работы: ежедневно 8:00-20:00. Бесплатная парковка, Telegram-консультант",
  keywords:
    "контакты установщика кондиционеров Тюмень, адрес магазина сплит-систем, телефон климатической компании, схема проезда,  купить кондиционер в тюмени ",
  ogTitle: "Как найти наш офис в Тюмени - контакты и схема проезда",
  ogDescription:
    "Бесплатная парковка. Работаем без выходных. Приезжайте или звоните +7 (912) 430-33-33 - профессиональные консультации по кондиционерам",
  ogUrl: "https://абсолютхолод.рф/contacts",
  ogImage: "https://абсолютхолод.рф/images/og.jpg",
});

useHead({
  link: [{ rel: "canonical", href: "https://абсолютхолод.рф/contacts" }],
  script: [
    {
      type: "application/ld+json",
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        name: "Абсолют холод",
        image: "https://абсолютхолод.рф/images/logo.jpg",
        priceRange: "₽₽",
        address: {
          "@type": "PostalAddress",
          streetAddress: "ул. Федюнинского, 60к1",
          addressLocality: "Тюмень",
          postalCode: "625042",
          addressCountry: "RU",
        },
        geo: {
          "@type": "GeoCoordinates",
          latitude: 57.100372,
          longitude: 65.566882,
        },
        telephone: "+79124303333",
        openingHoursSpecification: {
          "@type": "OpeningHoursSpecification",
          dayOfWeek: [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
          ],
          opens: "08:00",
          closes: "20:00",
        },
        sameAs: ["https://t.me/conditioner_comm_bot"],
      }),
    },
  ],
});
</script>

<style lang="scss" scoped>
.items {
  display: flex;
}
/* Общие стили */
.map-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;

  .time-icon,
  .locate-icon,
  .geo-icon {
    color: var(--blue);
    transition: transform 0.3s ease;
  }

  .geo-icon {
    font-size: 30px;
  }

  .time-icon {
    font-size: 16px;
  }

  .locate-icon {
    font-size: 16px;
  }

  h1 {
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 20px;
  }

  p {
    font-size: 18px;
  }

  p:first-of-type {
    margin-top: 10px;
  }

  iframe {
    width: 100%;
    height: 400px;
  }

  > div {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
  }
}

.contacts-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  width: 50%;
  border: 4px solid var(--blue);
  border-radius: 30px;

  .phone-icon {
    font-size: 30px;
  }

  .contact-buttons {
    display: flex;
    gap: 24px;
    margin-top: 20px;
  }

  .contact-button {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 16px;
    transition: transform 0.3s ease;
    text-decoration: none;

    button {
      width: 140px;
    }

    &:hover {
      transform: translateY(-10px);
    }
  }

  .telegam-icon,
  .call-icon {
    color: var(--blue);
    font-size: 100px;
    transition: color 0.3s ease;
  }

  p {
    width: 60%;
    text-align: center;
    font-size: 18px;
  }

  h1 {
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 20px;
  }

  .phone-icon {
    color: var(--blue);
  }
}

.goodbye {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-top: 16px;
  padding: 40px 0;
  border: 4px solid var(--blue);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 30px;

  h1 {
    font-size: 40px;
    font-weight: 700;
    text-align: center;
  }

  .rocket-icon {
    color: var(--blue);
    transition: transform 0.3s ease;
  }
}

/* Медиазапросы */
@media (max-width: 1280px) {
  .items {
    display: inline;
  }
  .map-container,
  .contacts-container {
    padding: 30px 0;
    width: 100%;

    h1 {
      font-size: 36px;
    }

    > div {
      max-width: 90%;
    }
  }
}

@media (max-width: 720px) {
  .items {
    display: inline;
  }

  .map-container {
    padding: 30px 0;

    h1 {
      font-size: 32px;
    }

    .geo-icon {
      font-size: 32px;
    }

    iframe {
      height: 350px;
    }

    p {
      font-size: 16px;
    }
  }

  .contacts-container {
    padding: 30px 0;
    width: 100%;

    h1 {
      font-size: 32px;
    }

    .phone-icon {
      font-size: 32px;
    }

    p {
      width: 80%;
      font-size: 16px;
    }

    .contact-buttons {
      flex-direction: column;
      gap: 15px;
    }

    .telegam-icon,
    .call-icon {
      font-size: 80px;
    }
  }

  .goodbye {
    padding: 30px 0;

    h1 {
      font-size: 32px;
      padding: 0 20px;
    }

    .rocket-icon {
      font-size: 32px;
    }
  }
}

@media (max-width: 480px) {
  .items {
    display: inline;
  }
  .map-container {
    padding: 20px 0;

    h1 {
      font-size: 24px;
      text-align: center;
    }

    .geo-icon {
      font-size: 24px;
    }

    iframe {
      height: 250px;
    }

    p {
      font-size: 14px;
      padding: 0 10px;
      text-align: center;
    }
  }

  .contacts-container {
    padding: 20px 0;
    width: 100%;

    h1 {
      font-size: 24px;
      text-align: center;
    }

    .phone-icon {
      font-size: 24px;
    }

    p {
      width: 95%;
      font-size: 14px;
    }

    .telegam-icon,
    .call-icon {
      font-size: 70px;
    }
  }

  .goodbye {
    padding: 20px 0;
    border-radius: 20px;

    h1 {
      font-size: 24px;
      padding: 0 10px;
    }

    .rocket-icon {
      font-size: 24px;
    }
  }
}

@keyframes float {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0);
  }
}

.contact-button:hover .telegam-icon,
.contact-button:hover .call-icon {
  animation: float 1.5s ease-in-out infinite;
}
</style>

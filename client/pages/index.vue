<template>
  <NuxtLayout name="page-layout">
    <Slider />
    <AboutUs />
    <Reasons />
    <New />
    <Services />
    <SeoText
      text="Интернет-магазин Абсолют Холод - официальный дилер климатической техники в Тюмени. 
  Продажа и профессиональная установка кондиционеров Hisense, Ballu, LG. 
  Обслуживание и ремонт сплит-систем во всех районах: Центральный, Восточный, Калининский."
    />
  </NuxtLayout>
</template>

<script setup>
import Slider from "~/components/Slider.vue";
import AboutUs from "~/components/sections/AboutUs.vue";
import Reasons from "~/components/sections/Reasons.vue";
import New from "~/components/sections/New.vue";
import Services from "~/components/sections/Services.vue";
import SeoText from "~/components/common/SeoText.vue";

useSeoMeta({
  title:
    "Купить кондиционер в Тюмени с установкой | Продажа и установка сплит-систем | Абсолют Холод",
  description:
    "Продажа и профессиональный монтаж кондиционеров в Тюмени. Широкий выбор моделей с гарантией. Установка под ключ по низкой цене. Акции и скидки!",
  keywords:
    "купить кондиционер Тюмень, монтаж кондиционеров Тюмень, установка сплит систем, обслуживание кондиционеров, цены на кондиционеры, магазин климатической техники",
  ogTitle: "Абсолют Холод - официальный дилер кондиционеров в Тюмени",
  ogDescription:
    "Бесплатная доставка. ⏱ Монтаж за 3 часа.Гарантия на оборудование и работы. Выгодные цены от производителей",
  ogUrl: "https://абсолютхолод.рф",
  ogImage: "https://абсолютхолод.рф/images/og.jpg",
});

useHead({
  link: [{ rel: "canonical", href: "https://абсолютхолод.рф/" }],
  script: [
    {
      type: "application/ld+json",
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        name: "Абсолют Холод",
        image: [
          "https://абсолютхолод.рф/images/logo.jpg",
          "https://абсолютхолод.рф/images/showroom.jpg",
        ],
        priceRange: "₽₽-₽₽₽",
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
        telephone: "+7(912)430-33-33",
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

<style lang="scss" scoped></style>

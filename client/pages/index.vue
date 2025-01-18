<template>
  <NuxtLayout name="page-layout">
    <div class="flex justify-center mb-10">
      <div
        class="relative w-[100%] h-[500px] shadow-[0px_5px_10px_-5px_rgba(34,60,80,0.6)]"
      >
        <div class="w-full h-full bg-[url('/slider-1.png')] bg-cover"></div>

        <div class="absolute inset-0 w-full h-full pointer-events-none">
          <div
            class="absolute top-0 left-0 w-[20%] h-full bg-gradient-to-r from-white/30 to-transparent backdrop-blur-sm"
          ></div>
          <div
            class="absolute top-0 right-0 w-[20%] h-full bg-gradient-to-l from-white/30 to-transparent backdrop-blur-sm"
          ></div>
        </div>
      </div>
    </div>

    <div name="about-us" class="flex border-t-4 border-[var(--blue)] pt-5">
      <div>
        <h1 class="text-3xl font-bold">
          <span class="text-[var(--blue)]">Сибирский холод</span> – ваш надежный
          партнер в мире комфорта и прохлады!
        </h1>
        <h2>
          Мы специализируемся на продаже, установке и обслуживании кондиционеров
          для дома, офиса и коммерческих помещений. Наша миссия – создать для
          вас комфортные климатические условия в любое время года.
        </h2>
      </div>
      <img class="size-[200px]" src="public/aboutus.png" alt="about" />
    </div>

    <div name="reasons">
      <h1
        class="text-[var(--blue)] text-3xl font-bold border-[var(--blue)] border-b-4 mb-5"
      >
        Почему выбирают нас?
      </h1>
      <div>
        <div class="reasons-grid grid-cols-2 grid gap-3">
          <div
            class="reason-item flex flex-col items-center w-[60%] mx-auto"
            v-for="reason in reasons"
            :key="reason.title"
          >
            <Icon :name="reason.icon" class="size-[64px] text-[var(--blue)]" />
            <p class="title text-xl font-bold text-[var(--blue)]">
              {{ reason.title }}
            </p>
            <p class="description text-center">
              {{ reason.description }}
            </p>
          </div>
        </div>

        <div class="reasons-contant w-[80%] mx-auto mt-7">
          <p
            class="desc flex text-center title text-xl font-bold text-[var(--blue)] opacity-80"
          >
            С нами ваш комфорт – в надежных руках! <br />
            Свяжитесь с нами сегодня, и мы подберем для вас идеальное
            климатическое оборудование.
          </p>
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
import UButton from "~/components/UI/UButton.vue";

const reasons = [
  {
    icon: "solar:shop-minimalistic-outline",
    title: "Широкий ассортимент",
    description:
      "В наличии кондиционеры ведущих брендов под любые задачи и бюджет.",
  },
  {
    icon: "material-symbols:manage-accounts-outline",
    title: "Профессиональная установка",
    description:
      "Сертифицированные специалисты обеспечат качественный монтаж и настройку оборудования.",
  },
  {
    icon: "material-symbols:docs-outline",
    title: "Гарантия и сервис",
    description:
      "Предоставляем гарантию на все работы и предлагаем услуги регулярного обслуживания.",
  },
  {
    icon: "fa6-regular:handshake",
    title: "Индивидуальный подход",
    description:
      "Помогаем выбрать оптимальное решение, учитывая ваши пожелания и особенности помещения.",
  },
];
</script>

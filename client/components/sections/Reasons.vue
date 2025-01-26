<template>
  <Section class="reasons" label="Почему выбирают нас?">
    <div>
      <div class="reasons-grid">
        <div class="reason-item" v-for="reason in reasons" :key="reason.title">
          <Icon :name="reason.icon" class="reason-icon" />
          <p class="reason-title">
            {{ reason.title }}
          </p>
          <p class="reason-description">
            {{ reason.description }}
          </p>
        </div>
      </div>

      <div class="reasons-content">
        <p class="reasons-desc">
          С нами ваш комфорт – в надежных руках! <br />
          Свяжитесь с нами сегодня, и мы подберем для вас идеальное
          климатическое оборудование.
        </p>
      </div>
    </div>
  </Section>
</template>

<script setup lang="ts">
import Section from "./Section.vue";

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

<style lang="scss" scoped>
.reasons {
  .reasons-grid {
    @apply grid gap-3 grid-cols-2;

    .reason-item {
      @apply flex flex-col items-center w-[60%] mx-auto;

      .reason-icon {
        @apply size-[64px] text-[var(--blue)];
      }

      .reason-title {
        @apply text-xl font-bold text-[var(--blue)];
      }

      .reason-description {
        @apply text-center;
      }
    }
  }

  .reasons-content {
    @apply w-[80%] mx-auto mt-12;

    .reasons-desc {
      @apply text-center text-xl font-bold text-[var(--blue)] opacity-80;
    }
  }
}
</style>

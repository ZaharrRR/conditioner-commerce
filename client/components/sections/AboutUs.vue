<template>
  <Section>
    <div class="about-us">
      <div>
        <h1 class="about-us-title">
          <span class="blue-text">Сибирский холод</span> – ваш надежный партнер
          в мире комфорта и прохлады!
        </h1>
        <h2 class="about-us-description">
          Мы специализируемся на продаже, установке и обслуживании кондиционеров
          для дома, офиса и коммерческих помещений. Наша миссия – создать для
          вас комфортные климатические условия в любое время года.
        </h2>
      </div>

      <NuxtImg class="about-us-image" src="/aboutus.png" alt="about" />
    </div>
  </Section>
</template>

<script setup lang="ts">
import Section from "./Section.vue";
</script>

<style lang="scss" scoped>
.about-us {
  @apply flex gap-6;

  .about-us-title {
    @apply text-4xl font-bold;

    .blue-text {
      @apply text-[var(--blue)];
    }
  }

  .about-us-description {
    @apply font-light text-xl w-[80%] mt-2;
  }

  .about-us-image {
    @apply size-[270px];
  }
}
</style>

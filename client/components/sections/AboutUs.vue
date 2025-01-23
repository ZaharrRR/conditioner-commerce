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

      <img class="about-us-image" src="public/aboutus.png" alt="about" />
    </div>
  </Section>
</template>

<script setup lang="ts">
import Section from "./Section.vue";
</script>

<style lang="scss" scoped>
.about-us {
  @apply flex;

  .about-us-title {
    @apply text-3xl font-bold;

    .blue-text {
      @apply text-[var(--blue)];
    }
  }

  .about-us-description {
    @apply text-base;
  }

  .about-us-image {
    @apply size-[200px];
  }
}
</style>

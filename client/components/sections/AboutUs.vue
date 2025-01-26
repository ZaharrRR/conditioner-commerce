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

      <NuxtImg class="about-us-image" src="/images/aboutus.png" alt="about" />
    </div>
  </Section>
</template>

<script setup lang="ts">
import Section from "./Section.vue";
</script>

<style lang="scss" scoped>
.about-us {
  display: flex;
  gap: 24px;
  align-items: center;

  .about-us-title {
    font-size: 36px;
    font-weight: bold;
    animation: fadeIn 1s ease-in-out;

    .blue-text {
      color: var(--blue);
    }
  }

  .about-us-description {
    font-weight: 300;
    font-size: 20px;
    width: 80%;
    margin-top: 8px;
    animation: fadeIn 1.5s ease-in-out;
  }

  .about-us-image {
    width: 270px;
    height: 270px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    animation: slideInRight 1s ease-in-out;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
  }
  to {
    transform: translateX(0);
  }
}
</style>

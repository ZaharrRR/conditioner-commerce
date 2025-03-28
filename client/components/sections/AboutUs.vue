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

<script setup>
import Section from "./Section.vue";
</script>

<style lang="scss" scoped>
.about-us {
  display: flex;
  gap: 24px;
  align-items: center;
  flex-direction: row;

  @media (max-width: 720px) {
    flex-direction: column;
    text-align: center;
    gap: 20px;

    .about-us-title {
      font-size: 28px;
      line-height: 1.3;
    }

    .about-us-description {
      font-size: 18px;
      width: 100%;
      margin: 12px auto 0;
    }

    .about-us-image {
      width: 200px;
      height: 200px;
      order: -1; // Переносим изображение наверх
    }
  }

  @media (max-width: 360px) {
    gap: 16px;
    padding: 0 12px;

    .about-us-title {
      font-size: 24px;
      br {
        display: none;
      } // Убираем перенос строки если есть
    }

    .about-us-description {
      font-size: 16px;
      line-height: 1.4;
    }

    .about-us-image {
      width: 180px;
      height: 180px;
    }
  }

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

// Анимации остаются без изменений
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

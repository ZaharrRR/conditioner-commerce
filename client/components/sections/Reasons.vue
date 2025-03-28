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

<script setup>
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
    display: grid;
    gap: 24px;
    grid-template-columns: repeat(2, 1fr);

    @media (max-width: 720px) {
      gap: 16px;
      grid-template-columns: 1fr; // Переключаем на одну колонку

      .reason-item {
        padding: 32px 12px; // Уменьшаем внутренние отступы
        margin: 0 8px; // Добавляем боковые отступы

        .reason-icon {
          width: 56px; // Уменьшаем размер иконок
          height: 56px;
        }

        .reason-title {
          font-size: 18px; // Корректируем размер шрифта
        }

        .reason-description {
          font-size: 15px;
        }
      }
    }

    @media (max-width: 480px) {
      gap: 12px;

      .reason-item {
        padding: 24px 10px;

        .reason-icon {
          width: 48px;
          height: 48px;
        }

        .reason-title {
          font-size: 16px;
          margin-top: 6px;
        }

        .reason-description {
          font-size: 14px;
          line-height: 1.4; // Улучшаем читаемость
        }
      }
    }

    .reason-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      padding: 48px 16px;
      background-color: white;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease;

      &:hover {
        transform: translateY(-10px);
      }

      .reason-icon {
        width: 64px;
        height: 64px;
        color: var(--blue);
        animation: fadeIn 1s ease-in-out;
      }

      .reason-title {
        font-size: 20px;
        font-weight: bold;
        color: var(--blue);
        margin-top: 8px;
      }

      .reason-description {
        font-size: 16px;
        color: #4a5568;
        margin-top: 8px;
      }
    }
  }

  .reasons-content {
    width: 80%;
    margin: 0 auto;
    margin-top: 48px;

    .reasons-desc {
      text-align: center;
      font-size: 20px;
      font-weight: bold;
      color: var(--blue);
      opacity: 0.8;
    }
  }
}

.reasons-content {
  width: 80%;
  margin: 0 auto;
  margin-top: 48px;

  @media (max-width: 720px) {
    width: 90%;
    margin-top: 32px;

    .reasons-desc {
      font-size: 18px; // Уменьшаем размер текста
      br {
        display: none;
      } // Убираем перенос строки
    }
  }

  @media (max-width: 480px) {
    width: 100%;
    margin-top: 24px;
    padding: 0 8px;

    .reasons-desc {
      font-size: 16px;
      line-height: 1.3;
    }
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
</style>

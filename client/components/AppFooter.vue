<template>
  <footer class="footer">
    <div class="footer-top">
      <img src="/logo.svg" alt="Логотип" class="footer-logo" loading="lazy" />

      <div class="footer-block">
        <p class="footer-title">Контакты</p>
        <p class="footer-text">603890, Россия, Тюмень, улица Пушкина, 52</p>
        <p class="footer-title">+7 (999) 999-99-99</p>
        <p class="footer-text">sibirskyholod@mail.com</p>
        <p class="footer-text">Режим работы: ежедневно c 8:00 до 19:00</p>
      </div>

      <div class="footer-block" v-for="item in links" :key="item.title">
        <p class="footer-title">{{ item.title }}</p>

        <p class="footer-link" v-for="el in item.links" :key="el.label">
          {{ el.label }}
        </p>
      </div>
    </div>

    <div class="footer-bottom">
      <span class="footer-bottom-text">© 2025 ООО “СИБирский хохол”</span>
      <span class="footer-bottom-text">Политика конфиденциальности</span>
      <span class="footer-bottom-text">Условия пользования</span>
    </div>
  </footer>
</template>

<script lang="ts" setup>
const links = [
  {
    title: "Продукция",
    links: [
      {
        label: "Кондиционеры",
        link: "/",
      },
      {
        label: "Сплит-системы",
        link: "/",
      },
      {
        label: "Холодильное оборудование",
        link: "/",
      },
      {
        label: "Вентиляционное оборудование",
        link: "/",
      },
    ],
  },
  {
    title: "Услуги",
    links: [
      {
        label: "Монтаж и сервис",
        link: "/",
      },
      {
        label: "Обслуживание",
        link: "/",
      },
      {
        label: "Чето еще хз",
        link: "/",
      },
      {
        label: "Чето еще хз 2",
        link: "/",
      },
    ],
  },
  {
    title: "Для клиентов",
    links: [
      {
        label: "О нас",
        link: "/",
      },
      {
        label: "Доставка и оплата",
        link: "/",
      },
      {
        label: "Обратная связь",
        link: "/",
      },
      {
        label: "Вопросы и ответы",
        link: "/",
      },
    ],
  },
];
</script>

<style lang="scss" scoped>
.footer {
  @apply bg-[var(--blue)];

  .footer-top {
    @apply py-4 px-7 flex items-center justify-evenly text-white;

    .footer-logo {
      @apply w-auto h-auto; // Настройте размер логотипа по необходимости
    }

    .footer-block {
      @apply flex flex-col;

      .footer-title {
        @apply font-bold;
      }

      .footer-text,
      .footer-link {
        @apply text-xs;
      }

      .footer-link {
        @apply cursor-pointer hover:underline; // Добавьте стили для ссылок
      }
    }
  }

  .footer-bottom {
    @apply p-6 flex items-center justify-between text-white bg-[var(--blue-dark)];

    .footer-bottom-text {
      @apply text-sm;
    }
  }
}
</style>

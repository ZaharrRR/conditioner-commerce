<template>
  <footer class="footer">
    <div class="footer-top">
      <NuxtImg
        src="/logo.svg"
        alt="Логотип компании Сибирский холод"
        class="footer-logo"
        loading="lazy"
      />

      <div class="footer-block">
        <h3 class="footer-title">Контакты</h3>
        <p class="footer-text">603890, Россия, Тюмень, улица Пушкина, 52</p>
        <p class="footer-text">
          Телефон:
          <a href="tel:+79999999999" class="footer-link">+7 (999) 999-99-99</a>
        </p>
        <p class="footer-text">
          Email:
          <a href="mailto:sibirskyholod@mail.com" class="footer-link"
            >sibirskyholod@mail.com</a
          >
        </p>
        <p class="footer-text">Режим работы: ежедневно c 8:00 до 19:00</p>
      </div>

      <div class="footer-block" v-for="item in links" :key="item.title">
        <h3 class="footer-title">{{ item.title }}</h3>
        <a
          class="footer-link"
          v-for="el in item.links"
          :key="el.label"
          :href="el.link"
          :aria-label="el.label"
        >
          {{ el.label }}
        </a>
      </div>
    </div>

    <div class="footer-bottom">
      <span class="footer-bottom-text">© 2025 ООО “СИБирский холод”</span>
      <a class="footer-bottom-text" href="/privacy-policy"
        >Политика конфиденциальности</a
      >
      <a class="footer-bottom-text" href="/terms-of-use">Условия пользования</a>
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
  background-color: var(--blue);
  box-shadow: 0 -4px 6px rgba(0, 0, 0, 0.1);

  .footer-top {
    padding: 32px 24px;
    display: flex;
    align-items: flex-start;
    justify-content: space-evenly;
    color: white;

    .footer-logo {
      width: auto;
      height: 80px;
    }

    .footer-block {
      display: flex;
      flex-direction: column;
      gap: 8px;

      .footer-title {
        font-weight: bold;
        margin-bottom: 8px;
      }

      .footer-text,
      .footer-link {
        font-size: 14px;
      }

      .footer-link {
        cursor: pointer;
        transition: color 0.3s ease;

        &:hover {
          color: var(--blue-light);
          text-decoration: underline;
        }
      }
    }
  }

  .footer-bottom {
    padding: 16px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: white;
    background-color: var(--blue-dark);

    .footer-bottom-text {
      font-size: 14px;
      transition: color 0.3s ease;

      &:hover {
        color: var(--blue-light);
      }
    }
  }
}
</style>

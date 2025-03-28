<template>
  <footer class="footer">
    <div class="footer-top">
      <NuxtImg
        src="/logo.svg"
        alt="Логотип компании Абсолют холод"
        class="footer-logo"
        loading="lazy"
      />

      <div class="footer-block">
        <h3 class="footer-title">Контакты</h3>
        <p class="footer-text">
          625042, Россия, Тюмень, улица Федюнинского 60к1
        </p>
        <p class="footer-text">
          Телефон:
          <a href="tel:89124303333" class="footer-link">+7 (912) 243-33-33</a>
        </p>
        <p class="footer-text">Режим работы: ежедневно c 8:00 до 20:00</p>
      </div>

      <div class="footer-block" v-for="item in links" :key="item.title">
        <h3 class="footer-title">{{ item.title }}</h3>
        <RouterLink
          class="footer-link"
          v-for="el in item.links"
          :key="el.label"
          :to="el.link"
          :aria-label="el.label"
        >
          {{ el.label }}
        </RouterLink>
      </div>
    </div>

    <div class="footer-bottom">
      <span class="footer-bottom-text">© 2025 ООО «Абсолют холод»</span>
      <a class="footer-bottom-text" href="/privacy-policy">
        Политика конфиденциальности
      </a>
      <a class="footer-bottom-text" href="/terms-of-use">
        Условия пользования
      </a>
    </div>
  </footer>
</template>

<script setup>
const links = [
  {
    title: "Продукция",
    links: [
      { label: "Кондиционеры", link: "/products" },
      { label: "Сплит-системы", link: "/products" },
      { label: "Холодильное оборудование", link: "/products" },
      { label: "Вентиляционное оборудование", link: "/products" },
    ],
  },
  {
    title: "Услуги",
    links: [
      { label: "Монтаж и сервис", link: "/services" },
      { label: "Обслуживание", link: "/services" },
      { label: "Ремонт", link: "/services" },
    ],
  },
  {
    title: "Для клиентов",
    links: [
      { label: "О нас", link: "/contacts" },
      { label: "Доставка и оплата", link: "/delivery" },
      { label: "Обратная связь", link: "/contacts" },
      { label: "Вопросы и ответы", link: "/contacts" },
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
      width: 300px;
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

  @media (max-width: 720px) {
    .footer-top {
      flex-direction: column;
      align-items: center;
      padding: 24px 16px;
      gap: 32px;

      .footer-logo {
        height: 60px;
      }

      .footer-block {
        text-align: center;
        width: 100%;
        max-width: 280px;

        .footer-title {
          font-size: 18px;
        }
      }
    }

    .footer-bottom {
      flex-wrap: wrap;
      gap: 12px;
      justify-content: center;
      padding: 12px 16px;
      text-align: center;

      .footer-bottom-text {
        font-size: 13px;
        flex: 1 1 45%;
      }
    }
  }

  @media (max-width: 470px) {
    /* адаптация для экранов 470px */
    .footer-top {
      padding: 20px 12px;
      gap: 24px;

      .footer-logo {
        height: 50px;
      }

      .footer-block {
        .footer-text,
        .footer-link {
          font-size: 13px;
        }
      }
    }

    .footer-bottom {
      flex-direction: column;
      gap: 8px;
      padding: 12px 8px;

      .footer-bottom-text {
        font-size: 12px;
        width: 100%;
        text-align: center;
      }
    }
  }
}
</style>

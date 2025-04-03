<template>
  <footer class="footer">
    <div class="footer-top">
      <NuxtImg
        src="/logo.svg"
        alt="Логотип компании Абсолют холод"
        class="footer-logo"
        loading="lazy"
      />

      <div class="footer-blocks">
        <div class="footer-block">
          <h3 class="footer-title">Контакты</h3>
          <p class="footer-text">
            625042, Россия, Тюмень, <br />
            улица Федюнинского 60к1
          </p>
          <p class="footer-text">
            Телефон:
            <a href="tel:89124303333" class="footer-link">+7 (912) 243-33-33</a>
          </p>
          <p class="footer-text">
            Режим работы: <br />
            ежедневно c 8:00 до 20:00
          </p>
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
    </div>

    <div class="footer-bottom">
      <span class="footer-bottom-text">© 2025 ООО «Абсолют холод»</span>
      <a class="footer-bottom-text" href="/privacy-policy">
        Политика конфиденциальности
      </a>
    </div>
  </footer>
</template>

<script setup>
const links = [
  {
    title: "Продукция",
    links: [
      { label: "Сплит-системы", link: "/products" },
      { label: "Холодильное оборудование", link: "/products" },
      { label: "Вентиляционное оборудование", link: "/products" },
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
    flex-direction: row;
    gap: 24px;
    align-items: center;
    width: fit-content;
    margin: 0 auto;

    .footer-logo {
      width: fit-content;
      max-width: 300px;
      height: 80px;
      margin-bottom: 32px;
    }

    .footer-blocks {
      color: white;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 32px;
      width: fit-content;
      max-width: 1280px;

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

  @media (max-width: 1280px) {
    .footer-top {
      width: 100%;
      flex-direction: column;
      gap: 0;
    }

    .footer-logo {
      width: 100%;
    }

    .footer-blocks {
      width: 100%;
    }
  }

  @media (max-width: 720px) {
    .footer-top {
      padding: 24px 16px;

      .footer-logo {
        height: 60px;
      }
      .footer-blocks {
        text-align: center;
        grid-template-columns: 1fr;
        gap: 32px;
      }

      .footer-block {
        max-width: 280px;
        width: 100%;
        margin: 0 auto;

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

  @media (max-width: 480px) {
    .footer-top {
      padding: 20px 12px;

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

<template>
  <header class="header">
    <div class="header-container">
      <NuxtLink to="/">
        <img src="/logo.svg" alt="Логотип" class="header-logo" loading="lazy" />
      </NuxtLink>
      <HeaderSearch />
    </div>
    <div class="nav-container">
      <nav class="nav-links">
        <NuxtLink to="/products" class="nav-link">Товары</NuxtLink>
        <NuxtLink to="/services" class="nav-link">Услуги</NuxtLink>
        <NuxtLink to="/delivery" class="nav-link">Доставка</NuxtLink>
        <NuxtLink to="/contacts" class="nav-link">Контакты</NuxtLink>
      </nav>
    </div>
  </header>
</template>

<script setup>
import HeaderSearch from "@/components/HeaderSearch.vue";
</script>

<style lang="scss" scoped>
.header {
  background-color: var(--blue-dark);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);

  .header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1280px;
    width: 100%;
    padding: 8px 16px;
    margin: 0 auto;

    .header-logo {
      width: auto;
      height: auto;
    }
  }

  .nav-container {
    background-color: var(--blue);
    color: white;

    .nav-links {
      display: flex;
      gap: 20px;
      padding: 8px 24px;
      width: fit-content;
      margin: 0 auto;
      flex-wrap: wrap;
      justify-content: center;
      padding: 8px 16px;
      gap: 12px;

      .nav-link {
        color: white;
        font-weight: 600;
        width: 120px;
        display: flex;
        justify-content: center;
        background-color: var(--blue-dark);
        text-decoration: none;
        padding: 8px 16px;
        border-radius: 10px;
        transition: background-color 0.3s ease, color 0.3s ease;

        &:hover {
          background-color: var(--blue-light);
          color: white;
        }
      }
    }
  }

  @media (max-width: 720px) {
    .header-container {
      padding: 8px 12px;

      .header-logo {
        max-height: 40px; // Уменьшаем размер логотипа
      }
    }

    .nav-container .nav-links {
      gap: 8px;
      padding: 8px 12px;

      .nav-link {
        width: auto; // Убираем фиксированную ширину
        padding: 6px 12px;
        font-size: 14px;
        min-width: 90px; // Минимальная ширина для кнопок
      }
    }
  }

  @media (max-width: 480px) {
    .header-container {
      flex-direction: column; // Вертикальное расположение лого и поиска
      gap: 8px;
      padding: 12px 8px;

      .header-logo {
        max-height: 35px;
      }
    }

    .nav-container .nav-links {
      gap: 6px;
      padding: 6px 8px;

      .nav-link {
        font-size: 13px;
        padding: 4px 8px;
        border-radius: 6px;
        min-width: 80px;
      }
    }
  }
}
</style>

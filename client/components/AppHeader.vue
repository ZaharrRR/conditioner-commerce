<template>
  <header class="header">
    <div class="header-container">
      <img src="/logo.svg" alt="Логотип" class="header-logo" loading="lazy" />
      <HeaderSearch />
    </div>
    <div class="nav-container">
      <nav class="nav-links">
        <NuxtLink to="/" class="nav-link">Товары</NuxtLink>
        <NuxtLink to="/" class="nav-link">Услуги</NuxtLink>
        <NuxtLink to="/" class="nav-link">Доставка</NuxtLink>
        <NuxtLink to="/" class="nav-link">Контакты</NuxtLink>
      </nav>
    </div>
  </header>
</template>

<script setup lang="ts">
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
    padding: 8px 24px;
    width: 1280px;
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
      gap: 64px;
      padding: 8px 24px;
      width: fit-content;
      margin: 0 auto;

      .nav-link {
        color: white;
        text-decoration: none;
        padding: 8px 16px;
        border-radius: 4px;
        transition: background-color 0.3s ease, color 0.3s ease;

        &:hover {
          background-color: var(--blue-light);
          color: white;
        }
      }
    }
  }
}
</style>

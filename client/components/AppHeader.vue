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
      gap: 20px;
      padding: 8px 24px;
      width: fit-content;
      margin: 0 auto;

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
}
</style>

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
  @apply bg-[var(--blue-dark)];

  .header-container {
    @apply flex justify-between items-center px-6 py-6 w-[1280px] mx-auto;

    .header-logo {
      @apply w-auto h-auto;
    }
  }

  .nav-container {
    @apply bg-[var(--blue)] text-white;

    .nav-links {
      @apply flex gap-16 px-6 py-2 w-fit mx-auto;

      .nav-link {
        @apply text-white no-underline hover:text-[var(--blue-light)] transition-colors;
      }
    }
  }
}
</style>

<template>
  <header class="bg-[var(--blue-dark)]">
    <div class="flex justify-between items-center px-6 py-6 w-[1280px] mx-auto">
      <img src="public/logo.svg" />
      <div class="bg-white w-[40%] flex justify-between rounded-lg p-1">
        <input
          type="text"
          class="border-none outline-none w-[90%] rounded"
          placeholder="Поиск"
        />
        <button class="bg-[var(--blue)] text-xs text-white rounded p-1">
          <Icon name="simple-line-icons:magnifier" />
        </button>
      </div>
    </div>
    <div class="bg-[var(--blue)] text-white">
      <nav class="flex gap-16 px-6 py-2 w-fit mx-auto">
        <NuxtLink>Товары</NuxtLink>
        <NuxtLink>Услуги</NuxtLink>
        <NuxtLink>Доставка</NuxtLink>
        <NuxtLink>Контакты</NuxtLink>
      </nav>
    </div>
  </header>
</template>

<script setup lang="ts">
import UButton from "~/components/UI/UButton.vue";
</script>

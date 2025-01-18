
<template>
  <header>
    <div class="bg-[var(--blue-dark)] flex justify-between items-center px-4 py-2">
      <img src="public/logo.svg">
      <div class="bg-white w-[40%]  flex justify-between rounded-lg p-1">
        <input type="text" class="border-none outline-none w-[90%] rounded" placeholder="Поиск">
        <button class="bg-[var(--blue)] text-xs text-white rounded p-1"><Icon name="simple-line-icons:magnifier" /></button>
      </div>
      <UButton size="small" color="blue" variant="solid">Заявки</UButton>
    </div>
    <div class="bg-[var(--blue)]">
      <nav class="flex gap-5 p-3">
        <UButton size="small" color="blue-dark" variant="solid">Товары</UButton>
        <UButton size="small" color="blue-dark" variant="solid">Услуги</UButton>
        <UButton size="small" color="blue-dark" variant="solid">Доставка</UButton>
        <UButton size="small" color="blue-dark" variant="solid">Контакты</UButton>
      </nav>
    </div>
  </header>
</template>

<script setup lang="ts">
import UButton from "~/components/UI/UButton.vue";
</script>

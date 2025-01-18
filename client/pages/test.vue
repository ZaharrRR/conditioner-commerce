<template>
  <NuxtLayout name="page-layout">
    <h1>test page</h1>

    <div class="buttons flex gap-3">
      <UButton size="medium" color="blue" variant="solid">Solid Button</UButton>
      <UButton size="small" color="blue-dark" variant="outline"
        >Outline Button</UButton
      >
      <UButton size="small" color="blue-accent" variant="link"
        >Link Button</UButton
      >
      <UButton size="medium" color="blue-lightest" variant="solid" disabled
        >Disabled Button</UButton
      >
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
import UButton from "~/components/UI/UButton.vue";
</script>

<style scoped></style>

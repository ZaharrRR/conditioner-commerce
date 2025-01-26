<template>
  <section class="section" :class="className">
    <h2 class="section__label">{{ label }}</h2>
    <div class="section__content">
      <slot></slot>
    </div>
  </section>
</template>

<script setup lang="ts">
defineProps({
  label: String,
  className: String,
});
</script>

<style lang="scss" scoped>
.section {
  width: 100%;

  &__label {
    font-size: 32px;
    font-weight: bold;
    color: var(--blue);
  }

  &__content {
    padding-top: 36px;
    border-top: 4px solid var(--blue);
  }
}
</style>

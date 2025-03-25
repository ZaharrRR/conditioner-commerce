<template>
  <section class="section" :class="className">
    <h2 class="section__label">{{ label }}</h2>
    <div class="section__content">
      <slot></slot>
    </div>
  </section>
</template>

<script setup>
defineProps({
  label: String,
  className: String,
});
</script>

<style lang="scss" scoped>
.section {
  width: 100%;
  padding: 40px 0;

  &__label {
    font-size: 32px;
    font-weight: bold;
    color: var(--blue);
    text-align: center;
    animation: fadeIn 1s ease-in-out;
  }

  &__content {
    padding-top: 36px;
    border-top: 4px solid var(--blue);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>

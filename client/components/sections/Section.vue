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

    @media (max-width: 720px) {
      font-size: 28px;
      padding: 0 16px;
    }

    @media (max-width: 360px) {
      font-size: 24px;
      line-height: 1.3;
    }
  }

  &__content {
    padding-top: 36px;
    border-top: 4px solid var(--blue);

    @media (max-width: 720px) {
      padding-top: 24px;
    }

    @media (max-width: 360px) {
      padding-top: 16px;
      margin: 0 12px;
    }
  }

  @media (max-width: 720px) {
    padding: 30px 0;
  }

  @media (max-width: 360px) {
    padding: 20px 0;
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

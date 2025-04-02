<template>
  <nav class="breadcrumbs" aria-label="Навигационная цепочка">
    <NuxtLink
      v-for="(item, index) in items"
      :key="index"
      :to="item.path"
      class="breadcrumbs__item"
      :class="{ 'breadcrumbs__item--last': index === items.length - 1 }"
    >
      {{ item.name }}
      <span v-if="index !== items.length - 1" class="breadcrumbs__separator"
        >/</span
      >
    </NuxtLink>
  </nav>
</template>

<script setup>
const props = defineProps({
  items: {
    type: Array,
    required: true,
    validator: (value) => {
      return value.every((item) => "name" in item && "path" in item);
    },
  },
});
</script>

<style lang="scss" scoped>
.breadcrumbs {
  padding: 15px 0;
  font-size: 16px;

  &__item {
    color: var(--blue);
    text-decoration: none;
    transition: opacity 0.3s;

    &:hover {
      opacity: 0.8;
      text-decoration: underline;
    }

    &--last {
      color: #666;
      pointer-events: none;
    }
  }

  &__separator {
    margin: 0 5px;
    color: #999;
  }
}

@media (max-width: 768px) {
  .breadcrumbs {
    font-size: 14px;
    padding: 10px 0;
  }
}
</style>

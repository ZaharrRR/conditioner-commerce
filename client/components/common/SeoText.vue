<template>
  <div class="seo-text" :class="customClass" aria-hidden="true">
    {{ text }}
  </div>
</template>

<script setup>
const props = defineProps({
  text: {
    type: String,
    required: true,
  },
  customClass: {
    type: String,
    default: "",
  },
});
</script>

<style lang="scss" scoped>
.seo-text {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;

  /* Альтернативный вариант скрытия */
  /* left: -9999px; */
  /* top: -9999px; */
}
</style>

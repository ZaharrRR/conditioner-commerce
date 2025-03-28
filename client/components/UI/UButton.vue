<template>
  <button class="button">
    <slot></slot>
  </button>
</template>

<script setup></script>

<style scoped>
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
  background-color: var(--blue);
  color: white;
  padding: 8px 16px;
  font-size: 20px;
}

.button:hover {
  scale: 1.05;
}

.button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>

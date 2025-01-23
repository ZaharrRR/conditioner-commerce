<template>
  <div class="search-bar">
    <input
      type="text"
      class="search-input"
      placeholder="Поиск"
      aria-label="Поиск"
    />
    <button class="search-button" aria-label="Найти">
      <Icon name="simple-line-icons:magnifier" />
    </button>
  </div>
</template>

<style lang="scss" scoped>
.search-bar {
  @apply bg-white w-[40%] flex rounded-lg p-2;

  .search-input {
    @apply border-none outline-none flex-1 px-4;
  }

  .search-button {
    @apply bg-[var(--blue)] flex items-center  font-bold px-1  text-white rounded hover:bg-[var(--blue-dark)];
  }
}
</style>

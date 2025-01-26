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
  background-color: white;
  width: 40%;
  display: flex;
  border-radius: 8px;
  padding: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;

  &:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }

  .search-input {
    border: none;
    outline: none;
    flex: 1;
    padding-left: 16px;
    padding-right: 16px;
    font-size: 16px;
  }

  .search-button {
    background-color: var(--blue);
    display: flex;
    align-items: center;
    font-weight: bold;
    padding: 8px 16px;
    color: white;
    border-radius: 8px;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: var(--blue-dark);
    }
  }
}
</style>

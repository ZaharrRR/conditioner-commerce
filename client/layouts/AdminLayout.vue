<template>
  <div class="layout">
    <h1>Админ панель</h1>

    <nav>
      <RouterLink to="/admin/">Продукты</RouterLink>
      <RouterLink to="/admin/categories">Категории</RouterLink>
      <RouterLink to="/admin/brands">Бренды</RouterLink>
      <RouterLink to="/admin/attributes">Атрибуты</RouterLink>
    </nav>

    <main>
      <slot />
    </main>
  </div>
</template>

<style scoped>
.layout {
  width: 1280px;
  margin: 0 auto;
  min-height: 100vh;
  padding: 24px;
}

main {
  flex: 1;

  margin-top: 32px;
  margin-bottom: 16px;
}

h1 {
  font-size: 24px;
  font-weight: 700;
}

nav {
  display: flex;
  gap: 12px;
  margin-top: 24px;
}
</style>

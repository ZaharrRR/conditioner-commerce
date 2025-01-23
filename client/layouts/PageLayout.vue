<template>
  <div class="layout">
    <AppHeader />

    <main>
      <slot />
    </main>

    <AppFooter />
  </div>
</template>

<style scoped>
main {
  width: 1280px;
  margin: 0 auto;
  padding: 24px;
}
</style>

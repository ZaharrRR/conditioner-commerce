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
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  width: 1280px;
  margin: 0 auto;
  padding: 24px;
  flex: 1;
  background-color: white;
  margin-top: 16px;
  margin-bottom: 16px;
}
</style>

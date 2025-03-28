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
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 24px;
  flex: 1;
  background-color: white;
  margin-top: 16px;
  margin-bottom: 16px;
  box-sizing: border-box;

  @media (max-width: 720px) {
    padding: 16px;
    margin-top: 12px;
    margin-bottom: 12px;
  }

  @media (max-width: 360px) {
    padding: 12px 8px;
    margin-top: 8px;
    margin-bottom: 8px;
  }
}
</style>

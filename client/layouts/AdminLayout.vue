<template>
  <div class="layout" v-if="isApiKeyValid">
    <h1>Админ панель</h1>
    <RouterLink to="/">На главную</RouterLink>

    <nav>
      <RouterLink to="/admin/">Продукты</RouterLink>
      <RouterLink to="/admin/categories">Категории</RouterLink>
      <RouterLink to="/admin/brands">Бренды</RouterLink>
      <RouterLink to="/admin/attributes">Атрибуты</RouterLink>
      <RouterLink to="/admin/services">Услуги</RouterLink>
    </nav>

    <main>
      <slot />
    </main>
  </div>

  <div v-else>
    <AuthModal :is-visible="isModalOpen" @success="handleSuccess" />
  </div>
</template>

<script setup lang="ts">
import AuthModal from "~/components/admin/AuthModal.vue";
import { checkApiKey, getAdminApiKey, setAdminApiKey } from "~/api/http";

const isApiKeyValid = ref(false);
const isModalOpen = ref(false);

const checkLocalApiKey = async () => {
  try {
    // 1. Проверяем ключ в памяти
    const memoryKey = getAdminApiKey();
    if (memoryKey) {
      const response = await checkApiKey(memoryKey);
      if (response.status == 200) {
        isApiKeyValid.value = true;
        return;
      }
    }

    // 2. Если в памяти нет или невалидный, проверяем localStorage
    const storedKey = localStorage.getItem("adminApiKey");
    if (storedKey) {
      const response = await checkApiKey(storedKey);
      if (response.status == 200) {
        setAdminApiKey(storedKey);
        isApiKeyValid.value = true;
        return;
      } else {
        // Удаляем невалидный ключ из хранилища
        localStorage.removeItem("adminApiKey");
      }
    }

    // 3. Если ключ не найден или невалидный
    isApiKeyValid.value = false;
    isModalOpen.value = true;
  } catch (error) {
    console.error("Ошибка при проверке API ключа:", error);
    isApiKeyValid.value = false;
    isModalOpen.value = true;
  }
};

const handleSuccess = () => {
  isApiKeyValid.value = true;
  isModalOpen.value = false;
};

onMounted(() => {
  checkLocalApiKey();
});
</script>

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

nav a {
  padding: 8px 16px;
  border-radius: 4px;
  text-decoration: none;
  color: #333;
  background-color: #f0f0f0;
  transition: all 0.2s;
}

nav a:hover {
  background-color: #e0e0e0;
}

nav a.router-link-active {
  background-color: #4a90e2;
  color: white;
}
</style>

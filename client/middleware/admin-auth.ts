export default defineNuxtRouteMiddleware((to, from) => {
  const authUser = false; // Предположим, что у вас есть хук для получения данных пользователя
  if (!authUser || !authUser.isAdmin) {
    return navigateTo("/login");
  }
});

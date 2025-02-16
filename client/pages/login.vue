<template>
  <div>
    <h1>Вход</h1>
    <form @submit.prevent="login">
      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Пароль" />
      <button type="submit">Войти</button>
    </form>
  </div>
</template>

<script setup>
const email = ref("");
const password = ref("");

const login = async () => {
  const { data } = await useFetch("/api/auth/login", {
    method: "POST",
    body: { email: email.value, password: password.value },
  });
  if (data.value.token) {
    localStorage.setItem("token", data.value.token);
    navigateTo("/admin");
  }
};
</script>

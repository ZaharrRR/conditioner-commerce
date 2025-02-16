<template>
  <div>
    <h1>Управление брендами</h1>
    <form @submit.prevent="createBrand">
      <input v-model="brandName" placeholder="Название бренда" />
      <button type="submit">Создать</button>
    </form>
  </div>
</template>

<script setup>
definePageMeta({
  middleware: "admin-auth",
});

const brandName = ref("");

const createBrand = async () => {
  const { data } = await useFetch("/api/admin/brands", {
    method: "POST",
    body: { name: brandName.value },
  });
  console.log(data.value);
};
</script>

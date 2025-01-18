<template>
  <footer class="bg-[var(--blue)]">
    <div class="top py-4 px-7 flex items-center justify-evenly text-white">
      <img src="/logo.svg" alt="" />

      <div class="block">
        <p class="title">Контакты</p>
        <p class="text">603890, Россия, Тюмень, улица Пушкина, 52</p>

        <p class="title">+7 (999) 999-99-99</p>
        <p class="text">sibirskyholod@mail.com</p>
        <p class="text">Режим работы: ежедневно c 8:00 до 19:00</p>
      </div>

      <div class="block" v-for="item in links" :key="item.title">
        <p class="title">{{ item.title }}</p>

        <p class="link" v-for="el in item.links" :key="el.label">
          {{ el.label }}
        </p>
      </div>
    </div>

    <div
      class="bottom p-6 flex items-center justify-between text-white bg-[var(--blue-dark)]"
    >
      <span class="text-sm">© 2025 ООО “СИБирский хохол”</span>
      <span class="text-sm">Политка конфиденциальности</span>
      <span class="text-sm">Условия пользования</span>
    </div>
  </footer>
</template>

<script lang="ts" setup>
const links = [
  {
    title: "Продукция",
    links: [
      {
        label: "Кондиционеры",
        link: "/",
      },
      {
        label: "Сплит-системы",
        link: "/",
      },
      {
        label: "Холодильное оборудование",
        link: "/",
      },
      {
        label: "Вентиляционное оборудование",
        link: "/",
      },
    ],
  },
  {
    title: "Услуги",
    links: [
      {
        label: "Монтаж и сервис",
        link: "/",
      },
      {
        label: "Обслуживание",
        link: "/",
      },
      {
        label: "Чето еще хз",
        link: "/",
      },
      {
        label: "Чето еще хз 2",
        link: "/",
      },
    ],
  },
  {
    title: "Для клиентов",
    links: [
      {
        label: "О нас",
        link: "/",
      },
      {
        label: "Доставка и оплата",
        link: "/",
      },
      {
        label: "Обратная связь",
        link: "/",
      },
      {
        label: "Вопросы и ответы",
        link: "/",
      },
    ],
  },
];
</script>

<style scoped>
.title {
  font-weight: bold;
}

.text,
.link {
  font-size: 10px;
}
</style>

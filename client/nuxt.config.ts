// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devServer: {
    port: 5000,
  },
  nitro: {
    preset: "node-server",
    serveStatic: true,
    port: 5000,
  },
  runtimeConfig: {
    public: {
      host: process.env.HOST,
    },
  },
  app: {
    head: {
      meta: [
        {
          name: "yandex-verification",
          content: "a694d0451ae6f0d3",
        },
      ],
    },
  },

  compatibilityDate: "2024-11-01",
  devtools: { enabled: true },
  modules: ["@pinia/nuxt", "@nuxtjs/tailwindcss", "@nuxt/icon", "@nuxt/image"],
  css: ["~/assets/css/main.css"],
});

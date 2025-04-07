export default defineNuxtPlugin((nuxtApp) => {
  // Инициализация dataLayer
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    dataLayer.push(arguments);
  }

  // Вставка основного скрипта GTM
  (function (w, d, s, l, i) {
    w[l] = w[l] || [];
    w[l].push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
    const f = d.getElementsByTagName(s)[0];
    const j = d.createElement(s);
    const dl = l !== "dataLayer" ? `&l=${l}` : "";
    j.async = true;
    j.src = `https://www.googletagmanager.com/gtm.js?id=${i}${dl}`;
    f.parentNode.insertBefore(j, f);
  })(window, document, "script", "dataLayer", "GTM-P38ZTLTR");

  // Отслеживание переходов между страницами
  const router = useRouter();
  router.afterEach((to) => {
    dataLayer.push({
      event: "pageview",
      pagePath: to.fullPath,
      pageTitle: to.meta.title || document.title,
    });
  });
});

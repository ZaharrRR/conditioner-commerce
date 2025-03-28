<template>
  <NuxtLayout name="page-layout">
    <Slider />
    <AboutUs />
    <Reasons />
    <New />
    <Services />
  </NuxtLayout>
</template>

<script setup>
import Slider from "~/components/Slider.vue";
import AboutUs from "~/components/sections/AboutUs.vue";
import Reasons from "~/components/sections/Reasons.vue";
import New from "~/components/sections/New.vue";
import Services from "~/components/sections/Services.vue";
</script>

<style lang="scss" scoped></style>

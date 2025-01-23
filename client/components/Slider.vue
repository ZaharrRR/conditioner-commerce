<template>
  <div class="slider-container">
    <div class="slider">
      <div class="slider-image" loading="lazy"></div>
      <div class="slider-overlay">
        <div class="slider-gradient-left"></div>
        <div class="slider-gradient-right"></div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.slider-container {
  @apply flex justify-center mb-10;

  .slider {
    @apply relative w-full h-[500px] shadow-[0px_5px_10px_-5px_rgba(34,60,80,0.6)];

    .slider-image {
      @apply w-full h-full bg-[url('/slider-1.png')] bg-cover;
    }

    .slider-overlay {
      @apply absolute inset-0 w-full h-full pointer-events-none;

      .slider-gradient-left {
        @apply absolute top-0 left-0 w-[20%] h-full bg-gradient-to-r from-white/30 to-transparent backdrop-blur-sm;
      }

      .slider-gradient-right {
        @apply absolute top-0 right-0 w-[20%] h-full bg-gradient-to-l from-white/30 to-transparent backdrop-blur-sm;
      }
    }
  }
}
</style>

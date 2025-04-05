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
  display: flex;
  justify-content: center;
  margin-bottom: 40px;

  .slider {
    position: relative;
    width: 100%;
    height: 500px;
    box-shadow: 0px 5px 10px -5px rgba(34, 60, 80, 0.6);
    overflow: hidden;

    .slider-image {
      width: 100%;
      height: 100%;
      background-image: url("/images/slider-1.png");
      background-size: cover;
      animation: fadeIn 1s ease-in-out;
    }

    .slider-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;

      .slider-gradient-left {
        position: absolute;
        top: 0;
        left: 0;
        width: 20%;
        height: 100%;
        background: linear-gradient(
          to right,
          rgba(255, 255, 255, 0.5),
          transparent
        );
        backdrop-filter: blur(4px);
        animation: slideInLeft 1s ease-in-out;
      }

      .slider-gradient-right {
        position: absolute;
        top: 0;
        right: 0;
        width: 20%;
        height: 100%;
        background: linear-gradient(
          to left,
          rgba(255, 255, 255, 0.5),
          transparent
        );
        backdrop-filter: blur(4px);
        animation: slideInRight 1s ease-in-out;
      }
    }
  }
}

@media (max-width: 720px) {
  .slider-gradient-right {
    width: 10% !important;
  }

  .slider-gradient-left {
    width: 10% !important;
  }
}

@media (max-width: 480px) {
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideInLeft {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
  }
  to {
    transform: translateX(0);
  }
}
</style>

<template>
  <NuxtLayout name="page-layout">
    <div class="map-container">
      <h1>
        <Icon
          name="material-symbols:location-on-outline"
          class="geo-icon"
        ></Icon
        >Наш офис и магазин
      </h1>
      <div style="position: relative; overflow: hidden">
        <a
          href="https://yandex.ru/maps/55/tyumen/?utm_medium=mapframe&utm_source=maps"
          style="color: #eee; font-size: 12px; position: absolute; top: 0px"
          >Тюмень</a
        ><a
          href="https://yandex.ru/maps/55/tyumen/?ll=65.547998%2C57.159990&utm_medium=mapframe&utm_source=maps&z=14"
          style="color: #eee; font-size: 12px; position: absolute; top: 14px"
          >Яндекс Карты — транспорт, навигация, поиск мест</a
        ><iframe
          src="https://yandex.ru/map-widget/v1/?ll=65.547998%2C57.159990&z=14"
          width="560"
          height="400"
          frameborder="1"
          allowfullscreen="true"
          style="position: relative"
        ></iframe>
      </div>
      <p>
        <Icon
          name="material-symbols:nest-clock-farsight-analog-outline-rounded"
          class="time-icon"
        ></Icon
        >Режим работы: ежедневно c 8:00 до 19:00
      </p>
      <p>
        <Icon
          name="material-symbols:location-on-outline"
          class="locate-icon"
        ></Icon
        >603890, Россия, Тюмень, улица Пушкина, 52
      </p>
    </div>
    <div class="contacts-container">
      <h1>
        <Icon
          name="material-symbols:call-outline-rounded"
          class="phone-icon"
        ></Icon
        >Контакты
      </h1>
      <p>
        Мы всегда на связи и готовы помочь вам выбрать, купить и установить
        кондиционер!<br />Свяжитесь с нами удобным способом.
      </p>
      <div class="contact-buttons">
        <div class="contact-button">
          <Icon name="mdi:telegram" class="telegam-icon"></Icon>
          <UButton>Написать</UButton>
        </div>
        <div class="contact-button">
          <Icon name="material-symbols:phone-in-talk" class="call-icon"></Icon>
          <UButton>Позвонить</UButton>
        </div>
      </div>
    </div>
    <div class="goodbye">
      <h1>
        <Icon
          name="material-symbols:rocket-launch-outline"
          class="rocket-icon"
        ></Icon>
        Ждем вас в нашем офисе или на связи!
      </h1>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
import UButton from "~/components/UI/UButton.vue";
</script>

<style lang="scss" scoped>
.map-container {
  border-bottom: 5px solid var(--blue);
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;
  padding: 40px 0;

  .time-icon,
  .locate-icon,
  .geo-icon {
    color: var(--blue);
    transition: transform 0.3s ease;
  }

  .geo-icon {
    font-size: 40px;
  }

  h1 {
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 20px;
  }

  p {
    margin-bottom: 10px;
    font-size: 18px;
  }

  &:hover {
    .geo-icon,
    .time-icon,
    .locate-icon {
      transform: scale(1.1);
    }
  }
}

.contacts-container {
  border-bottom: 5px solid var(--blue);
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;
  padding: 40px 0;

  .contact-buttons {
    display: flex;
    gap: 24px;
    margin-top: 20px;
  }

  .contact-button {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 16px;
    transition: transform 0.3s ease;

    &:hover {
      transform: translateY(-10px);
    }
  }

  .telegam-icon,
  .call-icon {
    color: var(--blue);
    font-size: 100px;
    transition: color 0.3s ease;
  }

  p {
    width: 60%;
    text-align: center;
    font-size: 18px;
  }

  h1 {
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 20px;
  }

  .phone-icon {
    color: var(--blue);
  }
}

.goodbye {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-top: 16px;
  padding: 40px 0;
  background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);

  h1 {
    font-size: 40px;
    font-weight: 700;
  }

  .rocket-icon {
    color: var(--blue);
    transition: transform 0.3s ease;

    &:hover {
      transform: rotate(45deg);
    }
  }
}

@keyframes float {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0);
  }
}

.contact-button:hover .telegam-icon,
.contact-button:hover .call-icon {
  animation: float 1.5s ease-in-out infinite;
}
</style>

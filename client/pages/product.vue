<template>
  <NuxtLayout name="page-layout">
    <div class="product-box">
      <img src="/images/hisense.png" alt="Hisense AS-24HR4SBADC005" />
      <div class="product-info">
        <h1>Hisense AS-24HR4SBADC005</h1>
        <p>66,890 ₽</p>
        <UButton>Оставить заявку</UButton>

        <div class="product-spec">
          <h2>Характеристики</h2>
          <div class="spec-icons">
            <div class="spec-icon">
              <Icon name="mdi:cube-outline" class="icon" />
              <p>Площадь помещения</p>
              <p>70 м²</p>
            </div>
            <div class="spec-icon">
              <Icon name="ri:snowflake-fill" class="icon" />
              <p>Мощность охлаждения</p>
              <p>7.0 кВт</p>
            </div>
            <div class="spec-icon">
              <Icon name="material-symbols:settings" class="icon" />
              <p>Гарантия</p>
              <p>2 года</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Контент с описанием и характеристиками -->
    <div class="product-content">
      <div class="description">
        <h2>Описание</h2>
        <h3>Сплит-система Hisense AS-24HR4SBA6DC00S</h3>
        <p>
          Серия NEO Classic A оснащена полностью автоматическими жалюзи 4D AUTO
          Air, что даёт возможность регулировать распределение воздуха полностью
          по вашему желанию с помощью пульта дистанционного управления. Ранее
          эта функция была доступна только у моделей бизнес-класса.
        </p>
        <p>
          Полнофункциональный дисплей скрыт за светопрозрачной передней панелью,
          что делает эксплуатацию очень удобной.
        </p>
        <a href="#">Подробнее...</a>
      </div>

      <div class="characteristics">
        <h2>Характеристики</h2>
        <ul>
          <li><strong>Бренд:</strong> Hisense</li>
          <li><strong>Серия:</strong> Neo classic A</li>
          <li><strong>Обслуживаемая площадь, м²:</strong> 70</li>
          <li><strong>Мощность в режиме охлаждения:</strong> 7.0 кВт</li>
          <li><strong>Мощность в режиме обогрева:</strong> 7.2 кВт</li>
          <li><strong>Страна производства:</strong> Китай</li>
        </ul>
        <a href="#">Подробнее...</a>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import UButton from "~/components/UI/UButton.vue";
</script>

<style scoped>
/* Главный блок с продуктом */
.product-box {
  border: solid 5px var(--blue);
  border-radius: 10px;
  padding: 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: white;
}

.product-box img {
  width: 400px;
  height: auto;
  object-fit: contain;
}

.product-info {
  max-width: 50%;
}

.product-info h1 {
  font-size: 36px;
  font-weight: 500;
  margin-bottom: 10px;
}

.product-info p {
  font-size: 30px;
  font-weight: 700;
  color: var(--blue);
  margin-bottom: 15px;
}

/* Секция характеристик */
.product-spec {
  margin-top: 20px;
  background-color: var(--blue);
  border-radius: 10px;
  padding: 5px 10px;
}

.product-spec h2 {
  color: white;
  font-weight: 600;
  font-size: 24px;
  padding-left: 10px;
}

.spec-icons {
  display: flex;
  justify-content: space-around;
}

.spec-icon {
  text-align: center;
  max-width: 100px;
}

.spec-icon p {
  font-size: 18px;
  font-weight: 600;
  color: white;
  line-height: 1;
}

.icon {
  width: 75px;
  height: 75px;
  color: white;
}

/* Контейнер с описанием и характеристиками */
.product-content {
  display: flex;
  justify-content: space-between;
  padding-top: 30px;
}

.description,
.characteristics {
  width: 48%;
}

.description h2,
.characteristics h2 {
  font-size: 22px;
  font-weight: 600;
  border-bottom: 2px solid var(--blue);
  padding-bottom: 5px;
  margin-bottom: 15px;
}

.description p {
  font-size: 14px;
  line-height: 1.5;
  color: #555;
}

.characteristics ul {
  list-style: none;
  padding: 0;
}

.characteristics li {
  font-size: 14px;
  line-height: 1.6;
  color: #333;
  margin-bottom: 5px;
}

.characteristics a,
.description a {
  display: inline-block;
  margin-top: 10px;
  color: #007bff;
  text-decoration: none;
  font-size: 14px;
}

.characteristics a:hover,
.description a:hover {
  text-decoration: underline;
}
</style>

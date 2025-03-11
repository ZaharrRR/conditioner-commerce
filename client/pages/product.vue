<template>
  <NuxtLayout name="page-layout">
    <div class="product-box">
      <img src="/images/hisense.png" alt="" />
      <div class="product-info">
        <h1>Hisense AS-24HR4SBADC005</h1>
        <p>66,890 ₽</p>
        <UButton>Оставить заявку</UButton>
        <div class="product-spec">
          <h1>Характеристики</h1>
          <div class="spec-icons">
            <div class="spec-icon">
              <Icon name="mdi:cube-outline" class="icon" />
              <p>Площадь помещения</p>
            </div>
            <div class="spec-icon">
              <Icon name="ri:snowflake-fill" class="icon" />
              <p>Мощность охлаждения</p>
            </div>
            <div class="spec-icon">
              <Icon name="material-symbols:settings" class="icon" />
              <p>Гарантия</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="product-content">
      <div class="description">
        <h1>Описание</h1>
        <p>
          Серия NEO Classic A оснащена полностью автоматическими жалюзи 4D AUTO
          Air, что дает возможность регулировать распределение воздуха полностью
          по вашему желанию с помощью пульта дистанционного управления. Раньше
          эта функция была доступна только у моделей бизнес класса.
          Полнофункциональный дисплей скрыт за светопрозрачной передней панелью,
          что делает эксплуатацию очень удобной.
        </p>
      </div>
      <div class="specifications">
        <h1>Характеристики</h1>
        <p></p>
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup>
import UButton from "~/components/UI/UButton.vue";
</script>

<style scoped>
.product-box {
  border: solid 5px var(--blue);
  border-radius: 10px;
  padding: 40px;
  display: flex;
  justify-content: space-between;

  img {
    width: 500px;
    height: 450px;
  }

  h1 {
    font-size: 40px;
    font-weight: 500;
  }

  p {
    font-size: 40px;
    font-weight: 700;
    color: var(--blue);
  }

  .product-spec {
    margin-top: 20px;
    background-color: var(--blue);
    border-radius: 10px;
    padding: 0px 10px 0px 10px;

    p {
      font-size: 20px;
      font-weight: 700;
      color: white;
      text-align: center;
    }

    h1 {
      color: white;
      font-weight: 600;
    }

    .spec-icons {
      display: flex;
      justify-content: space-between;
    }

    .spec-icon {
      text-align: center;
    }

    .icon {
      width: 100px;
      height: 100px;
      color: white;
    }
  }
}

.product-content {
  display: flex;
  justify-content: space-between;
  padding-top: 30px;

  h1 {
    font-size: 20px;
    font-weight: 600;
    width: 100px;
    border-bottom: solid 2px var(--blue);
  }
}
</style>

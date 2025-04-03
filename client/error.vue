<template>
  <div>
    <div class="error-page">
      <div class="error-intro">
        <div>
          <h1>Упс! Что-то пошло не так</h1>
          <p class="intro-text">
            Кажется, мы не можем найти нужную вам страницу. Возможно, она была
            удалена или перемещена.
          </p>
        </div>
        <Icon name="material-symbols:error-circle-rounded" class="icon" />
      </div>

      <div class="error-actions">
        <div class="error-card">
          <Icon
            name="mdi:home"
            class="icon"
            aria-label="Иконка главной страницы"
          />
          <h2>Вернуться на главную</h2>
          <p>Перейдите на главную страницу нашего сайта</p>
          <button class="action-button" @click="handleError">На главную</button>
        </div>

        <div class="error-card">
          <Icon name="mdi:email-fast" class="icon" aria-label="Иконка почты" />
          <h2>Написать нам</h2>
          <p>Сообщите о проблеме, и мы поможем</p>
          <button class="action-button" @click="contactSupport">
            Связаться
          </button>
        </div>

        <div class="error-card">
          <Icon name="mdi:history" class="icon" aria-label="Иконка истории" />
          <h2>Попробовать снова</h2>
          <p>Обновите страницу или вернитесь назад</p>
          <button class="action-button" @click="refreshPage">Обновить</button>
        </div>
      </div>

      <div class="error-code">
        <p>Код ошибки: {{ error.statusCode || "500" }}</p>
        <p v-if="error.message">{{ error.message }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  error: Object,
});

const handleError = () => {
  clearError({ redirect: "/" });
};

const refreshPage = () => {
  window.location.reload();
};

const contactSupport = () => {
  window.location.href = "https://t.me/conditioner_comm_bot";
};
</script>

<style lang="scss" scoped>
.error-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;

  .error-intro {
    display: flex;
    gap: 48px;
    align-items: center;
    margin-bottom: 40px;

    h1 {
      font-size: 48px;
      font-weight: 700;
      margin-bottom: 20px;
      color: #6896eb;
    }

    .intro-text {
      font-size: 24px;
      margin-bottom: 40px;
      line-height: 1.6;
    }

    .icon {
      font-size: 300px;
      color: #6896eb;
    }
  }

  .error-actions {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 40px;

    .error-card {
      background-color: #fff;
      border: 4px solid #6896eb;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      text-align: center;

      .icon {
        font-size: 80px;
        color: #6896eb;
        margin-bottom: 15px;
      }

      h2 {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 15px;
      }

      p {
        font-size: 16px;
        margin: 10px 0 20px;
        color: #555;
      }
    }
  }

  .error-code {
    text-align: center;
    padding: 20px;
    background-color: #f8f8f8;
    border-radius: 10px;
    font-size: 18px;
    color: #777;
  }

  .action-button {
    display: block;
    width: 100%;
    max-width: 200px;
    margin: 0 auto;
    padding: 12px;
    background-color: #6896eb;
    color: #fff;
    border: none;
    border-radius: 8px;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: чё#6896eb;
    }
  }
}

@media (max-width: 1280px) {
  .error-page {
    .error-intro {
      h1 {
        font-size: 40px;
      }

      .intro-text {
        font-size: 20px;
      }

      .icon {
        font-size: 250px;
      }
    }

    .error-actions {
      .error-card {
        h2 {
          font-size: 22px;
        }
      }
    }
  }
}

@media (max-width: 720px) {
  .error-page {
    padding: 15px;

    .error-intro {
      flex-direction: column;
      gap: 30px;
      text-align: center;

      h1 {
        font-size: 32px;
      }

      .intro-text {
        font-size: 18px;
        margin-bottom: 30px;
      }

      .icon {
        font-size: 180px;
      }
    }

    .error-actions {
      grid-template-columns: 1fr;
      gap: 15px;

      .error-card {
        padding: 15px;

        .icon {
          font-size: 60px;
        }

        h2 {
          font-size: 20px;
        }

        p {
          font-size: 14px;
        }
      }
    }

    .action-button {
      font-size: 16px;
      padding: 10px;
    }
  }
}

@media (max-width: 480px) {
  .error-page {
    .error-intro {
      h1 {
        font-size: 28px;
      }

      .intro-text {
        font-size: 16px;
      }

      .icon {
        font-size: 120px;
      }
    }

    .error-actions {
      .error-card {
        h2 {
          font-size: 18px;
        }
      }
    }
  }
}
</style>

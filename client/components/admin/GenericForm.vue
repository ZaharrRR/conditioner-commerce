<template>
  <form class="generic-form" @submit.prevent="handleSubmit">
    <transition name="fade-slide" mode="out-in">
      <div v-if="error" key="error" class="error-message">⚠️ {{ error }}</div>
    </transition>

    <div class="form-sections">
      <div
        v-for="(section, index) in formConfig"
        :key="index"
        class="form-section"
      >
        <h2 v-if="section.title" class="section-title">
          {{ section.title }}
        </h2>

        <div class="form-fields">
          <FormField
            v-for="field in section.fields"
            :key="field.key"
            :label="field.label"
            :type="field.type"
            :required="field.required"
            :options="externalData[field.options]"
            v-model="formData[field.key]"
          />
        </div>
      </div>
    </div>

    <div class="form-actions">
      <slot name="actions">
        <button type="submit" class="submit-button">
          <span class="button-text">{{ submitButtonText }}</span>
          <div class="button-overlay"></div>
        </button>
      </slot>
    </div>
  </form>
</template>

<script setup>
import { ref } from "vue";

import FormField from "./FormField.vue";

const props = defineProps({
  formConfig: {
    type: Array,
    required: true,
  },
  formData: {
    type: Object,
    required: true,
  },
  externalData: {
    type: Object,
    default: () => ({}),
  },
  submitHandler: Function,
  submitButtonText: {
    type: String,
    default: "Сохранить",
  },
});

const error = ref(null);

const handleSubmit = async () => {
  try {
    error.value = null;
    if (props.submitHandler) {
      await props.submitHandler(props.formData);
    }
  } catch (err) {
    error.value = err.message || "Произошла ошибка";
  }
};
</script>

<style scoped>
.generic-form {
  background: white;
  padding: 2.5rem;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.error-message {
  background: #fff0f0;
  color: #ff4444;
  padding: 1.2rem;
  border-radius: 12px;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  border: 1px solid #ffdddd;
  font-weight: 500;
}

.form-sections {
  display: grid;
  gap: 2.5rem;
}

.form-section {
  padding: 1.5rem;
  background: #f9fafb;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.form-section:hover {
  transform: translateY(-2px);
}

.section-title {
  font-size: 1.3rem;
  color: #1f2937;
  margin-bottom: 1.8rem;
  position: relative;
  padding-left: 1rem;
}

.section-title::before {
  content: "";
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 70%;
  background: #3b82f6;
  border-radius: 4px;
}

.form-fields {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.8rem;
}

.form-actions {
  margin-top: 3rem;
  display: flex;
  justify-content: flex-end;
}

.submit-button {
  position: relative;
  background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
  color: white;
  padding: 1.1rem 2.4rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  font-weight: 600;
  letter-spacing: 0.5px;
}

.submit-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
}

.button-overlay {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    rgba(255, 255, 255, 0) 20%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0) 80%
  );
  transition: left 0.6s;
}

.submit-button:hover .button-overlay {
  left: 100%;
}

/* Анимации */
.fade-slide-enter-active {
  animation: fadeInUp 0.4s ease-out;
}
.fade-slide-leave-active {
  animation: fadeOutDown 0.3s ease-in;
}

@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeOutDown {
  0% {
    opacity: 1;
    transform: translateY(0);
  }
  100% {
    opacity: 0;
    transform: translateY(10px);
  }
}
</style>

<template>
  <div class="form-group" :class="{ 'has-focus': isFocused }">
    <label v-if="label" class="form-label">
      <span class="label-text">{{ label }}</span>
      <span v-if="required" class="required-asterisk">*</span>
    </label>

    <div class="input-container">
      <input
        v-if="type === 'input' || type === 'number'"
        :type="type === 'number' ? 'number' : 'text'"
        :value="modelValue"
        @input="handleInput"
        @focus="isFocused = true"
        @blur="isFocused = false"
        class="form-control"
        :required="required"
        :step="step"
      />

      <select
        v-else-if="type === 'select'"
        :value="modelValue"
        @change="handleChange"
        @focus="isFocused = true"
        @blur="isFocused = false"
        class="form-control form-select"
        :required="required"
      >
        <option value="" disabled>Выберите опцию</option>
        <option v-for="option in options" :key="option.id" :value="option.id">
          {{ option.name || option.title }}
        </option>
      </select>

      <textarea
        v-else-if="type === 'textarea'"
        :value="modelValue"
        @input="handleInput"
        @focus="isFocused = true"
        @blur="isFocused = false"
        class="form-control"
        :required="required"
        :rows="3"
      ></textarea>

      <input
        v-else-if="type === 'file'"
        type="file"
        @change="handleFileUpload"
        @focus="isFocused = true"
        @blur="isFocused = false"
        class="form-control"
        :required="required"
        accept="image/*"
      />
    </div>
  </div>
</template>

<script setup>
defineProps({
  label: String,
  modelValue: [String, Number],
  type: {
    type: String,
    default: "input",
    validator: (value) =>
      ["input", "select", "textarea", "number", "file"].includes(value),
  },
  required: Boolean,
  step: String,
  options: {
    type: Array,
    default: () => [],
  },
});

const emit = defineEmits(["update:modelValue"]);

const isFocused = ref(false);

const handleInput = (e) => {
  emit("update:modelValue", e.target.value);
};

const handleChange = (e) => {
  emit("update:modelValue", e.target.value);
};

const handleFileUpload = (e) => {
  const file = e.target.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("photo_file", file);

  emit("update:modelValue", file);

  // const reader = new FileReader();
  // reader.onload = (e) => {
  //   const arrayBuffer = e.target.result;
  //   emit("update:modelValue", arrayBuffer);
  // };
  // reader.readAsArrayBuffer(file);
};
</script>

<style scoped>
.form-group {
  position: relative;
  margin-bottom: 1.8rem;
}

.form-label {
  display: block;
  margin-bottom: 0.8rem;
  font-size: 0.95rem;
  color: #374151;
  transition: all 0.3s ease;
}

.label-text {
  transform-origin: left center;
  display: inline-block;
}

.input-container {
  position: relative;
}

.form-control {
  width: 100%;
  padding: 1rem 1.2rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  background: white;
  color: #1f2937;
}

.form-control:focus {
  border-color: #3b82f6;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);
  outline: none;
  padding-left: 1.4rem;
}

.form-control::placeholder {
  color: #9ca3af;
}

.form-select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3csvg...");
  background-position: right 1rem center;
  background-repeat: no-repeat;
  background-size: 1.2em;
  padding-right: 3rem;
}

textarea.form-control {
  min-height: 100px;
  resize: vertical;
  line-height: 1.5;
}

.required-asterisk {
  color: #ef4444;
  margin-left: 0.3rem;
  font-size: 0.9em;
}

/* Анимация лейбла при фокусе */
.has-focus .label-text {
  transform: translateY(-2px);
  color: #3b82f6;
}

input[type="file"] {
  padding: 0.8rem 1.2rem;
  cursor: pointer;
}

input[type="file"]::file-selector-button {
  margin-right: 1rem;
  padding: 0.5rem 1rem;
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s ease;
}

input[type="file"]::file-selector-button:hover {
  background: #e5e7eb;
}

/* Анимация ввода */
@keyframes inputGlow {
  0% {
    box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.3);
  }
  100% {
    box-shadow: 0 0 0 6px rgba(59, 130, 246, 0);
  }
}

.form-control:focus {
  animation: inputGlow 1s ease-out;
}
</style>

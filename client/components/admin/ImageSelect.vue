<template>
  <div class="image-uploader">
    <div class="preview-container">
      <img v-if="previewUrl" :src="previewUrl" class="preview-image" />
      <div v-else class="upload-prompt">Выберите изображение</div>
    </div>

    <div class="controls">
      <input
        type="file"
        ref="fileInput"
        accept="image/*"
        @change="handleFileSelect"
        class="hidden-input"
      />
      <button @click="openFileDialog" class="btn-select">Выбрать файл</button>
      <button
        @click="confirmSelection"
        class="btn-confirm"
        :disabled="!selectedFile"
      >
        Подтвердить
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const emit = defineEmits(["confirm"]);
const fileInput = ref(null);
const selectedFile = ref(null);
const previewUrl = ref("");

const openFileDialog = () => {
  fileInput.value.click();
};

const handleFileSelect = (event) => {
  const file = event.target.files[0];
  if (!file || !file.type.startsWith("image/")) return;

  selectedFile.value = file;
  previewUrl.value = URL.createObjectURL(file);
};

const confirmSelection = async () => {
  if (!selectedFile.value) return;

  const reader = new FileReader();
  reader.onload = (e) => {
    emit("confirm", {
      binary: e.target.result,
      file: selectedFile.value,
      preview: previewUrl.value,
    });
  };
  reader.readAsArrayBuffer(selectedFile.value);
};
</script>

<style scoped>
.image-uploader {
  padding: 1rem;
  max-width: 400px;
}

.preview-container {
  border: 2px dashed #ccc;
  border-radius: 8px;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
  overflow: hidden;
}

.preview-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.upload-prompt {
  color: #666;
  font-size: 0.9rem;
}

.hidden-input {
  display: none;
}

.controls {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn-select,
.btn-confirm {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s;
}

.btn-select {
  background: #3b82f6;
  color: white;
}

.btn-confirm {
  background: #10b981;
  color: white;
}

.btn-confirm:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.btn-select:hover,
.btn-confirm:not(:disabled):hover {
  opacity: 0.9;
}
</style>

<template>
  <div class="image-uploader">
    <h3 v-if="title" class="image-uploader__title">{{ title }}</h3>

    <div class="image-uploader__current" v-if="currentImage">
      <img :src="currentImage" :alt="altText" class="image-uploader__image" />
    </div>

    <div class="image-uploader__controls">
      <input
        type="file"
        ref="fileInput"
        accept="image/*"
        @change="handleFileSelect"
        class="image-uploader__input"
      />
      <button
        type="button"
        @click="triggerFileInput"
        class="image-uploader__button"
      >
        Выбрать файл
      </button>
      <span class="image-uploader__filename">{{
        selectedFile?.name || "Файл не выбран"
      }}</span>
    </div>

    <div class="image-uploader__actions">
      <button
        type="button"
        @click="handleUpload"
        class="image-uploader__upload-btn"
        :disabled="isUploading || !selectedFile"
      >
        {{ uploadButtonText }}
      </button>
    </div>

    <div v-if="error" class="image-uploader__error">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  currentImage: String,
  entityType: {
    type: String,
    required: true,
    validator: (value) => ["product", "brand", "category"].includes(value),
  },
  entityId: {
    type: [String, Number],
    required: true,
  },
  title: String,
  altText: {
    type: String,
    default: "Изображение",
  },
});

const emit = defineEmits(["upload"]);

const selectedFile = ref(null);
const isUploading = ref(false);
const error = ref(null);
const fileInput = ref(null);

const uploadButtonText = computed(() => {
  if (isUploading.value) return "Загрузка...";
  return props.currentImage ? "Обновить изображение" : "Загрузить изображение";
});

const triggerFileInput = () => {
  fileInput.value.click();
};

const handleFileSelect = (event) => {
  const file = event.target.files[0];
  if (!file) return;

  if (!file.type.startsWith("image/")) {
    error.value = "Можно загружать только изображения";
    return;
  }

  selectedFile.value = file;
  error.value = null;
};

const handleUpload = async () => {
  if (!selectedFile.value) {
    error.value = "Выберите файл для загрузки";
    return;
  }

  isUploading.value = true;
  error.value = null;

  try {
    const formData = new FormData();
    formData.append("photo_file", selectedFile.value);
    formData.append("entity_type", props.entityType);
    formData.append("entity_id", props.entityId);
    console.log(formData);

    emit("upload", formData);
  } catch (err) {
    error.value = "Ошибка загрузки: " + (err.message || "");
  } finally {
    isUploading.value = false;
  }
};
</script>

<style scoped>
.image-uploader {
  margin: 2rem 0;
  padding: 1.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
}

.image-uploader__title {
  font-size: 1.1rem;
  margin-bottom: 1rem;
  color: #4a5568;
}

.image-uploader__current {
  margin-bottom: 1.5rem;
}

.image-uploader__image {
  max-width: 300px;
  height: auto;
  border-radius: 0.375rem;
  border: 1px solid #e2e8f0;
}

.image-uploader__controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-bottom: 1rem;
}

.image-uploader__input {
  display: none;
}

.image-uploader__button {
  background: #3b82f6;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background 0.2s;
}

.image-uploader__button:hover {
  background: #2563eb;
}

.image-uploader__filename {
  color: #64748b;
  font-size: 0.875rem;
}

.image-uploader__upload-btn {
  background: #10b981;
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background 0.2s;
}

.image-uploader__upload-btn:hover:not(:disabled) {
  background: #059669;
}

.image-uploader__upload-btn:disabled {
  background: #6ee7b7;
  cursor: not-allowed;
}

.image-uploader__error {
  color: #dc2626;
  margin-top: 1rem;
  padding: 0.5rem;
  background: #fee2e2;
  border-radius: 0.375rem;
}
</style>

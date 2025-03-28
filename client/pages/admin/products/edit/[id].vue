<template>
  <NuxtLayout name="admin-layout" class="product-edit">
    <h1 class="product-edit__title">Управление товаром: {{ productName }}</h1>

    <div v-if="error" class="product-edit__error">{{ error }}</div>

    <form v-else class="product-edit__form" @submit.prevent="submit">
      <!-- Отображение информации о товаре (только для чтения) -->
      <div class="product-edit__info">
        <div class="product-edit__info-item">
          <label>Название:</label>
          <p>{{ form.name }}</p>
        </div>

        <div class="product-edit__info-item">
          <label>Цена:</label>
          <p>{{ form.price }} ₽</p>
        </div>

        <div class="product-edit__info-item">
          <label>Бренд:</label>
          <p>{{ form.brand_name }}</p>
        </div>

        <div class="product-edit__info-item">
          <label>Категория:</label>
          <p>{{ form.category_name }}</p>
        </div>
      </div>

      <!-- Секция атрибутов -->
      <div class="product-edit__attributes">
        <h3 class="product-edit__subtitle">Атрибуты товара</h3>

        <!-- Старые атрибуты (только для чтения) -->
        <div class="product-edit__existing-attributes">
          <h4>Существующие атрибуты:</h4>
          <ul>
            <li v-for="(attr, index) in existingAttributes" :key="index">
              {{ attr.attribute_name }}: {{ attr.value }}
            </li>
          </ul>
        </div>

        <!-- Новые атрибуты (форма добавления) -->
        <div class="product-edit__new-attributes">
          <h4>Добавить новые атрибуты:</h4>
          <div
            v-for="(attribute, index) in form.newAttributes"
            :key="'new-' + index"
            class="product-edit__attribute-group"
          >
            <select
              v-model="attribute.attribute_id"
              class="product-edit__select"
              required
            >
              <option value="">Выберите атрибут</option>
              <option
                v-for="attr in availableAttributes"
                :key="attr.id"
                :value="attr.id"
              >
                {{ attr.name }}
              </option>
            </select>

            <input
              v-model="attribute.value"
              class="product-edit__input"
              placeholder="Значение атрибута"
              required
            />

            <button
              type="button"
              class="product-edit__remove-btn"
              @click="removeAttributeField(index)"
            >
              ×
            </button>
          </div>

          <button
            type="button"
            class="product-edit__add-btn"
            @click="addAttributeField"
          >
            Добавить атрибут
          </button>
        </div>
      </div>

      <!-- Секция изображений -->
      <div class="product-edit__images">
        <h3 class="product-edit__subtitle">Фотография товара</h3>

        <!-- Поле загрузки файла -->
        <div class="product-edit__file-input">
          <input
            type="file"
            @change="handleFileUpload"
            accept="image/*"
            name="photo_file"
            class="product-edit__file-input"
          />
          <button
            type="button"
            @click="uploadPhoto"
            class="product-edit__upload-btn"
            :disabled="isUploading"
          >
            {{ isUploading ? "Загрузка..." : "Обновить фото" }}
          </button>
        </div>

        <!-- Отображение текущего изображения -->
        <div class="product-edit__image-list" v-if="existingImages">
          <div class="product-edit__image-item">
            <img
              :src="existingImages"
              alt="Изображение товара"
              class="product-edit__image"
            />
          </div>
        </div>
        <div v-else>Изображение отсутствует</div>
      </div>

      <button type="submit" class="product-edit__submit-btn">
        Сохранить изменения
      </button>
    </form>
    <img :src="existingImages" alt="" />
  </NuxtLayout>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from "vue";
import { useRoute } from "vue-router";
import {
  getProductById,
  linkProductAttributes,
  updateProductPhoto,
} from "@/api/products";
import { fetchAllAttributes } from "@/api/attributes";

const route = useRoute();
const productId = route.params.id;

const selectedFile = ref(null);
const isUploading = ref(false);

const product = ref(null);
const attributes = ref([]);
const existingImages = ref("");
const error = ref(null);

const form = reactive({
  name: "",
  price: "",
  brand_name: "",
  category_name: "",
  newAttributes: [],
});

// Вычисляемые свойства
const existingAttributes = computed(() => {
  return product.value?.attributes || [];
});

const availableAttributes = computed(() => {
  return attributes.value.filter(
    (attr) =>
      !existingAttributes.value.some((ex) => ex.attribute_id === attr.id)
  );
});

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (!file.type.startsWith("image/")) {
    error.value = "Можно загружать только изображения";
    return;
  }
  selectedFile.value = file;
};
const uploadPhoto = async () => {
  if (!selectedFile.value) {
    error.value = "Выберите файл для замены";
    return;
  }

  isUploading.value = true;
  try {
    const formData = new FormData();
    formData.append("photo_file", selectedFile.value);

    console.log(formData);

    // Отправка запроса
    const { imageUrl } = await updateProductPhoto(productId, formData);

    // Обновляем текущее изображение
    existingImages.value = imageUrl;
    selectedFile.value = null;
  } catch (err) {
    error.value = "Ошибка загрузки: " + (err.message || "");
  } finally {
    isUploading.value = false;
  }
};

const loadData = async () => {
  try {
    const [productRes, attributesRes] = await Promise.all([
      getProductById(productId),
      fetchAllAttributes(),
    ]);

    // Сохраняем продукт в отдельной переменной
    product.value = productRes;

    form.name = productRes.name;
    form.price = productRes.price;
    form.brand_name = productRes.brand_name;
    form.category_name = productRes.category_name;
    attributes.value = attributesRes;
    existingImages.value = productRes.image;
  } catch (err) {
    error.value = "Ошибка загрузки данных";
  }
};

const addAttributeField = () => {
  form.newAttributes.push({ attribute_id: "", value: "" });
};

const removeAttributeField = (index) => {
  form.newAttributes.splice(index, 1);
};

const submit = async () => {
  try {
    // Сохраняем атрибуты отдельным запросом
    if (form.newAttributes.length > 0) {
      const attributesToSend = form.newAttributes
        .filter((attr) => attr.attribute_id && attr.value)
        .map((attr) => ({
          attribute_id: attr.attribute_id,
          value: attr.value,
        }));

      await linkProductAttributes(productId, attributesToSend);
    }

    alert("Изменения успешно сохранены!");
    await loadData();
    form.newAttributes = [];
  } catch (err) {
    error.value = err.message || "Ошибка сохранения изменений";
  }
};

onMounted(() => {
  loadData();
});
</script>

<style lang="scss" scoped>
.product-edit {
  &__title {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    text-align: center;
  }

  .product-edit__image-list {
    margin-top: 1rem;
  }

  .product-edit__image-item {
    max-width: 300px;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    overflow: hidden;
  }

  .product-edit__image {
    width: 100%;
    height: auto;
    display: block;
  }

  &__file-input {
    margin: 1rem 0;
    display: flex;
    gap: 1rem;
    align-items: center;

    input[type="file"] {
      padding: 0.5rem;
      border: 1px solid #e2e8f0;
      border-radius: 0.375rem;
    }
  }

  &__upload-btn {
    background: #10b981;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.375rem;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #059669;
    }

    &:disabled {
      background: #6ee7b7;
      cursor: not-allowed;
    }
  }

  &__info {
    background: #f8fafc;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 2rem;

    &-item {
      margin-bottom: 1rem;
      label {
        font-weight: 500;
        color: #64748b;
        margin-right: 0.5rem;
      }
      p {
        margin: 0.5rem 0 0;
        font-size: 1.1rem;
        color: #1e293b;
      }
    }
  }

  &__error {
    color: #dc2626;
    padding: 1rem;
    background: #fee2e2;
    border-radius: 0.375rem;
    margin-bottom: 1rem;
  }

  &__form {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  &__form-group {
    margin-bottom: 1.5rem;
  }

  &__label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
  }

  &__input {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
    font-size: 1rem;

    &:focus {
      border-color: #3b82f6;
      outline: none;
    }
  }

  &__select {
    @extend .product-edit__input;
    appearance: none;
    background: white
      url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e")
      no-repeat right 0.75rem center;
    background-size: 1em;
  }

  &__existing-attributes {
    margin-bottom: 2rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;

    ul {
      list-style: none;
      padding: 0;

      li {
        padding: 0.5rem 0;
        border-bottom: 1px solid #eee;

        &:last-child {
          border-bottom: none;
        }
      }
    }
  }

  &__new-attributes {
    margin-top: 2rem;
  }

  &__attributes {
    margin: 2rem 0;
    padding: 1.5rem;
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
  }

  &__subtitle {
    font-size: 1.1rem;
    margin-bottom: 1rem;
    color: #4a5568;
  }

  &__attribute-group {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    align-items: center;

    select {
      flex: 1;
    }

    input {
      flex: 2;
    }
  }

  &__remove-btn {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #f56565;
    padding: 0 0.5rem;

    &:hover {
      color: #e53e3e;
    }
  }

  &__add-btn {
    background: #e2e8f0;
    color: #4a5568;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.375rem;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #cbd5e0;
    }
  }

  &__images {
    margin: 2rem 0;
    padding: 1.5rem;
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
  }

  &__image-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
  }

  &__image-item {
    position: relative;
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
    overflow: hidden;
  }

  &__image {
    width: 100%;
    height: 150px;
    object-fit: cover;
  }

  &__file-input {
    margin-top: 1rem;
  }

  &__submit-btn {
    background: #3b82f6;
    color: white;
    padding: 0.75rem 1.5rem;
    width: 100%;
    border: none;
    border-radius: 0.375rem;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #2563eb;
    }
  }
}
</style>

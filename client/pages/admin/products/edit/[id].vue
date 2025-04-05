<template>
  <NuxtLayout name="admin-layout" class="product-edit">
    <h1 class="product-edit__title">Управление товаром: {{ productName }}</h1>

    <div v-if="error" class="product-edit__error">{{ error }}</div>

    <form v-else class="product-edit__form" @submit.prevent="submit">
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

        <div class="product-edit__info-item">
          <label>Описание:</label>
          <p>{{ form.description }}</p>
        </div>
      </div>

      <div class="product-edit__attributes">
        <h3 class="product-edit__subtitle">Атрибуты товара</h3>

        <div class="product-edit__existing-attributes">
          <div v-if="existingAttributes.length" class="attributes-list">
            <div
              v-for="(attr, index) in existingAttributes"
              :key="index"
              class="attributes-list__item"
            >
              <div class="attributes-list__info">
                <span class="attributes-list__name">{{
                  attr.attribute_name
                }}</span>
                <span class="attributes-list__value">{{ attr.value }}</span>
              </div>
              <button
                type="button"
                class="attributes-list__remove-btn"
                @click="handleDeleteAttribute(attr.attribute_name)"
              >
                <svg width="12" height="12" viewBox="0 0 14 14" fill="none">
                  <path
                    d="M13 1L1 13M1 1L13 13"
                    stroke="currentColor"
                    stroke-width="2"
                  />
                </svg>
              </button>
            </div>
          </div>
          <div v-else class="attributes-empty">Нет добавленных атрибутов</div>
        </div>

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

        <button
          type="button"
          @click="saveAttrs()"
          class="product-edit__submit-btn"
        >
          Сохранить изменения
        </button>
      </div>

      <div class="product-edit__images">
        <ImageUploader
          :current-image="originalImage"
          :entity-type="'product'"
          :entity-id="productId"
          title="Фотография товара"
          alt-text="Изображение товара"
          @upload="handleImageUpload"
        />
      </div>
    </form>
  </NuxtLayout>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from "vue";

import ImageUploader from "~/components/admin/ImageUploader.vue";

import {
  getProductById,
  linkProductAttributes,
  updateProductPhoto,
  deleteProductAttribut,
} from "@/api/products";
import { fetchAllAttributes } from "@/api/attributes";

import { useRoute } from "vue-router";

const route = useRoute();
const productId = route.params.id;

const product = ref(null);
const attributes = ref([]);
const existingImages = ref("");
const error = ref(null);

const originalImage = ref("");
const updatedImage = ref("");

const form = reactive({
  name: "",
  price: "",
  brand_name: "",
  category_name: "",
  description: "",
  newAttributes: [],
});

const existingAttributes = computed(() => {
  return product.value?.attributes || [];
});

const availableAttributes = computed(() => {
  return attributes.value.filter(
    (attr) =>
      !existingAttributes.value.some((ex) => ex.attribute_id === attr.id)
  );
});

const handleImageUpload = async (formData) => {
  try {
    const response = await updateProductPhoto(productId, formData);

    originalImage.value = response.data.photo_url;
    existingImages.value = response.data.photo_url;
    alert("Изображение успешно загружено!");
  } catch (err) {
    error.value = "Ошибка загрузки изображения: " + (err.message || "");
  }
};

const handleDeleteAttribute = async (attribute_name) => {
  try {
    await deleteProductAttribut(productId, attribute_name);

    if (product.value?.attributes) {
      product.value.attributes = product.value.attributes.filter(
        (attr) => attr.attribute_name !== attribute_name
      );
    }
  } catch (err) {
    error.value = "Ошибка удаления атрибута: " + (err.message || "");
  }
};

const loadData = async () => {
  try {
    const [productRes, attributesRes] = await Promise.all([
      getProductById(productId),
      fetchAllAttributes(),
    ]);

    product.value = productRes;

    originalImage.value = productRes.photo_url;

    form.name = productRes.name;
    form.price = productRes.price;
    form.brand_name = productRes.brand_name;
    form.category_name = productRes.category_name;
    form.description = productRes.description;
    attributes.value = attributesRes;
    existingImages.value = productRes.photo_url;
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

const saveAttrs = async () => {
  try {
    if (form.newAttributes.length > 0) {
      const attributesToSend = form.newAttributes
        .filter((attr) => attr.attribute_id && attr.value)
        .map((attr) => ({
          attribute_id: attr.attribute_id,
          value: attr.value,
        }));

      await linkProductAttributes(productId, attributesToSend);

      form.newAttributes = [];
      await loadData();
    }
  } catch (err) {
    console.log(err);
    alert("Ошибка при сохранении атрибутов");
  }
};

onMounted(() => {
  loadData();
});
</script>

<style lang="scss" scoped>
.product-edit {
  &__title {
    font-size: 1.75rem;
    font-weight: 600;
    color: #1a202c;
    margin-bottom: 2.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #e2e8f0;
  }

  /* Блок с основной информацией */
  &__info {
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    margin-bottom: 2.5rem;
    overflow: hidden;

    &-item {
      padding: 1.25rem 1.5rem;
      border-bottom: 1px solid #f7fafc;
      background: linear-gradient(to right, #f8fafc 0%, #ffffff 10%);

      &:last-child {
        border-bottom: none;
      }

      label {
        display: block;
        font-size: 0.875rem;
        color: #718096;
        margin-bottom: 0.25rem;
        font-weight: 500;
      }

      p {
        font-size: 1.125rem;
        color: #2d3748;
        margin: 0;
        font-weight: 600;
        letter-spacing: -0.025em;
      }
    }
  }

  /* Общие стили для форм и элементов */
  &__form {
    display: grid;
    gap: 2.5rem;
  }

  &__input,
  &__select {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 1rem;
    transition: all 0.2s;

    &:focus {
      border-color: #4299e1;
      box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.2);
      outline: none;
    }
  }

  &__select {
    appearance: none;
    background: white url("data:image/svg+xml;charset=UTF-8,%3csvg...")
      no-repeat right 1rem center;
  }

  /* Секция с атрибутами */
  &__attributes {
    background: #ffffff;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  }

  &__subtitle {
    font-size: 1.25rem;
    font-weight: 600;
    color: #2d3748;
    margin-bottom: 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid #e2e8f0;
  }

  /* Список существующих атрибутов */
  .attributes-list {
    &__item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 1rem;
      margin-bottom: 0.75rem;
      background: #f8fafc;
      border-radius: 8px;
      transition: all 0.2s;

      &:hover {
        background: #f0f4f8;
      }
    }

    &__info {
      display: flex;
      gap: 1.5rem;
      align-items: center;
    }

    &__name {
      font-weight: 500;
      color: #2d3748;
      min-width: 180px;
    }

    &__value {
      color: #718096;
      font-size: 0.95em;
    }

    &__remove-btn {
      color: #cbd5e0;
      padding: 0.5rem;
      border-radius: 6px;
      transition: all 0.2s;

      &:hover {
        color: #f56565;
        background: rgba(245, 101, 101, 0.1);
      }
    }
  }

  /* Блок добавления новых атрибутов */
  &__attribute-group {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    align-items: center;

    select {
      flex: 1 1 40%;
    }

    input {
      flex: 2 1 60%;
    }
  }

  &__add-btn {
    width: 100%;
    padding: 0.75rem;
    background: #f7fafc;
    color: #718096;
    border: 1px dashed #cbd5e0;
    border-radius: 8px;
    transition: all 0.2s;

    &:hover {
      background: #ebf8ff;
      border-color: #90cdf4;
      color: #4299e1;
    }
  }

  /* Кнопки действий */
  &__submit-btn {
    background: #4299e1;
    color: white;
    padding: 0.875rem 1.5rem;
    border-radius: 8px;
    font-weight: 500;
    transition: all 0.2s;
    margin-top: 1.5rem;

    &:hover {
      background: #3182ce;
      transform: translateY(-1px);
    }
  }

  /* Загрузка изображений */
  &__images {
    background: #ffffff;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  }

  .images-preview {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;

    .image-preview {
      background: #fff;
      padding: 1rem;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

      h4 {
        margin: 0 0 1rem 0;
        font-size: 1.1rem;
        color: #2d3748;
      }

      img {
        width: 100%;
        height: auto;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
      }
    }
  }

  /* Сообщения об ошибках */
  &__error {
    background: #fed7d7;
    color: #c53030;
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 2rem;
    border: 1px solid #feb2b2;
  }

  /* Состояния пустых блоков */
  .attributes-empty {
    color: #cbd5e0;
    text-align: center;
    padding: 2rem;
    border: 2px dashed #e2e8f0;
    border-radius: 8px;
    margin: 1rem 0;
  }
}
</style>

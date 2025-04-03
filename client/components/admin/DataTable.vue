<template>
  <div class="table-wrapper">
    <!-- Панель управления с поиском -->
    <div class="table-controls" v-if="enableSearch">
      <div class="search-input">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Поиск..."
          @input="handleSearch"
        />
        <span class="search-icon">🔍</span>
      </div>
    </div>

    <div class="table-container">
      <table class="data-table">
        <thead>
          <tr>
            <th
              v-for="column in columns"
              :key="column.key"
              @click="toggleSort(column)"
              :class="{ sortable: column.sortable }"
            >
              <div class="header-content">
                {{ column.title }}
                <span v-if="sortedColumn === column.key" class="sort-indicator">
                  {{ sortDirection === "asc" ? "↑" : "↓" }}
                </span>
              </div>
            </th>
          </tr>
        </thead>

        <transition-group name="table-rows" tag="tbody">
          <tr
            v-for="(row, index) in processedRows"
            :key="row.id || index"
            class="table-row"
          >
            <td v-for="column in columns" :key="column.key">
              <template v-if="column.key === 'actions'">
                <slot name="actions" :row="row" />
              </template>
              <template v-else-if="column.type === 'image'">
                <img
                  v-if="row[column.key]"
                  :src="row[column.key]"
                  :alt="row[column.altKey || 'image']"
                  class="table-image"
                />
                <span v-else class="no-image">—</span>
              </template>
              <template v-else>
                {{ formatCell(row[column.key], column) }}
              </template>
            </td>
          </tr>
        </transition-group>
      </table>

      <div v-if="processedRows.length === 0" class="empty-state">
        Ничего не найдено
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  columns: {
    type: Array,
    required: true,
    validator: (value) => value.every((col) => "title" in col && "key" in col),
  },
  rows: {
    type: Array,
    required: true,
  },
  enableSearch: {
    type: Boolean,
    default: true,
  },
});

const emit = defineEmits(["sort", "search"]);

const searchQuery = ref("");
const sortedColumn = ref("");
const sortDirection = ref("asc");

// Форматирование ячеек
const formatCell = (value, column) => {
  if (column.formatter) return column.formatter(value);
  if (column.type === "date") return new Date(value).toLocaleDateString();
  if (column.type === "currency") return `${Number(value).toFixed(2)} ₽`;
  return value;
};

// Обработка сортировки
const toggleSort = (column) => {
  if (sortedColumn.value === column.key) {
    sortDirection.value = sortDirection.value === "asc" ? "desc" : "asc";
  } else {
    sortedColumn.value = column.key;
    sortDirection.value = "asc";
  }

  emit("sort", { column: column.key, direction: sortDirection.value });
};

// Фильтрация и сортировка данных
const processedRows = computed(() => {
  let filtered = [...props.rows];

  // Фильтрация
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter((row) =>
      props.columns.some((col) =>
        String(row[col.key]).toLowerCase().includes(query)
      )
    );
  }

  // Сортировка
  if (sortedColumn.value) {
    const column = props.columns.find((c) => c.key === sortedColumn.value);
    filtered.sort((a, b) => {
      const valA = a[sortedColumn.value];
      const valB = b[sortedColumn.value];

      if (column?.sortFn) return column.sortFn(valA, valB, sortDirection.value);
      if (typeof valA === "number")
        return (valA - valB) * (sortDirection.value === "asc" ? 1 : -1);
      return (
        String(valA).localeCompare(String(valB)) *
        (sortDirection.value === "asc" ? 1 : -1)
      );
    });
  }

  return filtered;
});

// Обработчик поиска с debounce
let searchTimeout = null;
const handleSearch = () => {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    emit("search", searchQuery.value);
  }, 300);
};
</script>

<style scoped>
.table-wrapper {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  overflow: hidden;
  margin-top: 24px;
}

.table-controls {
  padding: 1rem;
  border-bottom: 1px solid #eee;
}

.search-input {
  position: relative;
  max-width: 300px;

  input {
    width: 100%;
    padding: 0.75rem 2rem 0.75rem 1rem;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    transition: border-color 0.2s;

    &:focus {
      outline: none;
      border-color: #3b82f6;
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }
  }
}

.search-icon {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  opacity: 0.6;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;

  th {
    background: #f8fafc;
    font-weight: 600;
    color: #64748b;
    padding: 1rem;
    border-bottom: 2px solid #e2e8f0;
    cursor: pointer;
    transition: background 0.2s;

    &:hover {
      background: #f1f5f9;
    }

    &.sortable {
      cursor: pointer;
      user-select: none;
    }
  }

  td {
    padding: 1rem;
    border-bottom: 1px solid #f1f5f9;
  }

  tr:last-child td {
    border-bottom: none;
  }

  tr.table-row {
    transition: all 0.3s ease;

    &:hover {
      background: #f8fafc;
    }
  }
}

.sort-indicator {
  margin-left: 0.5rem;
  color: #3b82f6;
}

.table-image {
  width: 60px;
  height: 60px;
  object-fit: contain;
  border-radius: 4px;
  background: #f8fafc;
  padding: 4px;
  border: 1px solid #e2e8f0;
}

.no-image {
  color: #94a3b8;
  font-style: italic;
}

.empty-state {
  padding: 2rem;
  text-align: center;
  color: #94a3b8;
}

/* Анимации */
.table-rows-enter-active,
.table-rows-leave-active {
  transition: all 0.3s ease;
}

.table-rows-enter-from,
.table-rows-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

.table-rows-move {
  transition: transform 0.3s ease;
}
</style>

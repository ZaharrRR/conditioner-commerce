<template>
  <button :class="buttonClasses" :disabled="disabled" @click="handleClick">
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
import { computed } from "vue";

const props = defineProps({
  size: {
    type: String as () => "small" | "medium" | "large",
    default: "medium",
  },
  color: {
    type: String as () =>
      | "blue"
      | "blue-dark"
      | "blue-darkest"
      | "blue-accent"
      | "blue-light"
      | "blue-lightest",
    default: "blue",
  },
  variant: {
    type: String as () => "solid" | "outline" | "link",
    default: "solid",
  },
  className: { type: String, default: "" },
  disabled: { type: Boolean, default: false },
});

const emit = defineEmits(["click"]);

const buttonClasses = computed(() => [
  "button",
  `button--${props.size}`,
  `button--${props.variant}`,
  `button--${props.color}`,
  props.className,
  { "button--disabled": props.disabled },
]);

const handleClick = (event: MouseEvent) => {
  if (!props.disabled) emit("click", event);
};
</script>

<style scoped>
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
}

.button:hover {
  scale: 1.05;
}

.button--small {
  padding: 4px 8px;
  font-size: 16px;
}
.button--medium {
  padding: 8px 16px;
  font-size: 20px;
}
.button--large {
  padding: 16px 32px;
  font-size: 24px;
}

.button--solid {
  background-color: var(--blue);
  color: white;
  &.button--blue-dark {
    background-color: var(--blue-dark);
  }
  &.button--blue-darkest {
    background-color: var(--blue-darkest);
  }
  &.button--blue-accent {
    background-color: var(--blue-accent);
  }
  &.button--blue-light {
    background-color: var(--blue-light);
  }
  &.button--blue-lightest {
    background-color: var(--blue-lightest);
  }
}

.button--outline {
  background-color: transparent;
  border: 2px solid var(--blue);
  color: var(--blue);
  &.button--blue-dark {
    border-color: var(--blue-dark);
    color: var(--blue-dark);
  }
  &.button--blue-darkest {
    border-color: var(--blue-darkest);
    color: var(--blue-darkest);
  }
  &.button--blue-accent {
    border-color: var(--blue-accent);
    color: var(--blue-accent);
  }
  &.button--blue-light {
    border-color: var(--blue-light);
    color: var(--blue-light);
  }
  &.button--blue-lightest {
    border-color: var(--blue-lightest);
    color: var(--blue-lightest);
  }
}

.button--link {
  background-color: transparent;
  color: var(--blue);
  text-decoration: underline;
  &.button--blue-dark {
    color: var(--blue-dark);
  }
  &.button--blue-darkest {
    color: var(--blue-darkest);
  }
  &.button--blue-accent {
    color: var(--blue-accent);
  }
  &.button--blue-light {
    color: var(--blue-light);
  }
  &.button--blue-lightest {
    color: var(--blue-lightest);
  }
}

.button--disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>

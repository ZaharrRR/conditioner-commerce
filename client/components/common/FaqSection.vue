<template>
  <section class="faq-section">
    <h2 class="faq-section__title">{{ title }}</h2>
    <div class="faq-items">
      <div
        v-for="(item, index) in items"
        :key="index"
        class="faq-item"
        itemscope
        itemprop="mainEntity"
        itemtype="https://schema.org/Question"
      >
        <h3 class="faq-item__question" itemprop="name">
          {{ item.question }}
        </h3>
        <div
          class="faq-item__answer"
          itemscope
          itemprop="acceptedAnswer"
          itemtype="https://schema.org/Answer"
        >
          <p itemprop="text">{{ item.answer }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const props = defineProps({
  title: {
    type: String,
    default: "Частые вопросы",
  },
  items: {
    type: Array,
    required: true,
    validator: (value) => {
      return value.every((item) => "question" in item && "answer" in item);
    },
  },
});

useHead({
  script: [
    {
      type: "application/ld+json",
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        mainEntity: props.items.map((item) => ({
          "@type": "Question",
          name: item.question,
          acceptedAnswer: {
            "@type": "Answer",
            text: item.answer,
          },
        })),
      }),
    },
  ],
});
</script>

<style lang="scss" scoped>
.faq-section {
  margin: 40px 0;
  padding: 30px;
  background: #f8f9fa;
  border-radius: 15px;

  &__title {
    font-size: 28px;
    margin-bottom: 25px;
    color: #333;
  }
}

.faq-item {
  margin-bottom: 20px;
  padding: 15px;
  border-bottom: 1px solid #eee;

  &__question {
    font-size: 18px;
    color: var(--blue);
    margin-bottom: 10px;
  }

  &__answer {
    font-size: 16px;
    color: #555;
    line-height: 1.6;
  }
}

@media (max-width: 768px) {
  .faq-section {
    padding: 20px;

    &__title {
      font-size: 24px;
    }
  }

  .faq-item {
    &__question {
      font-size: 16px;
    }

    &__answer {
      font-size: 14px;
    }
  }
}
</style>

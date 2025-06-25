<script setup>
const props = defineProps({
  question: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['click-on-answer']);

function onAnswerClicked(index) {
  emit('click-on-answer', index);
}
</script>

<template>
  <div class="question-display">
    <h2>{{ question.text }}</h2>

    <img v-if="question.image" :src="question.image" alt="Illustration" class="question-image" />

    <div class="answers">
      <button
        v-for="(answer, index) in question.choices"
        :key="index"
        class="btn btn-outline-light m-2"
        @click="onAnswerClicked(index)"
      >
        {{ answer }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.question-image {
  max-width: 100%;
  height: auto;
  margin-bottom: 1rem;
}

.answers {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>

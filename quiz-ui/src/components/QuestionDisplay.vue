<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  question: Object,
});
const emit = defineEmits(['validated']);

const selectedIndex = ref(null);
const showError = ref(false);

watch(
  () => props.question,
  () => {
    selectedIndex.value = null;
    showError.value = false;
  }
);

function select(index) {
  selectedIndex.value = index;
}

function validateAnswer() {
  if (selectedIndex.value === null) {
    showError.value = true;
    return;
  }
  showError.value = false;
  emit('validated', selectedIndex.value + 1); // 1-based
}
</script>

<template>
  <div class="question-display">
    <h2>{{ question.title }}</h2>
    <p>{{ question.text }}</p>
    <img v-if="question.image" :src="question.image" alt="illustration" class="question-image" />

    <ul>
      <li
        v-for="(answer, index) in question.possibleAnswers"
        :key="index"
        :class="{ selected: selectedIndex === index }"
        @click="select(index)"
      >
        {{ answer.text }}
      </li>
    </ul>

    <button class="btn-validate" @click="validateAnswer">✅ Valider</button>
    <p v-if="showError" class="text-danger mt-2">
      ⚠️ Veuillez sélectionner une réponse avant de valider.
    </p>
  </div>
</template>

<style scoped>
.question-display {
  background: #222;
  padding: 20px;
  border-radius: 10px;
}
.question-image {
  max-width: 100%;
  height: auto;
  margin-top: 10px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  padding: 10px;
  background: #444;
  margin-bottom: 5px;
  cursor: pointer;
  border-radius: 5px;
}
li.selected {
  background-color: #2ecc71;
  font-weight: bold;
}
.btn-validate {
  margin-top: 15px;
  padding: 10px 20px;
  background-color: #3498db;
  border: none;
  border-radius: 6px;
  color: white;
  cursor: pointer;
}
</style>

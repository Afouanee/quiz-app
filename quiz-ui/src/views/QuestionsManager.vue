<script setup>
import { ref, onMounted } from 'vue';
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import ScoreDisplay from '@/components/ScoreDisplay.vue';
import ParticipationStorageService from '@/services/ParticipationStorageService';

const currentQuestionPosition = ref(0);
const currentQuestion = ref(null);
const totalNumberOfQuestions = ref(0);
const allQuestions = ref([]);
const score = ref(0);
const quizEnded = ref(false);

async function fetchQuestions() {
  const res = await fetch('http://localhost:5000/questions');
  return await res.json();
}

function answerClickedHandler(index) {
  const correctAnswer = currentQuestion.value.answer;
  if (index === correctAnswer) {
    score.value++;
  }

  if (currentQuestionPosition.value < allQuestions.value.length - 1) {
    currentQuestionPosition.value++;
    currentQuestion.value = allQuestions.value[currentQuestionPosition.value];
  } else {
    endQuiz();
  }
}

function endQuiz() {
  ParticipationStorageService.saveParticipationScore(score.value);
  quizEnded.value = true;
}

onMounted(async () => {
  allQuestions.value = await fetchQuestions();
  totalNumberOfQuestions.value = allQuestions.value.length;
  currentQuestion.value = allQuestions.value[0]; // Important : charger la première question
});
</script>

<template>
  <div class="questions-manager">
    <template v-if="!quizEnded && currentQuestion">
      <h1>Question {{ currentQuestionPosition + 1 }} / {{ totalNumberOfQuestions }}</h1>
      <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
    </template>

    <template v-else-if="quizEnded">
      <ScoreDisplay />
    </template>
  </div>
</template>

<style scoped>
.questions-manager {
  max-width: 800px;
  margin: 50px auto;
  padding: 24px;
  background-color: #1e1e1e;
  color: white;
  border-radius: 12px;
}
</style>

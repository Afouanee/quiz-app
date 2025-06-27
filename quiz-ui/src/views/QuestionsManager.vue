<script setup>
import { ref, onMounted } from 'vue';
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import ScoreDisplay from '@/components/ScoreDisplay.vue';
import ParticipationStorageService from '@/services/ParticipationStorageService';
import QuizApiService from '@/services/QuizApiService';

const currentQuestionPosition = ref(1); // Les positions sont 1-based
const currentQuestion = ref(null);
const totalNumberOfQuestions = ref(0);
const score = ref(0);
const quizEnded = ref(false);
const answers = ref([]);

async function loadQuestion(position) {
  try {
    const question = await QuizApiService.getQuestionByPosition(position);
    currentQuestion.value = question;
  } catch (err) {
    console.error(`Erreur lors du chargement de la question ${position}`, err);
  }
}

function handleValidatedAnswer(selectedIndex) {
  answers.value.push(selectedIndex); // 1-based index envoyé par le composant

  if (currentQuestionPosition.value < totalNumberOfQuestions.value) {
    currentQuestionPosition.value++;
    loadQuestion(currentQuestionPosition.value);
  } else {
    endQuiz();
  }
}

async function endQuiz() {
  const playerName = ParticipationStorageService.getPlayerName();

  try {
    const result = await QuizApiService.submitParticipation({
      playerName,
      answers: answers.value,
    });

    ParticipationStorageService.saveParticipationScore(result.score);
    score.value = result.score;
    quizEnded.value = true;
  } catch (error) {
    console.error("Erreur de soumission :", error);
  }
}

onMounted(async () => {
  try {
    const quizInfo = await QuizApiService.getQuizInfo();
    totalNumberOfQuestions.value = quizInfo.size;

    if (totalNumberOfQuestions.value > 0) {
      await loadQuestion(currentQuestionPosition.value);
    }
  } catch (error) {
    console.error("Impossible de charger les infos du quiz :", error);
  }
});
</script>

<template>
  <div class="questions-manager">
    <template v-if="!quizEnded && currentQuestion">
      <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
      <QuestionDisplay
        :question="currentQuestion"
        @validated="handleValidatedAnswer"
      />
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

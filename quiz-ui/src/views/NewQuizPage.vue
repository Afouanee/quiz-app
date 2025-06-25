<script setup>
import { ref } from 'vue';
import ParticipationStorageService from '@/services/ParticipationStorageService';
import { useRouter } from 'vue-router';

const username = ref('');
const showError = ref(false);
const router = useRouter();

function launchNewQuiz() {
  if (!username.value.trim()) {
    showError.value = true;
    return;
  }

  showError.value = false;
  ParticipationStorageService.savePlayerName(username.value);
  router.push('/questions');
}
</script>

<template>
  <div class="new-quiz-page">
    <h2>Page de participation au quiz</h2>
    <p>Saisissez votre nom :</p>
    <input type="text" class="form-control" placeholder="Username" v-model="username" />

    <button class="btn btn-outline-danger mt-3" @click="launchNewQuiz">GO!</button>
    <p v-if="showError" class="text-danger mt-2">
      ⚠️ Veuillez entrer un nom pour commencer le quiz.
    </p>
  </div>
</template>

<style scoped>
.new-quiz-page {
  max-width: 500px;
  margin: 60px auto;
  padding: 24px;
  background-color: #1e1e1e;
  color: white;
  border-radius: 12px;
}
</style>

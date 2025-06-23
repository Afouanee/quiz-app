<script setup>
import { ref } from 'vue';
import ParticipationStorageService from '@/services/ParticipationStorageService';
import { useRouter } from 'vue-router';

const username = ref('');
const router = useRouter();

function launchNewQuiz() {
  ParticipationStorageService.savePlayerName(username.value);
  console.log('Nom enrengistré :', username.value);
  router.push('/questions');
}
</script>

<template>
  <div class="new-quiz-page">
    <h2>Page de participation au quiz</h2>
    <p>Saisissez votre nom :</p>
    <input type="text" class="form-control" placeholder="Username" v-model="username" />

    <button class="btn btn-outline-danger mt-3" @click="launchNewQuiz">GO!</button>
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

<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from '@/services/QuizApiService';

const registeredScores = ref([]);

onMounted(async () => {
  try {
    const response = await quizApiService.getQuizInfo();
    registeredScores.value = response.data;
    console.log('Scores récupérés :', registeredScores.value);
  } catch (error) {
    console.error('Erreur API:', error);
  }
});
</script>

<template>
  <div>
    <h1>Home page</h1>

    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.name }} - {{ scoreEntry.score }}
    </div>

    <RouterLink to="/new-quiz">Démarrer le quiz !</RouterLink>
  </div>
</template>

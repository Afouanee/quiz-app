<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import QuizApiService from '@/services/QuizApiService';

const registeredScores = ref([]);
const clearError = ref('');
const clearSuccess = ref('');

async function fetchScores() {
  try {
    const { scores } = await QuizApiService.getQuizInfo();
    registeredScores.value = scores;
  } catch (err) {
    console.error('Erreur récupération scores :', err);
  }
}

async function clearScores() {
  clearError.value = '';
  clearSuccess.value = '';
  try {
    await QuizApiService.deleteAllParticipations();
    clearSuccess.value = '✅ Scores réinitialisés avec succès !';
    await fetchScores(); // Met à jour l'affichage
  } catch (e) {
    clearError.value = '❌ Erreur : vous devez être connecté en admin.';
    console.error(e);
  }
}

onMounted(fetchScores);
</script>

<template>
  <div class="homepage">
    <h1>🏠 Page d'accueil</h1>

    <div class="score-entry" v-for="entry in registeredScores" :key="entry.id">
      {{ entry.playerName }} — {{ entry.score }} pts ({{ entry.date }})
    </div>

    <RouterLink to="/new-quiz" class="btn btn-primary mt-3">Démarrer le quiz !</RouterLink>
    <button class="btn btn-danger mt-3 ms-2" @click="clearScores">
      🗑 Réinitialiser les scores
    </button>

    <p class="text-success mt-2" v-if="clearSuccess">{{ clearSuccess }}</p>
    <p class="text-danger mt-2" v-if="clearError">{{ clearError }}</p>
  </div>
</template>

<style scoped>
.homepage {
  color: white;
  padding: 24px;
}

.score-entry {
  margin-bottom: 0.5rem;
}

.text-success {
  color: #28a745;
}

.text-danger {
  color: red;
}
</style>

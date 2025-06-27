<script setup>
import { onMounted, ref } from 'vue';
import participationStorageService from '@/services/ParticipationStorageService';

const playerName = ref('');
const score = ref(0);

onMounted(() => {
  playerName.value = participationStorageService.getPlayerName();
  score.value = participationStorageService.getParticipationScore();
});
</script>

<template>
  <div class="score-display container mt-5">
    <div class="card p-4 text-center bg-dark text-white shadow rounded">
      <h2 class="mb-3">🎉 Félicitations {{ playerName }} !</h2>
      <p class="display-6">Votre score est :</p>
      <div class="score-box my-4">
        <span class="score">{{ score }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.score-box {
  font-size: 4rem;
  font-weight: bold;
  background-color: #343a40;
  color: #00ffcc;
  padding: 20px 40px;
  border-radius: 16px;
  display: inline-block;
  box-shadow: 0 0 10px rgba(0, 255, 204, 0.5);
}
</style>

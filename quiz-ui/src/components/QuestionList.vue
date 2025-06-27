<script setup>
import { ref, onMounted } from 'vue';
import QuizApiService from '@/services/QuizApiService';

const questions = ref([]);
const loading = ref(true);

async function fetchQuestions() {
  try {
    questions.value = await QuizApiService.getAllQuestions();
  } catch (err) {
    console.error("Erreur récupération questions :", err);
  } finally {
    loading.value = false;
  }
}

async function deleteQuestion(id) {
  if (confirm("Confirmer la suppression ?")) {
    try {
      await QuizApiService.deleteQuestion(id);
      questions.value = questions.value.filter(q => q.id !== id);
    } catch (err) {
      console.error("Erreur suppression question :", err);
    }
  }
}

onMounted(() => {
  fetchQuestions();
});
</script>

<template>
  <div class="questions-list">
    <h2>📋 Liste des questions</h2>

    <button class="btn btn-success mb-3" @click="$emit('create-question')">
  ➕ Créer une nouvelle question
    </button>


    <div v-if="loading">Chargement...</div>
    <div v-else-if="questions.length === 0">Aucune question.</div>

    <table v-else class="table table-dark table-striped">
      <thead>
        <tr>
          <th>#</th>
          <th>Titre</th>
          <th>Texte</th>
          <th>Position</th>
          <th>Actions</th>
        </tr>
      </thead>
      <!-- QuestionList.vue -->
        <tbody>
        <tr v-for="question in questions" :key="question.id">
            <td>{{ question.id }}</td>
            <td>{{ question.title }}</td>
            <td>{{ question.text }}</td>
            <td>{{ question.position }}</td>
            <td>
            <button class="btn btn-warning btn-sm me-2" @click="$emit('edit-question', question)">
                ✏️ Modifier
            </button>
            <button class="btn btn-danger btn-sm" @click="deleteQuestion(question.id)">
                🗑 Supprimer
            </button>
            </td>
        </tr>
        </tbody>

    </table>
  </div>
</template>

<style scoped>
.questions-list {
  margin-top: 1.5rem;
}

table {
  width: 100%;
}
</style>

<script setup>
import { ref } from 'vue';
import QuestionList from '@/components/QuestionList.vue';
import QuestionForm from '@/components/QuestionForm.vue';

const adminMode = ref('list'); // list | create | edit
const questionInEdition = ref(null); // null pour création, sinon une question à éditer

function editQuestion(question) {
  // Clonage sûr de l'objet
  questionInEdition.value = JSON.parse(JSON.stringify(question));
  adminMode.value = 'edit';
}

function createQuestion() {
  questionInEdition.value = null;
  adminMode.value = 'create';
}

function handleSubmit() {
  adminMode.value = 'list';
}
</script>

<template>
  <div class="admin-page">
    <h1>🛠️ Administration</h1>

    <!-- Liste des questions -->
    <QuestionList
      v-if="adminMode === 'list'"
      @edit-question="editQuestion"
      @create-question="createQuestion"
    />

    <!-- Formulaire de création ou d'édition -->
    <QuestionForm
      v-if="adminMode === 'create' || adminMode === 'edit'"
      :modelValue="questionInEdition"
      @update:modelValue="val => questionInEdition.value = val"
      @submit="handleSubmit"
      @cancel="adminMode = 'list'"
    />
  </div>
</template>

<style scoped>
.admin-page {
  max-width: 900px;
  margin: 60px auto;
  padding: 24px;
  color: white;
}
</style>

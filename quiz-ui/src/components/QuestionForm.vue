<script setup>
import { ref, watch } from 'vue';
import QuizApiService from '@/services/QuizApiService';

const props = defineProps({
  modelValue: Object,
});
const emit = defineEmits(['submit', 'cancel']);

const localQuestion = ref(
  props.modelValue
    ? JSON.parse(JSON.stringify(props.modelValue))
    : {
        position: 1,
        title: '',
        text: '',
        image: '',
        possibleAnswers: [
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
        ],
      }
);

const error = ref('');

watch(
  () => props.modelValue,
  (newVal) => {
    localQuestion.value = newVal
      ? JSON.parse(JSON.stringify(newVal))
      : {
          position: 1,
          title: '',
          text: '',
          image: '',
          possibleAnswers: [
            { text: '', isCorrect: false },
            { text: '', isCorrect: false },
          ],
        };
    error.value = '';
  }
);

// Ajouter une réponse
function addAnswer() {
  localQuestion.value.possibleAnswers.push({ text: '', isCorrect: false });
}

// Supprimer une réponse
function removeAnswer(index) {
  localQuestion.value.possibleAnswers.splice(index, 1);
}

// Forcer une seule bonne réponse
function setCorrectAnswer(index) {
  localQuestion.value.possibleAnswers.forEach((answer, i) => {
    answer.isCorrect = i === index;
  });
}

// Soumettre
async function handleSubmit() {
  const q = localQuestion.value;

  if (!q.title || !q.text) {
    error.value = 'Le titre et le texte sont requis.';
    return;
  }

  const correctCount = q.possibleAnswers.filter((a) => a.isCorrect).length;
  if (correctCount !== 1) {
    error.value = 'Il doit y avoir exactement UNE seule réponse correcte.';
    return;
  }

  error.value = '';
  try {
    const action = props.modelValue
      ? QuizApiService.updateQuestion(q.id, q)
      : QuizApiService.createQuestion(q);
    await action;
    emit('submit');
  } catch (e) {
    error.value = 'Erreur lors de la sauvegarde.';
    console.error(e);
  }
}
</script>

<template>
  <div class="question-form">
    <h3>{{ props.modelValue ? 'Modifier' : 'Créer' }} une question</h3>

    <label>Position :</label>
    <input type="number" v-model="localQuestion.position" min="1" />

    <label>Titre :</label>
    <input type="text" v-model="localQuestion.title" />

    <label>Texte :</label>
    <input type="text" v-model="localQuestion.text" />

    <label>Image (URL base64 ou lien) :</label>
    <input type="text" v-model="localQuestion.image" />

    <label>Réponses possibles :</label>
    <div
      v-for="(answer, index) in localQuestion.possibleAnswers"
      :key="index"
      class="answer-line"
    >
      <input type="text" v-model="answer.text" placeholder="Texte" />
      <label>
        <input
          type="radio"
          :checked="answer.isCorrect"
          @change="setCorrectAnswer(index)"
        />
        Bonne réponse
      </label>
      <button
        @click="removeAnswer(index)"
        v-if="localQuestion.possibleAnswers.length > 2"
      >
        🗑
      </button>
    </div>
    <button @click="addAnswer">➕ Ajouter une réponse</button>

    <div class="buttons">
      <button @click="handleSubmit">✅ Enregistrer</button>
      <button @click="$emit('cancel')">❌ Annuler</button>
    </div>

    <p class="text-danger mt-2" v-if="error">{{ error }}</p>
  </div>
</template>

<style scoped>
.question-form {
  margin-top: 20px;
  padding: 1rem;
  background: #1e1e1e;
  border-radius: 10px;
  color: white;
}
.question-form input[type='text'],
.question-form input[type='number'] {
  display: block;
  margin-bottom: 8px;
  width: 100%;
  padding: 5px;
  border-radius: 5px;
}
.answer-line {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-bottom: 5px;
}
.buttons {
  margin-top: 10px;
  display: flex;
  gap: 1rem;
}
.text-danger {
  color: red;
}
</style>

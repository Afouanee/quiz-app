<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const password = ref('');
const error = ref('');
const router = useRouter();

async function login() {
  error.value = '';
  try {
    const res = await axios.post('http://localhost:5000/login', {
      password: password.value,
    });

    const token = res.data.token;
    if (token) {
      localStorage.setItem('token', token); // ✅ cohérent avec App.vue
      router.push('/admin');
    } else {
      error.value = 'Token manquant dans la réponse.';
    }
  } catch (err) {
    console.error(err);
    error.value = 'Mot de passe incorrect ou erreur serveur.';
  }
}
</script>

<template>
  <div class="login-page">
    <h1>🔐 Connexion Admin</h1>

    <input
      type="password"
      placeholder="Mot de passe"
      v-model="password"
      class="form-control"
    />

    <button class="btn btn-primary mt-3" @click="login">Connexion</button>

    <div v-if="error" class="text-danger mt-2">{{ error }}</div>
  </div>
</template>

<style scoped>
.login-page {
  max-width: 400px;
  margin: 80px auto;
  padding: 24px;
  background: #1e1e1e;
  border-radius: 12px;
  color: white;
}
input {
  width: 100%;
  padding: 8px;
  margin-top: 1rem;
  border-radius: 6px;
  border: 1px solid #ccc;
}
button {
  width: 100%;
  padding: 10px;
  background-color: teal;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
</style>

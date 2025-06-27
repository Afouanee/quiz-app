import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

const instance = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

function getAuthHeaders() {
  const token = localStorage.getItem('adminToken');
  return token
    ? { Authorization: `Bearer ${token}` }
    : {};
}

export default {
  // 📊 PARTICIPATION (publique)
  async getQuizInfo() {
    const response = await instance.get('/quiz-info');
    return response.data;
  },

  async submitParticipation(payload) {
    const response = await instance.post('/participations', payload);
    return response.data; // retourne le score calculé
  },

  // 📚 QUESTIONS (lecture publique)
  async getAllQuestions() {
    const response = await instance.get('/questions');
    return response.data;
  },

  async deleteAllParticipations() {
  const token = localStorage.getItem('adminToken');
  const headers = token ? { Authorization: `Bearer ${token}` } : {};
  const response = await instance.delete('/participations/all', { headers });
  return response.data;
  },

  async getQuestionById(id) {
    const response = await instance.get(`/questions/${id}`);
    return response.data;
  },

  async getQuestionByPosition(position) {
    const response = await instance.get(`/questions/position/${position}`);
    return response.data;
  },

  // ✏️ QUESTIONS (opérations protégées)
  async createQuestion(payload) {
    const response = await instance.post('/questions', payload, {
      headers: getAuthHeaders(),
    });
    return response.data;
  },

  async updateQuestion(id, payload) {
    const response = await instance.put(`/questions/${id}`, payload, {
      headers: getAuthHeaders(),
    });
    return response.data;
  },

  async deleteQuestion(id) {
    const response = await instance.delete(`/questions/${id}`, {
      headers: getAuthHeaders(),
    });
    return response.data;
  },

  async deleteAllQuestions() {
    const response = await instance.delete('/questions', {
      headers: getAuthHeaders(),
    });
    return response.data;
  },
};

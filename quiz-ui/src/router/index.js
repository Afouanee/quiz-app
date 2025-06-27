import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import NewQuizPage from '../views/NewQuizPage.vue';
import QuestionsManager from '../views/QuestionsManager.vue';
import ScoreDisplay from '@/components/ScoreDisplay.vue';
import LoginPage from '@/views/LoginPage.vue';
import AdminPage from '@/views/AdminPage.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/new-quiz',
    name: 'NewQuizPage',
    component: NewQuizPage,
  },
  {
    path: '/questions',
    name: 'QuestionsManager',
    component: QuestionsManager,
  },
  {
    path: '/score',
    name: 'ScoreDisplay',
    component: ScoreDisplay,
  },
  { 
    path: '/login',
    name: 'Login', 
    component: LoginPage
  },
  {
    path: '/admin',
    name: 'AdminPage',
    component: AdminPage,
    beforeEnter: (to, from, next) => {
      const token = localStorage.getItem('token')
      if (token) {
        next()
      } else {
        next('/login')
      }
    }
  },
];


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;

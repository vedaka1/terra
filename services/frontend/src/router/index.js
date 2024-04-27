// import axios from 'axios';
import { useAuthStore } from '@/store/auth';
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      meta: { requiresAuth: true },
      component: () => import('../views/HomePage.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginPage.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/SignUpPage.vue')
    },
    {
      path: '/friends',
      name: 'friends',
      meta: { requiresAuth: true },
      component: () => import('../views/FriendsPage.vue')
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: () => import('../views/ProfilePage.vue')
    },
    {
      path: '/chats',
      name: 'chats',
      meta: { requiresAuth: true },
      component: () => import('../views/MessagesPage.vue')
    },
    {
      path: '/chats/:id',
      name: 'chat',
      meta: { requiresAuth: true },
      component: () => import('../views/ChatPage.vue')
    }
  ]
})

router.beforeEach(async (to, _, next) => {
  // const requiresAdmin = to.matched.some((record) => record.meta.requiresAdmin);
  // const isAuthenticated = axios.get('/user/me', {withCredentials: true});
  const authStore = useAuthStore();
  if (to.matched.some((record) => record.meta.requiresAuth)) {
      if (authStore.user) {
        next()
      } else {
        next('/login')
      }
  } else {
      next()
  }
})


export default router

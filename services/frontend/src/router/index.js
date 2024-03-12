// import axios from 'axios';
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
      component: () => import('../views/FriendsPage.vue')
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: () => import('../views/ProfilePage.vue')
    },
    {
      path: '/messages',
      name: 'messages',
      component: () => import('../views/MessagesPage.vue')
    }
  ]
})

router.beforeEach(async (to, _, next) => {
  // const requiresAdmin = to.matched.some((record) => record.meta.requiresAdmin);
  // const isAuthenticated = axios.get('/user/me', {withCredentials: true});
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    const isAuthenticated = localStorage.getItem('user')
      if (isAuthenticated) {
        next()
      } else {
        next('/login')
      }
  } else {
      next()
  }
})


export default router

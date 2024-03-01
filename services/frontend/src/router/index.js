// import axios from 'axios';
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
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
    
    // .then((response) => {
    //     console.log('gggg');
    //     if (requiresAuth && response.status == 401) {
    //         next("/login");
    //     }
        
    //     } else {
    //         next();
    //     }
});


export default router

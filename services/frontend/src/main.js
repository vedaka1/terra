import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import { user } from '@/store/user'

axios.defaults.withCredentials = true
axios.defaults.baseURL = import.meta.env.VITE_API_URL; // FastApi backend url

axios.interceptors.response.use(undefined, async (error) => {
  if (error) {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      await axios.post('/auth/refresh')
      .catch((error) => {
          console.log(error);
          user.LogOut()
          return router.push('/login')
      })
    }
  }
});

document.body.classList.add('dark-theme')

createApp(App).use(router).mount('#app')

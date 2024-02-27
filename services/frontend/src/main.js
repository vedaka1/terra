import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import '@/main.css'
import { user } from '@/store/user'

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:5000/' // FastApi backend

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
      else {
        user.LogIn()
      }
    }
  });

document.body.classList.add('dark-theme')

createApp(App).use(router).mount('#app')

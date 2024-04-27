import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import { createPinia } from 'pinia'
import { useAuthStore } from './store/auth'

main();

axios.defaults.withCredentials = true
axios.defaults.baseURL = import.meta.env.VITE_API_URL; // FastApi backend url

axios.interceptors.response.use(undefined, async (error) => {
  if (error) {
    const authStore = useAuthStore();
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      authStore.refreshToken();
    }
  }
});

document.body.classList.add('dark-theme')
async function main() {
  const app = createApp(App)
  app.use(createPinia())
  app.use(router)
  app.mount('#app')
}

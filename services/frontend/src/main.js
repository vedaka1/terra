import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import '@/main.css'

axios.defaults.baseURL = 'http://localhost:5000/' // FastApi backend

createApp(App).use(router).mount('#app')

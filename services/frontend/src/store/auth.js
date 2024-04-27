import router from "@/router";
import axios, { formToJSON } from "axios";
import { defineStore } from "pinia";

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')),
    }),
    actions: {
        async login(form) {
            try {
                const user = await axios.post('/auth/login', form)
                this.user = user.data;
                localStorage.setItem('user', JSON.stringify(user));
                router.push('/');
            } catch (error) {
                console.log(error);
            }
        },
        async register(form) {
            await axios.post(
                '/auth/register',
                formToJSON(form)
            );
            router.push('/login');
        },
        logout() {
            axios.post('/auth/logout')
            localStorage.removeItem('user');
            this.user = null;
            router.push('/login');
        },
        refreshToken() {
            try {
                axios.post('/auth/refresh')
            } catch (error) {
                localStorage.removeItem('user');
                this.user = null;
                router.push('/login');
            }
        }
    }
})

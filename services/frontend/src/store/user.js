import { defineStore } from "pinia";

export const useUserStore = defineStore('user', {
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')) || null,
    }),
    actions: {
        async me() {
            const user = await axios.get('/users/me');
            this.user = user.data;
            localStorage.setItem('user', JSON.stringify(user));
        }
    }
})

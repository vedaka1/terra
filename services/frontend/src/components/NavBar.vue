<template>
    <aside v-show="authStore.user">
        <div class="wrapper">
            <div class="logo">
                <img src="../assets/hexagon-svgrepo-com.svg" alt="Logo">
            </div>
            <!-- <span>Menu</span> -->
            <div class="menu-toggle-wrap">
                
            </div>
            <div class="menu">
                <RouterLink class="button" to="/">
                    <span class="text">Home</span>
                </RouterLink>
                <RouterLink class="button" to="/friends">
                    <span class="text">Friends</span>
                </RouterLink>
                <RouterLink class="button" to="/chats">
                    <span class="text">Messages</span>
                </RouterLink>
                <button class="button" @click="authStore.logout()">
                    Logout
                </button>
            </div>
        </div>
    </aside>
</template>

<style scoped>
aside {
    display: flex;
    align-items: center;
    width: 100%;
    height: 3rem;
    justify-content: center;
    position: fixed;
    top: 0;
    left: 0;
    backdrop-filter: blur(15px);
    z-index: 10;
    /* background-color: var(--navigation-color); */
}
.wrapper {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    height: 100%;
    max-width: 800px;
    padding: 0;
}
img {
    /* height: 3rem;
    width: 3rem; */
    
}
.logo {
    display: flex;
    height: 3rem;
    width: 3rem;
}
.menu {
    margin-left: 1rem;
    display: flex;
    gap: 1rem;
}
.button {
    display: flex;
    align-items: center;
    padding: 5px;
}
.router-link-exact-active {
    padding: 5px;
    border-radius: 15px;
    background: linear-gradient(90deg, rgba(131,58,180,1) 0%, rgba(92,29,253,1) 50%, rgba(69,134,252,1) 100%);
}
a {
    outline: none;
    text-decoration: none;
    color: var(--text-color);
}
a:active,
a:hover,
a::after {
    text-decoration: none;
    background-color: none;
    color: none;
    -webkit-tap-highlight-color: transparent;
}
</style>

<script setup>
import { useAuthStore } from '@/store/auth';

const authStore = useAuthStore();
</script>
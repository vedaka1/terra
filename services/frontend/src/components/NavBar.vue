<template>
    <aside>
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
            <button class="button" @click="LogOut">
                Logout
            </button>
        </div>
    </aside>
</template>

<style scoped>
aside {
    display: flex;
    align-items: center;
    width: 100%;
    height: 3rem;
    background-color: var(--navigation-color);
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
    background: rgb(131,58,180);
    background: linear-gradient(90deg, rgba(131,58,180,1) 0%, rgba(92,29,253,1) 50%, rgba(69,134,252,1) 100%);
    transition: 0.1s ease-out;
}
a {
    outline: none;
    text-decoration: none;
    color: var(--text-color);
}
</style>

<script setup>
import { useRouter } from 'vue-router';
import axios from 'axios';


const router = useRouter()

const LogOut = async () => {
    await axios.post('/auth/logout')
    .then(() => {
        localStorage.removeItem('user')
        router.push("/login");
    }, (error) => {
    console.log(error);
    }); 
}
</script>
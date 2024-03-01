<template>
    <div class="main-page">
        <NavBar v-if="isAuthorized" />
        <router-view/>
    </div>
</template>

<style>
</style>

<script setup>
import { onMounted, ref } from 'vue';
import NavBar from './components/NavBar.vue';
// import { user } from './store/user'
const isAuthorized = ref('')
// user.LogIn()
onMounted(async () => {
    isAuthorized.value = localStorage.getItem('user')
});

</script>
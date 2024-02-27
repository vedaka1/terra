<template>
    <div class="main-page">
        <NavBar v-if="user.state" />
        <router-view/>
    </div>
</template>

<style>
</style>

<script setup>
import NavBar from './components/NavBar.vue';
import { user } from './store/user'

user.LogIn()
// let isAuthorized = localStorage.getItem('user')
</script>
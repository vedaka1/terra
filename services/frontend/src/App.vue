<template>
    <div class="main-page">
        <NavBar v-if="isAuthorized" />
        <router-view/>
    </div>
</template>

<style>
</style>

<script setup>
import NavBar from './components/NavBar.vue';

const isAuthorized = localStorage.getItem('user')
</script>
<template>
  <div class="main-page">
    <div class="wrapper">
        {{ username }}
    </div>
  </div>
</template>

<style>
</style>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';

const router = useRouter();
let username = ref("")


onMounted(async () => {
    await axios.get('/user/me')
    .then((response) => {
        username.value = response.data.username
    }, (error) => {
        console.log(error);
        router.push("/login");
    });
})

</script>

<template>
  <div class="main-page">
    <div class="wrapper">
        {{ msg }}
    </div>
    <button @click="LogOut">
        LogOut
    </button>
  </div>
</template>

<style>
</style>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
let msg = ref("")

axios.get('/user/me', {withCredentials: true})
.then((response) => {
    msg.value = response.data.username
}, (error) => {
    console.log(error);
    router.push("/login");
});

const LogOut = async () => {
    await axios.post('/auth/logout', {headers: {"Access-Control-Allow-Origin": "https://<FE DOMAIN>",}, withCredentials: true,})
    .then((response) => {
        console.log(response);
        router.push("/login");
    })
}

</script>

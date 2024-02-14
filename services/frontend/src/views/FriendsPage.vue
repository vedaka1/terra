<template>
    <div class="user-card" v-for="user in users" :key="user.id">
        {{ user.username }}
    </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';

const users = ref([])


onMounted(async () => {
    users.value = (await axios.get('/user/all', {params: {offset: 0}})).data
})

</script>

<style scoped>
.user-card {
    margin-top: 1rem;
    border-radius: 15px;
    padding: 1rem;
    background-color: var(--items-color);
}
</style>

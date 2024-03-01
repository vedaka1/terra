<template>
    <div class="main-page">
        <div class="wrapper">
            <button @click="showUsers()">Show all users</button>
            <div class="user-card" v-for="user in users" :key="user.id">
                <RouterLink :to="{name: 'profile', params: {id: user.id}}">
                    {{ user.username }}
                </RouterLink>
                <div class="buttons-row">
                    <button class="button-add" @click="addFriend(user.id)">&plus;</button>
                    <button v-if="!state" class="button-delete" @click="deleteFriend(user.id)">&Cross;</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';


const users = ref([])
const state = ref()


onMounted(async () => {
    // console.log(await axios.get('/user/me/friends', {params: {offset: 0}}));
    let friends = (await axios.get('/users/me/friends', {params: {offset: 0}})).data
    state.value = false
    console.log(friends);
    users.value = friends
})

const addFriend = async (user_id) => {
    await axios.post('/users/me/friend', null, {params: {friend_id: user_id}})
    .then((response) => {
        console.log(response);
    })
    .catch((error) => {
        console.log(error);
    });
}

const deleteFriend = async (user_id) => {
    await axios.delete('/users/me/friend', {params: {friend_id: user_id}})
    .then((response) => {
        console.log(response);
    })
    .catch((error) => {
        console.log(error);
    });
}

const showUsers = async () => {
    await axios.get('/users/all', {params: {offset: 0}})
    .then((response) => {
        state.value = true
        users.value = response.data
    })
}


</script>

<style scoped>
.user-card {
    margin-top: 1rem;
    border-radius: 15px;
    padding: 0.5rem;
    min-width: 300px;
    background-color: var(--items-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
}
button {
    color: var(--text-second-color);
}
a {
    /* height: 100%;
    width: 100%; */
    text-decoration: none;
    border: none;
    display: flex;
    justify-content: center;
    color: var(--text-color);
}
a:hover {
    text-decoration: underline;
}
.buttons-row {
    display: flex;
    gap: 10px;
}
.button-add {
    color: #4fff5d;
    font-size: 30px;
    padding: 0;
    width: 3rem;
    height: 3rem;
}
.button-delete {
    color: #ff4343;
    font-size: 30px;
    padding: 0;
    width: 3rem;
    height: 3rem;
}
</style>

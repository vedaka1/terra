<template>
    <div class="main-page">
        <div class="wrapper">
            <button @click="showUsersAndFriends()">{{ buttonText }}</button>
            <div class="user-card" v-for="user in users" :key="user.id" :id="user.id">
                <RouterLink :to="{name: 'profile', params: {id: user.id}}">
                    {{ user.username }}
                </RouterLink>
                <div class="buttons-row">
                    <button v-if="!user.isFriend" class="button-add" @click="addFriend(user.id)">&plus;</button>
                    <button v-if="user.isFriend" class="button-delete" @click="deleteFriend(user.id)">&Cross;</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';


let showUsersState = false

const users = ref([])
const buttonText = ref('Show all users')
let friends = []


onMounted(async () => {
    // console.log(await axios.get('/user/me/friends', {params: {offset: 0}}));
    await axios.get('/users/me/friends', {params: {offset: 0}})
    .then((response) => {
        friends = response.data
        friends.forEach(user => {
            user.isFriend = true
        });
    })
    users.value = friends
})

const addFriend = async (user_id) => {
    await axios.post('/users/me/friends', null, {params: {friend_id: user_id}})
    .then((response) => {
        document.getElementById(user_id).classList.add('hide-item');
        setTimeout(() => {
            document.getElementById(user_id).style.display = 'none';
        }, 1000);
    })
    .catch((error) => {
        console.log(error);
    });
}

const deleteFriend = async (user_id) => {
    await axios.delete('/users/me/friends/' + user_id)
    .then((response) => {
        document.getElementById(user_id).classList.add('hide-item');
        setTimeout(() => {
            document.getElementById(user_id).style.display = 'none';
        }, 1000);
    })
    .catch((error) => {
        console.log(error);
    });
}

const showUsersAndFriends = async () => {
    showUsersState = !showUsersState
    if (showUsersState) {
        buttonText.value = "Show my friends"
        await axios.get('/users', {params: {offset: 0}})
        .then((response) => {
            let usersData = response.data
            for (let i = usersData.length - 1; i >= 0; i--) {
                const user = usersData[i]
                const found = friends.find(friend => friend.id === user.id);
                if (found) {
                    usersData.splice(i, 1)
                }
            }
            users.value = usersData
        })
    } else {
        buttonText.value = "Show all users"
        await axios.get('/users/me/friends', {params: {offset: 0}})
        .then((response) => {
            friends = response.data
            friends.forEach(user => {
                user.isFriend = true
            });
        })
        users.value = friends
    }
}


</script>

<style scoped>
.wrapper {
    margin-top: 3rem;
    align-items: baseline;
    justify-content: flex-start;
}
.user-card {
    margin-top: 1rem;
    border-radius: 15px;
    padding: 0.5rem;
    width: 100%;
    min-width: 300px;
    background-color: var(--items-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
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
</style>

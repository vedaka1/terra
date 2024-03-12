<template>
    <div class="main-page">
        <div class="wrapper">
            <button @click="showChatForm()">Create new chat</button>
            <div v-if="showForm">
                <input type="text" placeholder="Enter chat name">
            </div>
            <div class="chat-card" v-for="chat in chats" :key="chat.id">
                {{ chat.name }}
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';

// const router = useRouter();
let chats = ref([]);
let showForm = ref(false)


onMounted(async () => {
    await axios.get('/chats')
    .then((response) => {
        chats.value = response.data
        console.log(response.data);
    }, (error) => {
        console.log(error);
    });
});

const showChatForm = async () => {
    showForm.value = true
    console.log(showForm);
}
</script>

<style scoped>
.wrapper {
    margin-top: 3rem;
    justify-content: flex-start;
    /* background-color: var(--items-color); */
    border-radius: 15px;
}
</style>
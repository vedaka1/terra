<template>
    <div class="main-page">
        <div class="wrapper">
            <button @click="ShowCreateChat()" id="showFormButton">{{ buttonText }}</button>
            <div v-show="showForm" class="form-wrapper">
                <input type="text" placeholder="Enter chat name" v-model="chatName">
                <button class="create-btn" @click="createChat()">Create</button>
            </div>
            <div class="chat-card" v-for="chat in chats" :key="chat.id" :id="chat.id">
                <RouterLink :to="{name: 'chat', params: {id: chat.id}}">
                    {{ chat.name }}
                </RouterLink>
                <button class="button-delete" @click="deleteChat(chat.id)">&Cross;</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';

// const router = useRouter();
const buttonText = ref("Create chat")
let chats = ref([]);
let showForm = ref(false);
const chatName = ref('')


onMounted(async () => {
    await axios.get('/chats')
    .then((response) => {
        console.log(response.data);
        chats.value = response.data
    }, (error) => {
        console.log(error);
    });
});

const ShowCreateChat = async () => {
    showForm.value = !showForm.value
    if (showForm.value) {
        buttonText.value = "Back to messages"
        await axios.get('/chats')
        .then((response) => {
            chats.value = response.data
        }, (error) => {
            console.log(error);
        });
    } else {
        buttonText.value = "Create chat"
    }
}

const createChat = async () => {
    await axios.post("/chats", null, {params: {name: chatName.value}})
    .then((response) => {
        showForm.value = !showForm.value
        buttonText.value = "Create chat"
        console.log(response);
    })
    await axios.get('/chats')
    .then((response) => {
        console.log(response.data);
        chats.value = response.data
    }, (error) => {
        console.log(error);
    });
}

const deleteChat = async (chat_id) => {
    await axios.delete("/chats/" + chat_id)
    .then((response) => {
        document.getElementById(chat_id).classList.add('hide-item');
        setTimeout(() => {
            document.getElementById(chat_id).style.display = 'none';
        }, 1000);
        console.log(response);
    })
}
</script>

<style scoped>
.wrapper {
    margin-top: 3rem;
    justify-content: flex-start;
    /* background-color: var(--items-color); */
    border-radius: 15px;
}
.form-wrapper {
    display: flex;
    width: 100%;
    margin-top: 1rem;
    justify-content: center;
    align-items: center;
    gap: 1rem;
}
input {
    width: 50%;
}
.create-btn {
    color: #4fff5d;
}
.chat-card {
    margin-top: 1rem;
    border-radius: 15px;
    padding: 0.5rem;
    width: 100%;
    min-width: 300px;
    background-color: var(--items-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: var(--box-shadow);
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
</style>
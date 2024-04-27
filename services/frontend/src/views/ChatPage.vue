<template>
    <div class="main-page">
        <div class="wrapper">
            <div class="messages-block">
                <Message v-for="message in messages" :key="message.id" :content="message.data"/>
            </div>
            <div class="send-block">
                <input type="text" placeholder="Write message here" v-model="messageText" @keyup.enter="sendMessage()">
                <button class="btn-send" @click="sendMessage()">
                    Send
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
// import axios from 'axios';
import Message from '@/components/Message.vue';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const messages = ref([])
let test = []
const chat_id = useRouter().currentRoute.value.params.id
const messageText = ref('')
const socket = new WebSocket("ws://localhost:5000/chats/ws/" + chat_id)
socket.onmessage = (event) => {
    test.push(event)
    messages.value = test
    console.log(test)
}

onMounted(async () => {
    // await axios.get('/chats/' + chat_id + '/messages', null)
    // .then((response) => {
    //     console.log(response.data);
    //     messages.value = response.data
    // }, (error) => {
    //     console.log(error);
    // });
});

const sendMessage = async () => {
    // await axios.post('/chats/' + chat_id + '/messages', null, {params: {content: messageText.value}})
    // .then((response) => {
    //     console.log(response);
    // })
    socket.send(messageText.value)
}
</script>

<style scoped>
.send-block {
    display: flex;
    width: 100%;
    gap: 1rem;
}
.btn-send {
    width: auto;
}
.wrapper {
    margin-top: 3rem;
    margin-bottom: 1rem;
    justify-content: end;
    background-color: var(--bg-second-color);
    border-radius: 15px;
}
</style>
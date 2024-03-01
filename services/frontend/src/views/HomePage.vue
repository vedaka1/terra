<template>
  <div class="main-page">
    <div class="wrapper">
      <div class="user-info">
        <h2>
          {{ username }}
        </h2>
        
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';

const router = useRouter();
let username = ref("")


onMounted(async () => {
    await axios.get('/users/me')
    .then((response) => {
        username.value = response.data.username
    }, (error) => {
        console.log(error);
        router.push("/login");
    });
})

</script>

<style scoped>
.wrapper {
  background-color: var(--items-color);
  border-radius: 15px;
  margin-top: 3rem;
  align-items: baseline;
  justify-content: flex-start;
}
</style>
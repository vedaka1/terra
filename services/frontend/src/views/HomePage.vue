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
import { ref } from 'vue';
import { onMounted } from 'vue';
import { useAuthStore } from '@/store/auth';

let username = ref("")


onMounted(() => {
  const authStore = useAuthStore();
  username.value = authStore.user.data.username
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
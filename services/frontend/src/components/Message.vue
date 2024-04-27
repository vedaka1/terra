<template>
    <div class="message">
        {{ username }}: {{ content }}
    </div>
</template>

<script setup>
defineProps(['username', 'content'])
</script>


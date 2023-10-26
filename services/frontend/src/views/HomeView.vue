<template>
  <div class="home">
    {{ msg }} test api
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PingP',
  data() {
    return {
        msg: '',
    };
  },
  methods: {
    getMessage() {
        axios.get('/')
        .then((res) => {
            this.msg = res.data;
        })
        .catch((error) => {
            console.log(error)
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

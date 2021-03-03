<template>
  <div class="container">
    <p>{{ msg }}</p>
    <button @click="postMessage()">Click to post</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    postMessage() {
        const path = 'http://localhost:5000/ping'
        axios.post(path, {title: "set up backend"}).then((response) => {
            this.msg = response.data;
        }).catch((error) => {
            console.log(error)
        })
    }
  },
  created() {
    this.getMessage();
  },
};
</script>
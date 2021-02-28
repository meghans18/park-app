<template>
  <div class="home text-center container">
    <div v-if="User">
      <p>Log in successful</p>
    </div>
  <h2>WELCOME TO PARK APP</h2>
  <p>COMING SOON</p>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  name: 'Home',
  components: {
  },
  computed: {
    ...mapGetters({User: "StateUser"}),
  },
}
</script>

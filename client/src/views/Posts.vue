<template>
  <div class="posts">
      <div v-if="User">
        <p>Hello</p>
      </div>
      <div v-else>
        Oh no!!!
      </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: 'Posts',
  components: {
    
  },
  computed: {
    ...mapGetters({User: "StateUser"}),
  },
};
</script>


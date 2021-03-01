<template>
  <div id="home" class="container">
    <div class="row">
      <b-col class="col-12 text-center">
        <div v-if="User">
          <p>Logged in as {{User}}</p>
          <p>WELCOME TO PARK APP</p>
        </div>
      </b-col>
    </div>

    <b-row>
      <b-col class="col-6 text-center">Filters and map side</b-col>
      <b-col class="col-6 text-center">List of spots side</b-col>
    </b-row>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  name: 'Home',
  components: {
  },
  computed: {
    ...mapGetters({User: "getFirstName"}),
  },
}
</script>

<style scoped>

</style>

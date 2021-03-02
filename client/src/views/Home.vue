<template>
  <div id="home" class="container">
    <div class="row">
      <b-col class="col-12 text-center">
        <div v-if="User">
          <b-alert v-model="showAlert" variant="success" dismissible>
            Logged in as {{User}}
          </b-alert>
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
  data() {
    return {
      showAlert: false,
    }
  },
  computed: {
    ...mapGetters({User: "getEmail"}),
  },
  methods: {
    checkShowAlert: function() {
      if (sessionStorage.getItem('show') == null) {
        this.showAlert = true;
        sessionStorage.setItem('show', false)
      } else {
        this.showAlert = false;
      }
    }
  },
  mounted: function() {
    this.checkShowAlert();
  },
}
</script>

<style scoped>

</style>

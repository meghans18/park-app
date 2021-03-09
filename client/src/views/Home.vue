<template>
  <div id="home">
    <div class="row">
      <b-col class="col-12 text-center">
        <div v-if="User">
          <b-alert v-model="showAlert" variant="success" dismissible>
            Logged in as {{User}} with privilege {{Privilege}}
          </b-alert>
        </div>
      </b-col>
    </div>

<div class="row">
      <b-col class="col-6">
        <GoogleMap />
      </b-col>
      <b-col class="col-6">
        List of spots side (COMING SOON)
      </b-col>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import GoogleMap from '@/components/GoogleMap.vue'

export default {
  name: 'Home',
  components: {
    GoogleMap,
  },
  data() {
    return {
      showAlert: false,
    }
  },
  computed: {
    ...mapGetters({User: "getEmail", Privilege: "getPrivilege"}),
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

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

    <div class="row" style="height: 80vh">       
      <b-col class="col-6" style="height: 100%;">
        <google-map :spots="this.spots"></google-map>
      </b-col>
      <b-col class="col-6" style="height: 100%; overflow-y: scroll">
        <spot-list :spots="this.spots"></spot-list>
      </b-col>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import axios from 'axios'
import GoogleMap from '@/components/GoogleMap.vue'
import SpotList from '@/components/SpotList.vue'

export default {
  name: 'Home',
  components: {
    GoogleMap,
    SpotList
  },
  data() {
    return {
      showAlert: false,
      spots: null,
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
    },
    getAllSpots() {
      const path = 'http://localhost:5000/spots';
      axios.get(path).then((response) => {
          this.spots = response.data.spots
      }).catch((error) => {
          console.log(error);
      });
    },
  },
  created: function() {
    this.getAllSpots();
  },
  mounted: function() {
    this.checkShowAlert();
  },
}
</script>

<style scoped>
#home {
  overflow-y:hidden;
  overflow-x: hidden;
}
</style>

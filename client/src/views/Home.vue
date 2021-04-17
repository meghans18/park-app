<template>
  <div id="home">
    <div class="row">
      <b-col class="col-12 text-center">
        <div v-if="User">
          <b-alert v-model="showAlert" variant="success" dismissible>
            Logged in as {{User}}
          </b-alert>
        </div>
      </b-col>
    </div>

    <div class="row" style="height: 80vh">       
      <b-col class="col-6" style="height: 100%;">
        <google-map :spots="this.spots" :center="{ lat: 41.6611, lng: -91.5302 }"></google-map>
      </b-col>
      <b-col class="col-6" style="height: 100%; overflow-y: scroll">
        <div class="row" style="margin: 10px 0px">

          <div class="col-5">
          <input type="date" id="dateInput" min="2021-01-01" value="2021-01-01" @change="onChange">
        </div>

        <div class="col-7">
        <b-input-group 
          size="sm"
          prepend="Zipcode:"
        >
          <b-form-input></b-form-input>
          <b-input-group-append>
            <b-button variant="outline-success">Button</b-button>
          </b-input-group-append>
        </b-input-group>
        </div>

        </div>
          <div v-if="User">
            <spot-list :spots="this.spots" :date="this.date"></spot-list>
          </div>
          <div v-else>
            Please register or sign in to view availablities.
          </div>
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
      date: null,
      zipcode: null
    }
  },
  computed: {
    ...mapGetters({User: "getEmail", Privilege: "getPrivilege"}),
  },
  methods: {
    onChange(e) {
      this.date = e.srcElement.value
      this.getAllSpots();
    },
    minDate() {
      var today = new Date();
      var dd = today.getDate();
      var mm = today.getMonth()+1; //January is 0!
      var yyyy = today.getFullYear();
      if(dd<10){
              dd='0'+dd
          } 
          if(mm<10){
              mm='0'+mm
          } 

      today = yyyy+'-'+mm+'-'+dd;
      this.date = today
      document.getElementById("dateInput").min = today
      document.getElementById("dateInput").value = today
    },
    checkShowAlert: function() {
      if (sessionStorage.getItem('show') == null) {
        this.showAlert = true;
        sessionStorage.setItem('show', false)
      } else {
        this.showAlert = false;
      }
    },
    getAllSpots() {
      const userEmail = this.$store.getters.getEmail
      const path = 'http://localhost:5000/listSpots';
      const payload = {
        'email': userEmail,
        'date': this.date,
        'zipcode': this.zipcode
      }
      axios.post(path, payload).then((response) => {
        // console.log(response)
          this.spots = response.data.spots
      }).catch((error) => {
          console.log(error);
      });
    },
  },
  mounted: function() {
    this.minDate();
    this.checkShowAlert();
    this.getAllSpots();
  },
}
</script>

<style scoped>
#home {
  overflow-y:hidden;
  overflow-x: hidden;
}

input {
  width: 100%;
}
</style>

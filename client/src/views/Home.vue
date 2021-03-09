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
        <GoogleMap />
      </b-col>
      <b-col class="col-6" style="height: 100%; overflow-y: scroll">
        <SpotList />
      </b-col>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import GoogleMap from '@/components/GoogleMap.vue'
import SpotList from '@/components/SpotList.vue'

export default {
  name: 'Home',
  components: {
    GoogleMap,
    SpotList,
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
#home {
  overflow-y:hidden;
  overflow-x: hidden;
}
</style>

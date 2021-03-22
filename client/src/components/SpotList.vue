<template>
    <div id="spotList">
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Spot Address</th>
              <th scope="col">List Price</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="spot in spots" :key="spot.id">
              <td>{{spot.addressNum}} {{spot.street}}, {{spot.city}}, {{spot.state}} {{spot.zipcode}}</td>
              <td>${{spot.price}}/per day</td>
              <td>
                <div class="btn-group" role="group">
                  <!-- check if user logged in and change button accordingly -->
                  <span v-if="isLoggedIn"><button type="button" class="btn btn-success btn-md">Rent Spot</button></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'SpotList',
    computed: {
      isLoggedIn : function(){ return this.$store.getters.isAuthenticated},
    },
    data() {
        return {
            spots: null,
        }
    },
    methods: {
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
    }
}
</script>

<style scoped>

</style>
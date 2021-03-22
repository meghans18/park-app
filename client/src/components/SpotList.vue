<template>
    <div id="spotList">
        <p>List of available spots</p>
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
export default {
    name: 'SpotList',
    computed: {
      isLoggedIn : function(){ return this.$store.getters.isAuthenticated},
    },
    data() {
        return {
            spots: [
                {
                    id: 1,
                    addressNum: 1,
                    street: 'Davenport St',
                    city: 'Grundy Center',
                    state: 'Iowa',
                    zipcode: 50613,
                    price: 300
                },
                {
                    id: 2,
                    addressNum: 239,
                    street: 'Rainbow Ave',
                    city: 'Coralville',
                    state: 'Illinois',
                    zipcode: 52245,
                    price: 129
                },
            ],
        }
    }
}
</script>

<style scoped>

</style>
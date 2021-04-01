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
                  <span v-if="isLoggedIn"><button type="button" class="btn btn-success btn-md" @click="submit(spot.id)">View Spot</button></span>
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
    props: ['spots'],
    methods: {
      submit(el) {
        this.$router.push({name: 'Spot Info', params: { spot_id: el } })
        // window.location = "https://www.google.com"
      }
    }
}
</script>

<style scoped>

</style>
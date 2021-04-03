<template>
  <div>
    <div>
      <!-- <label>
        <gmap-autocomplete
          @place_changed="setPlace">
        </gmap-autocomplete>
        <button @click="addMarker">Add</button>
      </label> -->
      <!-- <br/> -->
      <!-- <tr v-for="spot in spots" :key="spot.id">
        <td>setPlace({{spot.latitude}}{{spot.longitude}}), addMarker</td>
      </tr> -->
    </div>
    <br>
    <GmapMap
      :center="center"
      :zoom="12"
      style="width: 100%; height: 75vh"
    >
      <GmapMarker
        v-for="spot in spots"
        :key="spot.id"
        :position="getPosition(spot)"
        :clickable="true"
        @click="openInfo(spot.id)"
      ></GmapMarker>
    </GmapMap>
  </div>
</template>

<script>
export default {
  name: "GoogleMap",
  props: ['spots', 'center'],
  data() {
    return {
      // default to Iowa City
      // center: { lat: 41.6611, lng: -91.5302 },
      markers: [],
      places: [],
      currentPlace: null
    };
  },
  methods: {
    // receives a place object via the autocomplete component
    setPlace(place) {
      this.currentPlace = place;
    },
    openInfo(spotID) {
      if (this.$store.getters.getEmail) {
        this.$router.push({name: 'Spot Info', params: { spot_id: spotID }});
      }
    },
    getPosition: function(spot) {
      return {
        lat: parseFloat(spot.latitude), 
        lng: parseFloat(spot.longitude)
      }
    },
  }
};
</script>

<style scoped>
</style>
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
      style="width: 100%; height: 100vh"
    >
      <GmapMarker
        v-for="spot in spots"
        :key="spot.id"
        :position="getPosition(spot)"
        @click="center=spot.position"
      ></GmapMarker>
    </GmapMap>
  </div>
</template>

<script>
export default {
  name: "GoogleMap",
  props: ['spots'],
  data() {
    return {
      // default to Iowa City
      center: { lat: 41.6611, lng: -91.5302 },
      markers: [],
      places: [],
      currentPlace: null
    };
  },
  mounted() {
    this.geolocate();
  },
  methods: {
    // receives a place object via the autocomplete component
    setPlace(place) {
      this.currentPlace = place;
    },
    addMarker() {
      if (this.currentPlace) {
        const marker = {
          lat: this.currentPlace.geometry.location.lat(),
          lng: this.currentPlace.geometry.location.lng()
        };
        this.markers.push({ position: marker });
        this.places.push(this.currentPlace);
        this.center = marker;
        this.currentPlace = null;
      }
    },
    getPosition: function(spot) {
      return {
        lat: parseFloat(spot.latitude), 
        lng: parseFloat(spot.longitude)
      }
    },
    geolocate: function() {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      });
    }
  }
};
</script>

<style scoped>
</style>
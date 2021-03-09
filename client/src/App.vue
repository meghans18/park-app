<template>
  <div id="app">
    <div id="top-bar" class="container-fluid">
      <b-row class="row" align-v="center">
      <b-col class="col-6">
        <img src="@/assets/ParkYellow.png" width="100px" height="100px" align="left"/>
      </b-col>
      <b-col class="col-6">
        <NavBar />
      </b-col>
      </b-row>
    </div>

    <div class="container-fluid">
    <router-view/>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue'
export default {
  components: {
    NavBar
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  overflow-x: hidden;
}
#top-bar {
  margin-top: 25px;
  margin-bottom: 20px;
  padding-left: 40px;
}
</style>

<template>
  <div id="app container">
    <b-row id="top-bar" class="row" align-v="center">
      <b-col class="col-6">
        <img src="@/assets/fake-logo.png" width="100px" height="100px"/>
      </b-col>
      <b-col class="col-6">
        <NavBar />
      </b-col>
    </b-row>

    <div class="row">
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
}
#top-bar {
  margin-top: 20px;
  padding-left: 20px;
}
</style>

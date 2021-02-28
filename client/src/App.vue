<template>
  <div id="app container">
    <div class="row">
      <router-view/>
    </div>
    <div class="row">
      <div class="col-6">
        <p>Filters and map side</p>
      </div>
      <div class="col-6 text-right">
        <NavBar />
      </div>
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
</style>

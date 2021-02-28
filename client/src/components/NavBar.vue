<template>
  <div id="nav">
    <b-nav>
      <b-nav-item><router-link to="/">Home</router-link></b-nav-item>
        <b-nav-item v-if="isLoggedIn"><a @click="logout">Logout</a></b-nav-item>
        <b-nav-item><router-link to="/register">Register</router-link></b-nav-item>
        <b-nav-item><router-link to="/login">Login</router-link></b-nav-item>
    </b-nav>
  </div>
</template>
<script>
export default {
  name: 'NavBar',
  computed : {
      isLoggedIn : function(){ return this.$store.getters.isAuthenticated}
    },
    methods: {
      async logout (){
        await this.$store.dispatch('LogOut')
        this.$router.push('/login')
      }
    },
}
</script>
<style>
#nav a {
  font-weight: bold;
  color: rgb(46, 46, 46);
  text-decoration: none;
}
a:hover {
  cursor: pointer;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

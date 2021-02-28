<template>
  <div id="nav">
    <b-button><router-link to="/">Home</router-link></b-button>
    <span v-if="isLoggedIn">
      <b-button><a @click="logout">Logout</a></b-button>
    </span>
    <span v-else>
      <b-button><router-link to="/register">Register</router-link></b-button>
      <b-button><router-link to="/login">Login</router-link></b-button>
    </span>
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
button {
  margin: 5px !important;
}
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

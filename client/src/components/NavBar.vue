<template>
  <div id="nav">
    <!-- this is for regular privilege for now -->
    <span v-if="isLoggedIn">
      <span v-if="userPrivilege=='regular'">
        <b-nav align="right">
          <b-nav-item><router-link to="/map-home">Home</router-link></b-nav-item>
          <b-nav-item><router-link to="/manage-spots-owned">Add Spots</router-link></b-nav-item>
          <b-nav-item><router-link to="/rented-spots">Reservations</router-link></b-nav-item>
          <b-nav-item><router-link to="/register-vehicle">Vehicles</router-link></b-nav-item>
          <b-nav-item><router-link to="/faq">FAQs</router-link></b-nav-item>
          <b-nav-item><a @click="logout">Logout</a></b-nav-item>
        </b-nav>
      </span>
      <span v-if="userPrivilege=='admin'">
        <b-nav align="right">
          <b-nav-item><router-link to="/manage-users">Manage Users</router-link></b-nav-item>
          <b-nav-item><a @click="logout">Logout</a></b-nav-item>
        </b-nav>
      </span>
      <span v-if="userPrivilege=='towing'">
        <b-nav align="right">
          <b-nav-item><router-link to="/manage-spots">Reservation Information</router-link></b-nav-item>
          <b-nav-item><a @click="logout">Logout</a></b-nav-item>
        </b-nav>
      </span>
    </span>
    <!-- can check for permissions eventually to display different navs for different user levels -->
    <span v-else>
      <b-nav align="right">
        <b-nav-item><router-link to="/">Home</router-link></b-nav-item>
        <b-nav-item><router-link to="/register">Register</router-link></b-nav-item>
        <b-nav-item><router-link to="/login">Login</router-link></b-nav-item>
      </b-nav>
    </span>
  </div>
</template>
<script>
export default {
  name: 'NavBar',
  computed : {
      isLoggedIn : function(){ return this.$store.getters.isAuthenticated},
      userPrivilege: function(){ return this.$store.getters.getPrivilege },
    },
    methods: {
      async logout (){
        sessionStorage.clear();
        this.$store.dispatch('logOut')
        this.$router.push('/')
      }
    },
}
</script>
<style>
#nav {
  margin-right: 50px;
  font-size: 1.1em;
}
#nav a {
  color: rgb(46, 46, 46);
  text-decoration: none;
}
a:hover {
  cursor: pointer;
}
#nav a.router-link-exact-active {
  color: #0a814c;
}
</style>

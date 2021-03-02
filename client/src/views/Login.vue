<template>
  <div class="login container">
    <div class="text-center">
      <p>Login to Park</p>
    </div>
    <b-form @submit.prevent="submit">
      <b-form-group
        id="input-group-1"
        label="Email:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="text"
          placeholder="Enter your email:"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2"
        label="Password:"
        label-for="input-2"
      >
        <b-form-input
          id="input-2"
          v-model="form.password"
          type="password"
          required
        ></b-form-input>
      </b-form-group>

      <b-button variant="success" type="submit">Submit</b-button>
    </b-form>

  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  components: {},
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      showError: false
    };
  },
  methods: {
    ...mapActions(["logIn"]),
    checkUser(payload) {
      //const path = "http://localhost:5000/login";
      //use the same format as register
      //post to path and then make sure no errors were returned
      //need to check if payload exists in database on backend side
      this.logIn(payload); //sends to auth.js
      this.$router.push("/");
    },
    submit() {
      sessionStorage.clear()
      //get data from back end to set email, first name, and last name on auth state
      //need to send to back end
      const payload = {
        email: this.form.email,
        password: this.form.password
      }
      this.checkUser(payload);
    },
  },
};
</script>

<style scoped>
p {
  color: #0a814c;
  font-size: 2em;
}
</style>


<template>
  <div class="login container text-left">
    <div class="text-center">
      <p>Login to Park</p>
    </div>

    <b-alert v-model="showError" variant="danger" dismissible>
      {{errorMessage}}
    </b-alert>

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
import axios from 'axios'

export default {
  name: "Login",
  components: {},
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      showError: false,
      errorMessage: '',
    };
  },
  methods: {
    ...mapActions(["logIn"]),
    checkUser(payload) {
      const path = "http://localhost:5000/login";
      axios.post(path, payload).then((response) => {
        if (response.data.status == 'failed') { 
          this.resetForm();
          this.showError = true;
          this.errorMessage = response.data.message
        } else {
          payload.privilege = response.data.privilege
          payload.connected = response.data.connected
          this.logIn(payload); //sends to auth.js
          this.$router.push("/map-home")
        }
      }).catch((error) => {
        console.log(error);
        this.$router.push("/")
      });
    },
    submit() {
      sessionStorage.clear()
      const payload = {
        email: this.form.email,
        password: this.form.password
      }
      this.checkUser(payload);
    },
    resetForm() {
      this.form.email = ''
      this.form.password = ''
    }
  },
};
</script>

<style scoped>
p {
  color: #0a814c;
  font-size: 2em;
}
</style>


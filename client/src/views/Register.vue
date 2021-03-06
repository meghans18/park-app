<template>
  <div class="register container">
    <div class="text-center">
      <p>Welcome to Park</p>
    </div>

    <b-alert v-model="showError" variant="danger" dismissible>
      Email already in use!
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
          type="email"
          placeholder="Enter your email:"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2"
        label="First Name:"
        label-for="input-2"
      >
        <b-form-input
          id="input-2"
          v-model="form.first_name"
          type="text"
          placeholder="Enter your first name:"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-3"
        label="Last Name:"
        label-for="input-3"
      >
        <b-form-input
          id="input-3"
          v-model="form.last_name"
          type="text"
          placeholder="Enter your last name:"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-4"
        label="Password:"
        label-for="input-4"
      >
        <b-form-input
          id="input-4"
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
  name: "Register",
  components: {},
  data() {
    return {
      form: {
        email: "",
        first_name: "",
        last_name: "",
        password: "",
      },
      showError: false
    };
  },
  methods: {
    ...mapActions(["logIn"]),
    addUser(payload) {
      const path = 'http://localhost:5000/register';
      axios.post(path, payload).then((response) => {
        console.log(response.data.status)
        if (response.data.status == 'failed') { 
          this.resetForm();
          this.showError = true;
        } else {
          this.logIn(payload); //sends to auth.js
          this.$router.push("/")
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
        first_name: this.form.first_name,
        last_name: this.form.last_name,
        password: this.form.password
      };
      this.addUser(payload);
    },
    resetForm() {
      this.form.email = ''
      this.form.first_name = ''
      this.form.last_name = ''
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
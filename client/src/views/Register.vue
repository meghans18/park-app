<template>
  <div class="register container">
    <div class="text-center">
      <p>Welcome to Park</p>
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
          type="email"
          placeholder="Enter email:"
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
          required
        ></b-form-input>
      </b-form-group>

      <b-button variant="success" type="submit">Submit</b-button>
    </b-form>
    <p v-if="showError" id="error">Username already exists</p>
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
      },
      showError: false
    };
  },
  methods: {
    ...mapActions(["register"]),
    addUser(payload) {
      const path = 'http://localhost:5000/register';
      axios.post(path, payload).then((response) => {
        console.log(response)
        this.register(payload);
        this.$router.push("/")
      }).catch((error) => {
        console.log(error);
      });
    },
    submit() {
      const payload = {
        email: this.form.email,
        first_name: this.form.first_name,
        last_name: this.form.last_name
      };
      this.addUser(payload);
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
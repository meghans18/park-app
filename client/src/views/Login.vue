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
    ...mapActions(["LogIn"]),
    async submit() {
      //get data from back end to set email, first name, and last name on auth state
      //need to send to back end
      console.log(JSON.stringify(this.form))
      this.reset();
      this.$router.push("/");
    },
    reset() {
      this.form.username = ''
      this.form.password = ''
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


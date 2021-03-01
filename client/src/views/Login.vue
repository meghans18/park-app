<template>
  <div class="login container">
    <div class="text-center">
      <p>Login to Park</p>
    </div>
    <b-form @submit.prevent="submit">
      <b-form-group
        id="input-group-1"
        label="Username:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.username"
          type="text"
          placeholder="Enter username:"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2"
        label="Password:"
        label-for="input-2"
        description="Must be 12 characters."
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
        username: "",
        password: "",
      },
      showError: false
    };
  },
  methods: {
    ...mapActions(["LogIn"]),
    async submit() {
      // const User = new FormData();
      // User.append("username", this.form.username);
      // User.append("password", this.form.password);
      // try {
      //     await this.LogIn(User);
      //     this.$router.push("/");
      //     this.showError = false
      // } catch (error) {
      //   this.showError = true
      // }
      
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


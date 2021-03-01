<template>
  <div class="register container">
    <div class="text-center">
      <p>Welcome to Park</p>
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
        label="Full Name:"
        label-for="input-2"
      >
        <b-form-input
          id="input-2"
          v-model="form.full_name"
          type="text"
          placeholder="Enter your full name:"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-3"
        label="Password:"
        label-for="input-3"
        description="Must be 12 characters."
      >
        <b-form-input
          id="input-3"
          v-model="form.password"
          type="password"
          required
        ></b-form-input>
      </b-form-group>

      <b-button variant="success" type="submit">Submit</b-button>
    </b-form>


      <!-- <div>
          <form @submit.prevent="submit">
            <div>
              <label for="username">Username:</label>
              <input type="text" name="username" v-model="form.username">
            </div>
            <div>
              <label for="full_name">Full Name:</label>
              <input type="text" name="full_name" v-model="form.full_name">
            </div>
            <div>
              <label for="password">Password:</label>
              <input type="password" name="password" v-model="form.password">
            </div>
            <button type="submit"> Submit</button>
          </form>
      </div> -->
      <p v-if="showError" id="error">Username already exists</p>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Register",
  components: {},
  data() {
    return {
      form: {
        username: "",
        full_name: "",
        password: "",
      },
      showError: false
    };
  },
  methods: {
    ...mapActions(["Register"]),
    async submit() {
      // try {
      //   await this.Register(this.form);
      //   this.$router.push("/");
      //   this.showError = false
      // } catch (error) {
      //   this.showError = true
      // }
      console.log(JSON.stringify(this.form))
      this.$router.push("/")
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
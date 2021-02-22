<template>
  <div class="register">
      <div>
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
      </div>
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
      try {
        await this.Register(this.form);
        this.$router.push("/posts");
        this.showError = false
      } catch (error) {
        this.showError = true
      }
    },
  },
};
</script>

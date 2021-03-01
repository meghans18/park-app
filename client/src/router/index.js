import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register";
import Login from "../views/Login";

import Ping from "../components/Ping.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

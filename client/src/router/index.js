import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register";
import Login from "../views/Login";
import RentedSpots from '../views/RentedSpots'
import ManageUsers from '../views/ManageUsers'
import SpotInfo from '../components/SpotInfo'
import ManageSpotsOwned from '../views/ManageSpotsOwned'
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
    path: "/rented-spots",
    name: "Rented Spots",
    component: RentedSpots,
  },
  {
    path: '/manage-users',
    name: 'Manage Users',
    component: ManageUsers,
  },
  {
    path: '/manage-spots-owned',
    name: 'Manage Spots Owned',
    component: ManageSpotsOwned
  },
  {
    path: '/spot-info/:spot_id', //add dates selected eventually?
    name: 'Spot Info',
    component: SpotInfo,
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

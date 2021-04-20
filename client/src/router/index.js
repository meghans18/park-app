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
import Return from "../components/Return"
import Refresh from "../components/Refresh"
import Success from "../components/Success"
import Failure from "../components/Failure"
import MapHome from "../views/MapHome"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: '/map-home',
    name: "Map Home",
    component: MapHome,
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
    path: '/spot-info/:spot_id/:date', //add dates selected eventually?
    name: 'Spot Info',
    component: SpotInfo,
  },
  {
    path: '/return',
    name: 'Return',
    component: Return,
  },
  {
    path: '/refresh',
    name: 'Refresh',
    component: Refresh,
  },
  {
    path: '/success',
    name: 'Success',
    component: Success,
  },
  {
    path: '/failure',
    name: 'Failure',
    component: Failure,
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

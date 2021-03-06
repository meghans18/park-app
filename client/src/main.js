import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
import store from './store'
import  * as VueGoogleMaps from 'vue2-google-maps'
// import axios from 'axios'

// need to change to our python app's URL, this is just to check login functionality
// axios.defaults.baseURL = 'https://gabbyblog.herokuapp.com/';

// axios.interceptors.response.use(undefined, function (error) {
//   if (error) {
//     const originalRequest = error.config;
//     if (error.response.status === 401 && !originalRequest._retry) {
  
//         originalRequest._retry = true;
//         store.dispatch('LogOut')
//         return router.push('/login')
//     }
//   }
// })

Vue.use(BootstrapVue);

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyCVpzYXhFftDEmOI6qUVVefm0QhjDV5PCE', // API key
    libraries: 'places', // used for places input
  },
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

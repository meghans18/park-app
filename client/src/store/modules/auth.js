import axios from 'axios';
const state = {
    email: '',
    first_name: '',
    last_name: '',
};
const getters = {
    isAuthenticated: state => !(state.email==null) && !(state.first_name==null) && !(state.last_name==null),
    getFirstName: state => state.first_name,
    getLastName: state => state.last_name,
    getEmail: state => state.email,

};
const actions = {
    async register({commit}, form) {
        await commit('setUser', form)
    },
    async LogIn({commit}, userData) {
        await axios.post('login', userData);
        await commit('setUser', userData)
    },
    async logOut({commit}){
        commit('logOut')
    }
};
const mutations = {
    setUser(state, userData){
        state.email = userData.email
        state.first_name = userData.first_name
        state.last_name = userData.last_name
    },
    logOut(state){
        state.email = null
        state.first_name = null
        state.last_name = null
    },
};
export default {
  state,
  getters,
  actions,
  mutations
};
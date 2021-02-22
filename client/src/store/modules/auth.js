import axios from 'axios';
const state = {
    user: null,
};
const getters = {

};
const actions = {
    async Register({dispatch}, form) {
        await axios.post('register', form)
        let UserForm = new FormData()
        UserForm.append('username', form.username)
        UserForm.append('password', form.password)
        await dispatch('LogIn', UserForm)
    },
    async LogIn({commit}, User) {
        await axios.post('login', User)
        await commit('setUser', User.get('username'))
    },
    async LogOut({commit}){
        let user = null
        commit('logOut', user)
    }
};
const mutations = {
    setUser(state, username){
        state.user = username
    },
    logOut(state){
        state.user = null
    },
};
export default {
  state,
  getters,
  actions,
  mutations
};
const state = {
    email: null,
};
const getters = {
    isAuthenticated: state => !(state.email==null),
    getEmail: state => state.email,
};
const actions = {
    async logIn({commit}, userData) {
        await commit('setUser', userData)
    },
    async logOut({commit}){
        commit('logOut')
    }
};
const mutations = {
    setUser(state, userData){
        state.email = userData.email
    },
    logOut(state){
        state.email = null
    },
};
export default {
  state,
  getters,
  actions,
  mutations
};
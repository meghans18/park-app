const state = {
    email: null,
    privilege: null,
};
const getters = {
    isAuthenticated: state => !(state.email==null),
    getEmail: state => state.email,
    getPrivilege: state => state.privilege,
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
        state.privilege = userData.privilege
    },
    logOut(state){
        state.email = null,
        state.privilege = null
    },
};
export default {
  state,
  getters,
  actions,
  mutations
};
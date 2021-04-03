const state = {
    email: null,
    privilege: null,
    connected: 'no',
};
const getters = {
    isAuthenticated: state => !(state.email==null),
    getEmail: state => state.email,
    getPrivilege: state => state.privilege,
    getConnection: state => state.connected,
};
const actions = {
    async logIn({commit}, userData) {
        await commit('setUser', userData)
    },
    async logOut({commit}){
        commit('logOut')
    },
    async connect({commit}, status) {
        await commit('connect', status)
    }
};
const mutations = {
    setUser(state, userData){
        state.email = userData.email
        state.privilege = userData.privilege
        state.connected = userData.connected
    },
    logOut(state){
        state.email = null,
        state.privilege = null
        state.connected = null
    },
    connect(state, status) {
        state.connected = status.connected
    }
};
export default {
  state,
  getters,
  actions,
  mutations
};
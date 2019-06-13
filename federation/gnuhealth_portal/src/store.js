import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    credentials: {
        thalamus_server: '',
        fedacct: '',
        password: ''
    },
    authenticated: false,

    country_code: 'ESP'
},

  mutations: {
      set_credentials (state, login_info) {
          state.credentials.thalamus_server = login_info.thalamus_server;
          state.credentials.fedacct = login_info.federation_acct;
          state.credentials.password = login_info.password;
          state.authenticated = true;
    },
      reset_credentials (state) {
          state.credentials.fedacct = '';
          state.credentials.password = '';
          state.authenticated = false;

      }

  },

  actions: {

  }
})

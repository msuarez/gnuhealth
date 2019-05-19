import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    credentials: {
        fedacct: '',
        password: ''
    },
    authenticated: false
        
  },
  mutations: {
      set_credentials (state, login_info) {
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

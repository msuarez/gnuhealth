import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VeeValidate from 'vee-validate'

// Form validation support
Vue.use(VeeValidate)

Vue.config.productionTip = false

// Add global objects
Vue.prototype.$default_thalamus_server = 'http://localhost:5000'

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

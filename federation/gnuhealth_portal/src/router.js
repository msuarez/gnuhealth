import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home.vue'
import Login from "./components/Login.vue"
import Workplace from "./components/Workplace.vue"
import Demographics from "./components/Demographics.vue"
import Accounts from "./components/Accounts.vue"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },

    {
      path: '/login',
      name: 'login',
      component: Login
    },

    {
      path: '/workplace',
      name: 'workplace',
      component: Workplace
    },

    {
      path: '/demographics',
      name: 'demographics',
      component: Demographics
    },

    {
      path: '/accounts',
      name: 'accounts',
      component: Accounts
    },

    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './components/About.vue')
    }
  ]
})

import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home.vue'
import LoginComponent from "./components/Login.vue"
import WorkplaceComponent from "./components/Workplace.vue"

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
      component: LoginComponent
    },

    {
      path: '/workplace',
      name: 'workplace',
      component: WorkplaceComponent
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

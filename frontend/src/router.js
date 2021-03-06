import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Abort from './views/About.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { title: 'カメラ映像' }
    },
    {
      path: '/about',
      name: 'about',
      component: Abort,
      meta: { title: 'アバウト' }
    }
  ]
})

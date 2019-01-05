import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import People from './views/People.vue'
import Partner from './views/Partner.vue'
import Join from './views/Join.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/partner',
      name: 'partner',
      component: Partner
    },
    {
      path: '/people',
      name: 'people',
      component: People
    },
    {
      path: '/join',
      name: 'join',
      component: Join
    }

  ]
})

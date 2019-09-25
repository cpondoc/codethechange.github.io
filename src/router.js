import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import People from './views/People.vue'
import Partner from './views/Partner.vue'
import Projects from './views/Projects.vue'
import Join from './views/Join.vue'
import ProjectProfile from './views/ProjectProfile.vue'
import PartnerCriteria from './views/PartnerCriteria.vue'
import WaysToContribute from './views/WaysToContribute.vue'

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
      path: '/projects',
      name: 'projects',
      component: Projects
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
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProjectProfile
    },
    {
      path: '/partner_criteria',
      name: 'partner_criteria',
      component: PartnerCriteria
    },
    {
      path: '/ways_to_contribute',
      name: 'ways_to_contribute',
      component: WaysToContribute
    }
  ]
})

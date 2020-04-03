import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueScrollTo from 'vue-scrollto'
import VueShowdown from 'vue-showdown'

Vue.use(VueShowdown, {
  flavor: 'github'
})

Vue.config.productionTip = false
Vue.use(VueScrollTo)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

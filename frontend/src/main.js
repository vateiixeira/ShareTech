import Vue from 'vue'
import App from './App.vue'
import Vuelidate from 'vuelidate'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueCookie from 'vue-cookie'


// Tell Vue to use the plugin
Vue.use(VueCookie);


Vue.config.productionTip = false

Vue.use(Vuelidate)
Vue.use(VueAxios, axios)




new Vue({  
  render: h => h(App),
}).$mount('#app')

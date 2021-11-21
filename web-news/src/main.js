import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap-vue'
import '../HTML/assets/scss/app.scss'
import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts)
Vue.config.productionTip = false
Vue.use(BootstrapVue)
new Vue({
  render: h => h(App),
}).$mount('#app')

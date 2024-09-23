import './assets/css/satoshi.css'
import './assets/css/style.css'
import 'jsvectormap/dist/jsvectormap.min.css'
import 'flatpickr/dist/flatpickr.min.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import VueApexCharts from 'vue3-apexcharts'
import Toast, { PluginOptions } from "vue-toastification";
// Import the CSS or use your own!
import "vue-toastification/dist/index.css";

import App from './App.vue'
import router from './router'

const options: PluginOptions = {
    // You can set your default options here
};
const app = createApp(App)
const pinia = createPinia();
app.use(pinia)
app.use(router)
app.use(VueApexCharts)
app.use(Toast, options);
app.mount('#app')

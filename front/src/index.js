import Vue from 'vue';
import App from './components/App.vue';
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import store from "./store/store";
import { library } from '@fortawesome/fontawesome-svg-core';
import { faUserShield,faWindowClose,faEye,faClock, faPortrait,faMobileAlt,faBan } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faUserShield);
library.add(faWindowClose);
library.add(faEye);
library.add(faClock);
library.add(faPortrait);
library.add(faMobileAlt);
library.add(faBan);

Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.use(BootstrapVue);
Vue.use(store);


new Vue({
	store,
	  render: h => h(App),
}).$mount('#app');
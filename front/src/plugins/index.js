/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */


// Plugins

import axios from 'axios';
import { loadFonts } from './webfontloader';
import Vue3Toastify from 'vue3-toastify';

import vuetify from './vuetify';
import router from '../router';

import { i18n } from './i18n';
import store from '@/store/index'

import 'vue3-toastify/dist/index.css';

export function registerPlugins (app) {
  loadFonts();
  app
    .use(vuetify)
    .use(i18n)
    .use(router)
    .use(store)
    .use(Vue3Toastify, {
      autoClose: 3000,
      theme: "light"
    })
    ;
  app.config.globalProperties.$axios = axios;
}

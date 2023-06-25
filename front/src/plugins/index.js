/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */


// Plugins

import axios from 'axios';
import { loadFonts } from './webfontloader';
import vuetify from './vuetify';
import router from '../router';

import { i18n } from './i18n';
import store from '@/store/index'

export function registerPlugins (app) {
  loadFonts();
  app
    .use(vuetify)
    .use(i18n)
    .use(router)
    .use(store);
  app.config.globalProperties.$axios = axios;
}

import { createStore } from 'vuex';

const getCookie = (name) => {
  return document.cookie.split('; ').reduce((r, v) => {
    const parts = v.split('=')
    return parts[0] === name ? decodeURIComponent(parts[1]) : r
  }, '')
}

let init_login = false;
let access_token = getCookie("access_token");
if(access_token)
  init_login = true;
let init_lang = getCookie("lang") || "ko";

const store = createStore({
  state : {
    snackbar: {
      isShow: false,
      body: "", timeout:5000,
    },
    login: init_login,
    loginDialog: false,
    serverRequestDict: {},
    lang: init_lang
  },
  mutations: { // 동기작업
    showSnackbar(state, body, timeout){
      if(!timeout)  timeout = -1;  // -1 for indefinitely
      state.snackbar = {
        isShow: true,
        body,
        timeout,
      };
    },
    hideSnackbar(state){
      state.snackbar = {
        isShow: false,
        body: "", timeout:5000,
      };
    },
    changeVisibleLoginDialog(state, show){
      state.loginDialog = show;
    },
    changeLogin(state, login){
      state.login = login;
    },
    addLoadingKey(state, key){
      state.serverRequestDict[key] = true;
    },
    removeLoadingKey(state, key){
      if(state.serverRequestDict.hasOwnProperty(key)){
        delete state.serverRequestDict[key];
      }

    },
    changeLang(state, lang){
      state.lang = lang;
    },
  },
  action: { // 비동기 작업

  },
  getters: {
    isSnackbarShow: (state) => {
      return state.snackbar.isShow;
    },
    isLoginDialogShow: (state) => {
      return state.loginDialog;
    },
    getSnackbarBody: (state) => { 
      return state.snackbar.body;
    },
    isLogin: (state) => {
      return state.login;
    },
    isShowLoadingModal: (state) => {
      return Object.keys(state.serverRequestDict).length > 0;
    },
    getLang: (state) => {
      return state.lang;
    },
  },
});

export default store;

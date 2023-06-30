import { createStore } from 'vuex';

let init_login = false;
let access_token = sessionStorage.getItem("access_token");
if(access_token)
  init_login = true;

const store = createStore({
  state : {
    snackbar: {
      isShow: false,
      body: "", timeout:5000,
    },
    login: init_login,
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
    changeLogin(state, login){
      state.login = login;
    },
  },
  action: { // 비동기 작업

  },
  getters: {
    isSnackbarShow: (state) => {
      return state.snackbar.isShow;
    },
    getSnackbarBody: (state) => { 
      return state.snackbar.body;
    },
    isLogin: (state) => {
      return state.login;
    },
  },
});

export default store;

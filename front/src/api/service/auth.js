import {$axios, param2formdata} from "@/api/service/request"

// https://stackoverflow.com/a/38699214
const setCookie = (name, value, hours = 2, path = '/') => {
  const expires = new Date(Date.now() + hours * 24 * 24 * 60 * 60 * 1000).toUTCString()
  document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=' + path
}

class Auth{
  login(username, password){
    let param = {username, password};
    let data = param2formdata(param);
    return $axios({
      method: 'post',
      url: '/auth/login',
      data
    });
  }
  
  setLoginToken(access_token){
    // sessionStorage.setItem("access_token", access_token);
    setCookie("access_token", access_token);
  }
}
export let auth = new Auth();

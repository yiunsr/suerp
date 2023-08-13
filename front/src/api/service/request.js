import axios from 'axios';
import store from '@/store/index'

// https://stackoverflow.com/a/38699214
const getCookie = (name) => {
  return document.cookie.split('; ').reduce((r, v) => {
    const parts = v.split('=')
    return parts[0] === name ? decodeURIComponent(parts[1]) : r
  }, '')
}

const headers = {
  'X-Requested-With': 'XMLHttpRequest',
  'Content-Type': 'multipart/form-data;charset=UTF-8',
};
const $axios = axios.create(headers);
$axios.interceptors.request.use((config) => {
  let accessToken = getCookie("access_token");
  if(config.headers && accessToken){
    config.headers.Authorization = `Bearer ${accessToken}` 
  }
  return config;
});
$axios.interceptors.response.use(
  (res) => {
    if (!(res.status === 200 || res.status === 201 || res.status === 204))
      throw new Error();
    if (res.data.errors) throw new Error(res.data.errors);
    return res;
  },
  (error) => {
    if(error.response.status == 401){
      store.commit('changeVisibleLoginDialog', true);
      return Promise.reject(error);
    }
    console.log(error.response.data.errors);
    return Promise.reject(error);
  }
);



export {$axios}

function param2formdata(params){
  let formData = new FormData();
  for (var key in params){
    let value = params[key];
    if(Array.isArray(value) === false){
      formData.append(key, value);
      continue;
    }
    for(const value_item of value) {
      formData.append(key, value_item);
    }
  }
  return formData;
}
export {param2formdata}

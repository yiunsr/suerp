import axios from 'axios';

const headers = {
  'X-Requested-With': 'XMLHttpRequest',
  'Content-Type': 'multipart/form-data;charset=UTF-8',
};
const $axios = axios.create(headers);
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
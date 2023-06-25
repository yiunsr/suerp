import {$axios, param2formdata} from "@/api/service/request"

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
  
}
export let auth = new Auth();
import {$axios, param2formdata} from "@/api/service/request"

class Users{
  list(skip=0, limit=50){
    let param = {skip, limit};
    let data = param2formdata(param);
    return $axios({
      method: 'get',
      url: '/api/users/',
      data
    });
  }
  
}
export let users = new Users();

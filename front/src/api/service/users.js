import {$axios, param2formdata} from "@/api/service/request"

class Users{
  list(filters, sort, skip=0, limit=50){
    let params = {...filters, sort, skip, limit,};
    return $axios({
      method: 'get',
      url: '/api/users/',
      params
    });
  }
  
}
export let users = new Users();

import {$axios, param2formdata} from "@/api/service/request"

class Users{
  list(filters, sort, page=1, limit=50){
    let params = {...filters, sort, page, limit,};
    return $axios({
      method: 'get',
      url: '/api/users/',
      params
    });
  }

  add(data){
    return $axios({
      method: 'post',
      url: '/api/users/',
      data
    });
  }

  detail(id){
    return $axios({
      method: 'get',
      url: '/api/users/' + id,
    });
  }
  
}
export let users = new Users();

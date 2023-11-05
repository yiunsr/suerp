import {$axios, param2formdata} from "@/api/service/request"

class Persons{
  list(filters, sort, page=1, limit=50){
    let params = {...filters, sort, page, limit,};
    return $axios({
      method: 'get',
      url: '/api/persons/',
      params
    });
  }

  add(data){
    return $axios({
      method: 'post',
      url: '/api/persons/',
      data
    });
  }

  update(id, data){
    return $axios({
      method: 'put',
      url: '/api/persons/' + id,
      data
    });
  }

  get(id){
    return $axios({
      method: 'get',
      url: '/api/persons/' + id,
    });
  }
  
}
export let persons = new Persons();

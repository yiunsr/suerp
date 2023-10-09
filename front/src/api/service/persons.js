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
  
}
export let persons = new Persons();

import {$axios, param2formdata} from "@/api/service/request"

class Persons{
  list(filters, sort, skip=0, limit=50){
    let params = {...filters, sort, skip, limit,};
    return $axios({
      method: 'get',
      url: '/api/persons/',
      params
    });
  }
  
}
export let persons = new Persons();

import {$axios, param2formdata} from "@/api/service/request"

const URL_BASE = '/api/col_metas/'

class ColMetaAPI{
  list(filters, sort, page=1, limit=50){
    let params = {...filters, sort, page, limit,};
    return $axios({
      method: 'get',
      url: URL_BASE,
      params
    });
  }

  add(data){
    return $axios({
      method: 'post',
      url: URL_BASE,
      data
    });
  }

  update(id, data){
    return $axios({
      method: 'put',
      url: URL_BASE + id,
      data
    });
  }

  get(id){
    return $axios({
      method: 'get',
      url: URL_BASE + id,
    });
  }

  getUserField(){
    return $axios({
      method: 'get',
      url: URL_BASE + "user",
    });
  }
  
}
export let colMetaAPI = new ColMetaAPI();

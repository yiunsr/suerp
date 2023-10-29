import { useRoute,  useRouter } from 'vue-router';

let utils = {
  query2sortBy: function(query){
    return query.sort;
  },
  getDefaultSortBy: function(sortByStr, argDefaultSortBy){
    if(!argDefaultSortBy)
      argDefaultSortBy = [{key: "id", order: "desc"}];
    let defualtSortBy = [];
    if(sortByStr){
      let sortbys = sortByStr.split(",")
      for(let key of sortbys){
        if(key[0] == "-") defualtSortBy.push({ key: key.slice(1), order: 'desc' })
        else defualtSortBy.push({ key: key, order: 'asc' })
      }
    }
    else{
      defualtSortBy = argDefaultSortBy;
    }
    return defualtSortBy;
  },
  initFilters: function(query, defaultFilters){
    if(!query)
      return defaultFilters;
    let filterDict={};
    for(const key in defaultFilters){
      if(key in query){
        filterDict[key] = query[key];
      }
      else{
        filterDict[key] = defaultFilters[key];
      }
    }
    return filterDict;
  },
  changeSortUrl: function($route, $router, sortBy){
    let query = {...$route.query};
    if(sortBy && sortBy.length > 0 ){
      let urlSortParam = [];
      for(let item of sortBy){
        let key = item["key"];
        let order = item["order"];
        if(order == "desc"){
          key = "-" + key
        }
        urlSortParam.push(key);
      }
      let urlSortStr = urlSortParam.join(",");
      query["sort"] = urlSortStr;
    }
    else if(query["sort"]){
      delete  query["sort"];
    }
    let path = $route.path;
    $router.push({path, query}).catch(()=>{});
  },
  changeLimit: function($route, $router, limit){
    let query = {...$route.query};
    query["limit"] = limit;
    query["page"] = 1;
    let path = $route.path;
    $router.push({path, query}).catch(()=>{});
  },
  changePage: function($route, $router, page){
    let query = {...$route.query};
    query["page"] = page;
    let path = $route.path;
    $router.push({path, query}).catch(()=>{});
  },
  getItemByValue(items, value){
    for(const item of items){
      if(item.value == value){
        return item;
      }
    }
    return null;
  }

}

export {utils}
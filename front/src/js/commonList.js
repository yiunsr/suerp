
import { computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute,  useRouter } from 'vue-router';
import {utils} from '@/plugins/utils';

let $store;
let $route;
let $router;
let defaultFilter;
let initFilter;
let filters;

function initCommonList(_defaultFilter, _initFilter, _filters){
  defaultFilter = _defaultFilter;
  initFilter = _initFilter;
  filters = _filters;
  $store = useStore();
  $route = useRoute();
  $router = useRouter();
}

const isLogin = computed(() => {
  return $store.getters.isLogin;
});

function search (){
  let path = $route.path;
  const simpleFilter = utils.getSimpleFilter(filters, defaultFilter);
  $router.push({ path, query: simpleFilter});
}

function changeItemsPerPage(limit){
  utils.changeLimit($route, $router, limit);
}

function changePage(page){
  utils.changePage($route, $router, page);
}
export {initCommonList, isLogin, search, changeItemsPerPage, changePage}

<template>
  <div>
    <ListHeader :listTitle="t('page_cate_meta.list_title')" addUrl="/cate_meta/new" 
      @search="search"/>
    
    <ListTable
      :headers="headers" :sortBy="tableData.sortBy" 
      idUrlPrefix="/cate_meta/"
      :items="tableData.data" 
      :total="tableData.total" 
      :page="tableData.page" :limit="tableData.limit"
      :filters="filters" @search="search"
    >

      <template v-slot:filter>
        <td class="id">
          <v-text-field type="number" hide-spin-buttons density="compact" 
            v-model="filters.id" @keyup.enter="search" hide-details  />
        </td>

        <td></td>
        <td></td>
        <td></td>
      </template>
    </ListTable>

  </div>
</template>

<script setup>
import { reactive, onMounted, computed, watch } from 'vue';
import { useStore } from 'vuex';
import { useRoute,  useRouter } from 'vue-router';
import {i18n} from '@/plugins/i18n';
import {utils} from '@/plugins/utils';

import ListHeader from "@/components/ListHeader";
import ListTable from "@/components/ListTable";

import {reverseItem, ColMetaTableItems, ColMetaColumnMetaItems, ColMetaDataTypeItems} from '@/js/commonValue';

import {cateMetaAPI} from '@/api/service/cate_meta';

const $store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const headers = [
  { title: 'id', key: 'id', width: 80, },
  { code: 'common_const.status', key: 'status' },
  { code: 'page_cate_meta.table_meta_id', key: 'table_meta_id',
    value: function(_, value){ return reverseItem(ColMetaTableItems.value, value);},
  },
  { code: 'page_common.name', key: 'name'},
];
let defaultFilter = {id: "", status: [], table_meta_id: "", cate_meta: "", data_type: ""};
let initFilter = utils.initFilters($route.query, defaultFilter);


/**** common list code start ****/
const page = parseInt($route.query.page || 1);
const limit = parseInt($route.query.limit || 0) || 50;

let defualtSortBy = utils.getDefaultSortBy($route.query.sort);

let filters = reactive(initFilter);
let tableData = reactive({
  data: [], total: 0, sortBy: defualtSortBy, limit: limit, page: page,
});

function search(){
  let path = $route.path;
  const simpleFilter = utils.getSimpleFilter(filters, defaultFilter);
  $router.push({ path, query: simpleFilter});
}
/**** common list code end ****/

onMounted(() => {
  let sort = utils.query2sortBy($route.query) || "-id";
  cateMetaAPI.list(filters, sort, page, limit).then(function(res){
    let resData = res.data;
    tableData.data = resData.data;
    tableData.total = resData.total;
  }).catch(function(error){
  });
})

watch(
  () => tableData.sortBy,
  (sortBy) => {
    utils.changeSortUrl($route, $router, sortBy);
  }
)


</script>

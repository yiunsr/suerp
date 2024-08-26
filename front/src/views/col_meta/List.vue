<template>
  <div>
    <ListHeader :listTitle="t('page_col_meta.list_title')" addUrl="/col_meta/new" 
      @search="search"/>
    
    <ListTable :headers="headers" :sortBy="tableData.sortBy" 
      idUrlPrefix="/col_meta/"
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

        <td class="status"></td>

        <td class="user_role"></td>

        <td class="email">
          <v-text-field type="text" density="compact" 
            v-model="filters.email" @keyup.enter="search" hide-details />
        </td>
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

import {reverseItem, ColMetaTableItems} from '@/js/commonValue';

import {colMetaAPI} from '@/api/service/col_meta';

const $store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const headers = [
  { title: 'id', key: 'id', width: 80, },
  { title: t('common_const.status'), key: 'status' },
  { title: t('page_col_meta.table_meta_id'), key: 'table_meta_id' },
  { title: t('page_col_meta.column_meta'), key: 'column_meta' },
  { title: t('page_col_meta.data_type'), key: 'data_type' },
];
let defaultFilter = {id: "", status: [], table_meta_id: "", col_meta: "", data_type: ""};
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
  colMetaAPI.list(filters, sort, page, limit).then(function(res){
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

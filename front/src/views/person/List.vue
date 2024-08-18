<template>
  <div>
    <ListHeader :listTitle="t('page_person.list_title')" addUrl="/person/new" 
      @search="search"/>
    
    <ListTable :headers="headers" :sortBy="tableData.sortBy" 
      idUrlPrefix="/person/"
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

        <td class="display">
          <v-text-field type="text" density="compact" 
            v-model="filters.display" @keyup.enter="search" hide-details  />
        </td>

        <td class="first_name">
          <v-text-field type="text" density="compact" 
            v-model="filters.last_name" @keyup.enter="search" hide-details  />
        </td>

        <td class="email">
          <v-text-field type="text" density="compact" 
            v-model="filters.first_name" @keyup.enter="search" hide-details />
        </td>

        <td class="email">
          <v-text-field type="text" density="compact" 
            v-model="filters.email" @keyup.enter="search" hide-details />
        </td>

        <td class="phone">
          <v-text-field type="text" density="compact" 
            v-model="filters.phone" @keyup.enter="search" hide-details />
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

import {personAPI} from '@/api/service/persons';

const store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const headers = [
  { title: 'id', key: 'id', width: 80, },
  { code: 'page_common.display', key: 'display' },
  { code: 'page_common.last_name', key: 'last_name' },
  { code: 'page_common.first_name', key: 'first_name' },
  { code: 'page_common.email', key: 'email_jb[0].value' },
  { code: 'page_common.phone', key: 'phone_jb[0].value' },
];

let defaultFilter = {id: "", display: "", last_name: "", first_name: "", phone: "", email: ""}
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
  personAPI.list(filters, sort, page, limit).then(function(res){
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

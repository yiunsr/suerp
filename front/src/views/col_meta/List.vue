<template>
  <div>
    <table class="header-table">
      <colgroup><col><col><col></colgroup>
      <thead>
        <tr>
          <td>
            <div class="text-h5 pa-2">
              {{ t("page_col_meta.list_title") }}
            </div>
          </td>
          <td>
            <v-btn to="/col_meta/new" density="comfortable" class="ma-1 " size="large" color="blue-darken-4">
              {{  t('page_common.add') }}
            </v-btn>
          </td>
          <td>
            <v-btn density="compact" class="ma-1" @click="search">
              <v-icon icon="mdi mdi-magnify"  ></v-icon>
            </v-btn>
          </td>
        </tr>
      </thead>
    </table>
    
    <div v-if="isLogin">
      <v-data-table-server
        density="compact" class="data-list-table my-2" hide-default-footer
        :no-data-text="t('ui_table.no_data')" :items-per-page-text="t('ui_table.per_page')"	
        :headers="headers"
        v-model:sort-by="tableData.sortBy" :multi-sort="true" :must-sort="false"
        :items="tableData.data"
        :items-length="tableData.total"
      >
        <template v-slot:body.prepend>
          <tr class="table-filter">
            <td class="id">
              <v-text-field type="number" hide-spin-buttons density="compact" 
                v-model="filters.id" @keyup.enter="search" hide-details  />
            </td>

            <td class="status">
              
            </td>

            <td class="user_role">
              
            </td>

            <td class="email">
              <v-text-field type="text" density="compact" 
                v-model="filters.email" @keyup.enter="search" hide-details />
            </td>
          </tr>
        </template>

        <template v-slot:item.id="row">
          <router-link :to="'/user/' + row.item.id">{{ row.item.id }}</router-link>
        </template>

        <template v-slot:bottom>
          <v-row class="text-center pt-2">
            <v-col cols="2"></v-col>
            <v-col cols="8">
              <v-pagination class="text-center"
                v-model="tableData.page" density="compact" 
                :length="Math.ceil(tableData.total / tableData.limit)"
                @update:model-value="changePage"
              ></v-pagination>
            </v-col>
            <v-col cols="2">
              <v-select :hide-details="true" class="ma-0"
                :model-value="tableData.limit"
                :items="[{value: 5, title: '5'}, {value: 10, title: '10'}, {value: 25, title: '25'},
                  {value: 50, title: '50'}, {value: 100, title: '100'},
                ]"
                density="compact"
                label="Item Per Page"
                @update:model-value="changeItemsPerPage"
              ></v-select>
            </v-col>
          </v-row>
        </template>
      </v-data-table-server>
    </div>
    <div v-else class="mt-8">
      <h3>
        {{ t("common.login_required") }}
      </h3>
    </div>
  </div>
</template>

<script setup>
import { reactive, onMounted, computed, watch } from 'vue';
import { useStore } from 'vuex';
import { useRoute,  useRouter } from 'vue-router';
import {i18n} from '@/plugins/i18n';
import {utils} from '@/plugins/utils';

import {ColMetaTableItems} from '@/js/commonValue';
import {initCommonList, isLogin, search, 
  changeItemsPerPage, changePage} from '@/js/commonList';

import {colMetaAPI} from '@/api/service/col_meta';

const $store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const headers = [
  { title: 'id', key: 'id', width: 80, },
  { title: t('common_const.status'), key: 'status' },
  { title: t('page_col_meta.table_meta_id'), key: 'table_meta_id' },
  { title: t('page_col_meta.col_meta'), key: 'col_meta' },
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

initCommonList(defaultFilter, initFilter, filters);
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

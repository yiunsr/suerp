<template>
  <div>
    <table class="header-table">
      <colgroup><col><col><col></colgroup>
      <thead>
        <tr>
          <td>
            <div class="text-h5 pa-2">
              {{ t("page_user.list_title") }}
            </div>
          </td>
          <td>
            <v-btn to="/user/new" density="comfortable" class="ma-1 " size="large" color="blue-darken-4">
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
              <v-select :items="UserStatusItems" multiple density="compact" chips
                v-model="filters.status" hide-details></v-select>
            </td>

            <td class="user_role">
              <v-select :items="UserRoleItems" multiple density="compact" chips
                v-model="filters.user_role" hide-details></v-select>
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

        <template v-slot:item.status="row">
          <div>{{ rowStaus(row.item.status) }}</div>
        </template>

        <template v-slot:item.user_role="row">
          <div>{{ rowUserRole(row.item.user_role) }}</div>
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

import {UserStatusItems, UserRoleItems} from '@/js/commonValue';
import {initCommonList, isLogin, search, 
  changeItemsPerPage, changePage} from '@/js/commonList';

import {userAPI} from '@/api/service/users';

const $store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const headers = [
  { title: 'id', key: 'id', width: 80, },
  { title: t('page_common.status'), key: 'status' },
  { title: t('page_uesr.user_role'), key: 'user_role' },
  { title: t('page_common.email'), key: 'email' },
  { title: t('page_common.last_name'), key: 'last_name' },
  { title: t('page_common.first_name'), key: 'first_name' },
];
let defaultFilter = {id: "", status: [], user_role: [], email: "",};
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
  userAPI.list(filters, sort, page, limit).then(function(res){
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

function rowStaus(status){
  let item = utils.getItemByValue(UserStatusItems, status);
  if(!item) return "";
  return item.title;
}

function rowUserRole(role){
  let item = utils.getItemByValue(UserRoleItems, role);
  if(!item) return "";
  return item.title;
}

</script>

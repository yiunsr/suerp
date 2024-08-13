<template>
  <div>
    <h2>
      {{ t("page_user.list_title") }}
      <v-btn to="/user/new" density="comfortable" class="ml-4 mb-2" size="large" color="blue-darken-4">
        {{  t('page_common.add') }}
      </v-btn>
    </h2>
    <div v-if="isLogin">
      <div class="my-2">
        <v-form validate-on="submitFilter lazy" @submit.prevent="submitFilter">
          <table class="search-table">
            <colgroup>  <col><col><col>   </colgroup>
            <thead>
              <tr>
                <td>
                  <v-container class="ma-0 pa-0">
                    <v-row align="center" justify="center">
                      <v-col md="1" sm="2">
                        <div class="ms-4">{{ t("ui_table.search") }}</div>
                      </v-col>
                      <v-col md="2" sm="4">
                        <v-text-field type="email" density="compact" v-model="filters.id" hide-details label="ID" />
                      </v-col>
                      <v-col md="3" sm="5">
                        <v-text-field density="compact" v-model="filters.email" hide-details label="email" />
                      </v-col>
                      <v-col md="6" sm="1"></v-col>
                    </v-row>
                  </v-container>
                </td>
                <td>
                  <v-btn density="compact" class="pa-0" @click="submitFilter">
                    <v-icon icon="mdi mdi-magnify"  ></v-icon>
                  </v-btn>
                </td>
                <td>
                  <v-btn density="compact" class="pa-0" 
                      @click="searchTable.detail = !searchTable.detail">
                    <v-icon icon="mdi mdi-chevron-down"></v-icon>
                  </v-btn>
                </td>
              </tr>
            </thead>
            <tbody :class="{ show: searchTable.detail }">
              <tr>
                <td colspan="3">
                  <div>
                    <v-row>
                      <v-col>
                        test
                      </v-col>
                    </v-row>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </v-form>
      </div>

      <v-data-table-server
        density="compact" class="data-list-table my-2" hide-default-footer
        :no-data-text="t('ui_table.no_data')" :items-per-page-text="t('ui_table.per_page')"	
        :headers="headers"
        v-model:sort-by="tableData.sortBy" :multi-sort="true" :must-sort="false"
        :items="tableData.data"
        :items-length="tableData.total"
      >
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

import {UserStatusItems, UserRoleItems} from '@/commonValue';
import {users} from '@/api/service/users';


const store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const headers = [
  { title: 'id', key: 'id' },
  { title: t('page_common.status'), key: 'status' },
  { title: t('page_uesr.user_role'), key: 'user_role' },
  { title: t('page_common.email'), key: 'email' },
  { title: t('page_common.last_name'), key: 'last_name' },
  { title: t('page_common.first_name'), key: 'first_name' },
];
let initFilter = utils.initFilters($route.query,
  {id: "", email: ""}
);


/**** common list code start ****/
const page = parseInt($route.query.page || 1);
const limit = parseInt($route.query.limit || 0) || 50;

let defualtSortBy = utils.getDefaultSortBy($route.query.sort);

let searchTable = reactive(
  {detail: false}
);

let filters = reactive(initFilter);
let tableData = reactive({
  data: [], total: 0, sortBy: defualtSortBy, limit: limit, page: page,
});

const isLogin = computed(() => {
  return store.getters.isLogin;
});

function submitFilter (){
  let path = $route.path;
  $router.push({ path, query: filters});
}

function changeItemsPerPage(limit){
  utils.changeLimit($route, $router, limit);
}
function changePage(page){
  utils.changePage($route, $router, page);
}
/**** common list code start ****/


onMounted(() => {
  let sort = utils.query2sortBy($route.query) || "-id";
  users.list(filters, sort, page, limit).then(function(res){
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
  return t(item.title) + "(" + item.value + ")";
}

function rowUserRole(role){
  let item = utils.getItemByValue(UserRoleItems, role);
  if(!item) return "";
  return t(item.title) + "(" + item.value + ")";
}

</script>

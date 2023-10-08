<template>
  <div>
    <h2>
      {{ t("page_user_list.title") }}
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
        <!--
        <v-row>
          <v-col cols="11">
            {{ t('ui_table.search') }}
          </v-col>
          <v-col cols="1">
            <v-btn density="compact" class="ma-2" variant="outlined">
              <v-icon icon="mdi mdi-subdirectory-arrow-left"></v-icon>
            </v-btn>
          </v-col>
        </v-row>
        -->
      </div>
      <v-data-table-server 
        density="compact" class="data-list-table my-2"
        :no-data-text="t('ui_table.no_data')" :items-per-page-text="t('ui_table.per_page')"	
        :headers="headers"
        v-model:sort-by="tableData.sortBy" :multi-sort="true" :must-sort="false"	
        :items-per-page="tableData.limit"
        :items="tableData.data"
        :items-length="tableData.total"
      >
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
import { VDataTableServer } from 'vuetify/lib/labs/components';
import {users} from '@/api/service/users';

const store = useStore();
let t=i18n.global.t;

let headers = [
  { title: 'id', key: 'id' },
  { title: t('page_common.email'), key: 'email' },
  { title: t('page_common.last_name'), key: 'last_name' },
  { title: t('page_common.first_name'), key: 'first_name' },
];

let skip = 0;
let limit = 50;

const $route = useRoute();
let $router = useRouter();

let defualtSortBy = utils.getDefaultSortBy($route.query.sort);

let searchTable = reactive(
  {detail: false}
);


let initFilter = utils.initFilters($route.query,
  {id: "", email: ""}
);
let filters = reactive(initFilter);
let tableData = reactive({
  data: [], total: 0, sortBy: defualtSortBy,
});

const isLogin = computed(() => {
  return store.getters.isLogin;
});

function submitFilter (){
  let path = $route.path;
  $router.push({ path, query: filters});
}

onMounted(() => {
  skip = parseInt($route.query.skip || 0) || skip;
  limit = parseInt($route.query.limit || 0) || limit;
  tableData.limit = limit;
  let sort = utils.query2sortBy($route.query) || "-id";
  users.list(filters, sort, skip, limit).then(function(res){
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

watch(
  () => tableData.sortBy,
  (sortBy) => {
    utils.changeSortUrl($route, $router, sortBy);
  }
)


</script>

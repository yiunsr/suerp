<template>
  <div>
    <h2>
      {{ t("page_person.title") }}
      <v-btn to="/person/new" density="comfortable" class="ml-4 mb-2" size="large" color="blue-darken-4">
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
                        <v-text-field type="number" density="compact" v-model="filters.id" @keyup.enter="submitFilter" hide-details label="ID" />
                      </v-col>
                      <v-col md="2" sm="4">
                        <v-text-field type="text" density="compact" v-model="filters.display" @keyup.enter="submitFilter" hide-details label="display" />
                      </v-col>
                      <v-col md="3" sm="5">
                        <v-text-field density="compact" v-model="filters.email" hide-details @keyup.enter="submitFilter" label="email" />
                      </v-col>
                      <v-col md="4" sm="1"></v-col>
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
        density="compact" class="data-list-table my-2" hide-default-footer
        :no-data-text="t('ui_table.no_data')" :items-per-page-text="t('ui_table.per_page')"	
        :headers="headers"
        v-model:sort-by="tableData.sortBy" :multi-sort="true" :must-sort="false"
        :items="tableData.data"
        :items-length="tableData.total"
      >
        <template v-slot:item.id="row">
          <router-link :to="'/person/' + row.item.id">{{ row.item.id }}</router-link>
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
                :items="[{value: 2, title: '2'}, {value: 25, title: '25'},
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
import { VDataTableServer } from 'vuetify/lib/labs/components';
import {persons} from '@/api/service/persons';

const store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const headers = [
  { title: 'id', key: 'id' },
  { title: t('page_common.display'), key: 'display' },
  { title: t('page_common.last_name'), key: 'last_name' },
  { title: t('page_common.first_name'), key: 'first_name' },
  { title: t('page_common.email'), key: 'email_jb[0].value' },
  { title: t('page_common.phone'), key: 'phone_jb[0].value' },
];
let initFilter = utils.initFilters($route.query,
  {id: "", display: "", phone: "", email: ""}
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
  persons.list(filters, sort, page, limit).then(function(res){
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

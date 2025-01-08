<template>
  <div>
    <div v-if="isLogin">
      <v-data-table-server
        density="compact" class="data-list-table my-2" hide-default-footer
        :no-data-text="t('ui_table.no_data')" :items-per-page-text="t('ui_table.per_page')"	
        :headers="headerData"
        v-model:sort-by="props.sortBy" :multi-sort="true" :must-sort="false"
        :items="props.items"
        :items-length="props.total"
      >

        <template v-slot:body.prepend>
          <tr class="table-filter">
            <slot name="filter">
            </slot>
          </tr>
        </template>

        <template v-slot:item="{ item }">
          <tr>
            <td class="id">
              <router-link :to="props.idUrlPrefix + item.id">{{ item.id }}</router-link>
            </td>
            
            <td v-for="header in props.headers.slice(1)" :class="header.key">
              <template v-if="header.hasOwnProperty('value')">
                {{ header.value(item, item[header.key]) }}
              </template>

              <template v-else>
                {{ item[header.key] }}
              </template>
            </td>
          
          </tr>
        </template>

        <template v-slot:bottom>
          <v-row class="text-center pt-2">
            <v-col cols="2"></v-col>
            <v-col cols="8">
              <v-pagination class="text-center"
                :modelValue="props.page" density="compact" 
                :length="Math.ceil(props.total / props.limit)"
                @update:model-value="changePage"
              ></v-pagination>
            </v-col>
            <v-col cols="2">
              <v-select :hide-details="true" class="ma-0"
                :model-value="props.limit"
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
import _ from 'lodash';
import { computed, watch, reactive} from 'vue';
import { useStore } from 'vuex';
import { useRoute,  useRouter } from 'vue-router';
import {i18n} from '@/plugins/i18n';
import {utils} from '@/plugins/utils';

const props = defineProps({
  idUrlPrefix: { type: String, default: "" },
  headers: { type: Object, default: [] },
  items: { type: Object, default: [] },
  page: { type: Number, default: 0 },
  total: { type: Number, default: 0 },
  limit: { type: Number, default: 0 },
  sortBy: { type: Object, default: [] },
  filters: { type: Object, default: {} },
  
});

const _headers = _.cloneDeep(props.headers)
const headerData = reactive(_headers);

const $store = useStore();
const $route = useRoute();
const $router = useRouter();

const isLogin = computed(() => {
  return $store.getters.isLogin;
});

function changeItemsPerPage(limit){
  utils.changeLimit($route, $router, limit);
}

function changePage(page){
  utils.changePage($route, $router, page);
}

let t=i18n.global.t;

watch(() => $store.getters.getLang, function(){
  let index = 0;
  for(const header of props.headers){
    if(header.hasOwnProperty('title')){
      headerData[index]["title"] = header.title;
    }
    else{
      headerData[index]["title"] = t(header.code);
    }
    index += 1;
  }
}, { immediate: true });

</script>

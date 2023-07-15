<template>
  <div>
    <h2>
      {{ t("page_user_list.title") }}
    </h2>
    <div v-if="isLogin">
      <v-data-table-server density="compact" class="data-list-table"
        :no-data-text="t('ui_table.no_data')" :items-per-page-text="t('ui_table.per_page')"	
        :headers="headers"
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
import { reactive, onMounted, computed } from 'vue';
import {useStore} from 'vuex';
import { useRoute } from 'vue-router';
import {i18n} from '@/plugins/i18n';
import { VDataTableServer } from 'vuetify/lib/labs/components';
import {users} from '@/api/service/users';

const store = useStore();
let t=i18n.global.t;

let headers = [
  { title: 'id', key: 'id' },
  { title: t('page_user_list.email'), key: 'email' },
  { title: t('page_user_list.last_name'), key: 'last_name' },
  { title: t('page_user_list.first_name'), key: 'first_name' },
];

let skip = 0;
let limit = 50;
let tableData = reactive({
  data: [], total: 0,
})

const isLogin = computed(() => {
  return store.getters.isLogin;
});

onMounted(() => {
  const route = useRoute();
  skip = route.query.skip | skip;
  limit = route.query.limit | limit;
  tableData.limit = limit;
  users.list(skip, limit).then(function(res){
    let resData = res.data;
    tableData.data = resData.data;
    tableData.total = resData.total;
  }).catch(function(error){
  });
})
</script>

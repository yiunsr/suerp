<template>
  <div>
    <h2 v-if="isNewPage">
      {{ t("page_user.new_title") }}
    </h2>
    <h2 v-else>
      {{ t("page_user.edit_title") }}
    </h2>

    <fieldset class="mt-2 py-4 px-4 rounded-lg">
      <legend class="text-right mr-4">
        <v-btn-toggle v-model="detail.mode" color="primary" divided variant="outlined"
            mandatory density="compact">
          <v-btn prepend-icon="mdi-pencil" value="edit">{{  t('page_common.edit_mode') }}</v-btn>
          <v-btn prepend-icon="mdi-book-open" value="read">{{  t('page_common.read_mode') }}</v-btn>
        </v-btn-toggle>
      </legend>
      <v-form v-model="detail.valid" validate-on="input" ref="detailForm">
        <v-row>
          <v-col cols="12" md="4" v-show="data.id != undefined">
            <b class="mr-4">ID : </b> <span>{{  data.id }}</span>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_common.email')" type="email" :mode="detail.mode"
              :counter="256"
              required v-model="data.email" :rules="[rule.req, rule.email]" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_common.status')" :items="UserStatusItems" item-title="str" 
              :mode="detail.mode" :i18nValue="false"
              required v-model="data.status" :rules="[rule.req]" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_uesr.user_role')" :items="UserRoleItems" item-title="str" 
              :mode="detail.mode"  :i18nValue="false"
              required v-model="data.user_role" :rules="[rule.req]" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_common.last_name')" type="text" :mode="detail.mode"
              :counter="64"
              v-model="data.last_name"></mode-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_common.first_name')" type="text" :mode="detail.mode"
              :counter="64"
              v-model="data.first_name"></mode-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_user.nickname')" type="text" :mode="detail.mode"
              :counter="64"
              v-model="data.nickname"></mode-text-field>
          </v-col>
          
          <v-col cols="12" md="4">
            <mode-text-field label="ref_id0" type="number" :mode="detail.mode"
              v-model="data.ref_id0" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field label="ref_id1" type="number" :mode="detail.mode"
              v-model="data.ref_id1" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field label="ref_id2" type="number" :mode="detail.mode"
              v-model="data.ref_id2" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field label="ref_id3" type="number" :mode="detail.mode"
              v-model="data.ref_id3" />
          </v-col>

          
        </v-row>

        <v-row class="mt-4 mb-n2  py-0">
          <v-col>
            <hr class="float-left" size="1" width="45%">
            <span class="text-center mt-n3 float-left" style="width:10%;">category</span>
            <hr class="float-right" size="1" width="45%">
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="4">
            <mode-select label="category"
              :mode="detail.mode" :i18nValue="false" :items="custom_category.infos"
              item-title="name" item-value="id"
              required v-model="data.category_meta_id" :rules="[rule.req]" />
          </v-col>


          <v-col cols="12" md="4" v-for="cf_item in cur_custom_field">
            <mode-custom-field :label="cf_item.name" :type="cf_item.html_type" 
              :mode="detail.mode"
              v-model="custom_field.data['user_' + cf_item['code']]" />
          </v-col>
        </v-row>
        
        

        <v-row v-show="detail.mode == 'edit'">
          <v-col md="4">
            <v-btn v-if="isNewPage" color="success" @click="submitAdd">{{ t('page_common.add_new') }}</v-btn>
            <v-btn v-else color="success" @click="submitUpdate">{{ t('page_common.apply_update') }}</v-btn>
          </v-col>
        </v-row>
        
      </v-form>
    </fieldset>
  </div>
</template>
  
<script setup>
import _ from 'lodash';

import { ref, reactive, watch, computed } from 'vue';
import { toast } from 'vue3-toastify';
import { useStore } from 'vuex';
import { useRoute,  useRouter } from 'vue-router';
import {i18n} from '@/plugins/i18n';
import {utils} from '@/plugins/utils';
import {rule} from '@/js/rule';

import {UserStatusItems, UserRoleItems} from '@/js/commonValue';
import {userAPI} from '@/api/service/users';
import {colMetaAPI} from '@/api/service/col_meta';
import {categoryMetaAPI} from '@/api/service/category_meta';
import ModeCustomField from "@/widgets/ModeCustomField";
import ModeTextField from "@/widgets/ModeTextField";
import ModeRadioGroup from "@/widgets/ModeRadioGroup";
import ModeSelect from "@/widgets/ModeSelect";
import { onMounted } from 'vue';

const store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const detailForm = ref(null);
const userId = $route.params.id;

let isNewPage = $route.path.includes("new")?true:false;
let mode = $route.path.includes("new")?"edit":"read";
let detail = reactive({ mode, valid: false });


let data = reactive({
  id: null, email: "", status: "A", user_role: null, 
  last_name: "", first_name: "", nickname: "", category_meta_id: null,
  ref_id0: null, ref_id1: null, 
  ref_id2: null, ref_id3: null,
});
let custom_field = reactive({
  infos: [], data: {},
});
let custom_category = reactive({
  infos: [], data: {},
});

async function submitAdd(){
  console.log("form valid : " + detail.valid);
  if(!detail.valid){
    await detailForm.value.validate();
    return;
  }
    
  userAPI.add(data).then(function(res){
    $router.push('/user/' + res.data.id);
    toast.success(t('page_common.add_success'));
  }).catch(function(error){
  });
}

function submitUpdate(){
  let id = data.id;
  
  userAPI.update(id, data).then(function(res){
    toast.success(t('page_common.add_success'));
    detail.mode = 'read';
  }).catch(function(error){
  });
}

function getUserField(){
  colMetaAPI.getUserField().then(function(res){
    custom_field.infos = _.groupBy(res.data.data, "category_meta_id");
  }).catch(function(error){
  });
}

function getUserCategory(){
  categoryMetaAPI.getUserCategory().then(function(res){
    const categoryDict = _.groupBy(res.data.data, "table_meta_id");
    custom_category.infos = categoryDict[1] || [];
  }).catch(function(error){
  });
}

function getAPIDetail(){
  userAPI.get(userId).then(function(res){
    data.id = res.data.id;
    data.email = res.data.email;
    data.status = res.data.status;
    data.user_role = res.data.user_role;

    data.last_name = res.data.last_name;
    data.first_name = res.data.first_name;
    data.nickname = res.data.nickname;

    data.category_meta_id = res.data.category_meta_id;

    data.ref_id0 = res.data.ref_id0;
    data.ref_id1 = res.data.ref_id1;
    data.ref_id2 = res.data.ref_id2;
    data.ref_id3 = res.data.ref_id3;

    for (const [key, value] of Object.entries(res.data)) {
      if (!key.startsWith('user__')) continue;
        custom_field.data[key] = value;
    }
  }).catch(function(error){
  });
}


onMounted(() => {
  getUserField();
  getUserCategory();
   if(!isNewPage){
    getAPIDetail();
  }
})

const cur_custom_field = computed(() => {
  return custom_field.infos[data.category_meta_id];
});

watch(() => custom_field.data, (newValue, oldValue) => {
  for (const [key, value] of Object.entries(newValue)) {
    data[key] = value;
  }
},{deep: true, immediate: false})
</script>

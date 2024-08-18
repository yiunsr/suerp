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
              required v-model="data.email" :rules="[rule.req, rule.email]" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_common.status')" :items="UserStatusItems" item-title="str" 
              :mode="detail.mode"
              required v-model="data.status" :rules="[rule.req]" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_uesr.user_role')" :items="UserRoleItems" item-title="str" 
              :mode="detail.mode"
              required v-model="data.user_role" :rules="[rule.req]" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_common.last_name')" type="text" :mode="detail.mode"
              v-model="data.last_name"></mode-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_common.first_name')" type="text" :mode="detail.mode" 
              v-model="data.first_name"></mode-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_user.nickname')" type="text" :mode="detail.mode"
              v-model="data.nickname"></mode-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_uesr.display')" type="text" :mode="detail.mode"
              v-model="data.display"></mode-text-field>
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

        <v-row v-show="detail.mode == 'edit'">
          <v-col md="4">
            <v-btn v-if="isNewPage" color="success" @click="submitAdd">{{ t('page_common.add_new') }}</v-btn>
            <v-btn v-else color="success" @click="submitUpdate">{{ t('page_common.apply_update') }}</v-btn>
          </v-col>
        </v-row>
        <!-- <mode-radio-group label="Name2" :items="[{label: 'label', value: 'value'}]"></mode-radio-group> -->
      </v-form>
    </fieldset>
  </div>
</template>
  
<script setup>
import { ref, reactive } from 'vue';
import { toast } from 'vue3-toastify';
import { useStore } from 'vuex';
import { useRoute,  useRouter } from 'vue-router';
import {i18n} from '@/plugins/i18n';
import {utils} from '@/plugins/utils';
import {rule} from '@/js/rule';

import {UserStatusItems, UserRoleItems} from '@/js/commonValue';
import {userAPI} from '@/api/service/users';
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
  last_name: "", first_name: "", nickname: "", display: "", 
  ref_id0: null, ref_id1: null, 
  ref_id2: null, ref_id3: null,
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
    data.display = res.data.display;

    data.ref_id0 = res.data.ref_id0;
    data.ref_id1 = res.data.ref_id1;
    data.ref_id2 = res.data.ref_id2;
    data.ref_id3 = res.data.ref_id3;
  }).catch(function(error){
  });
}

onMounted(() => {
  if(!isNewPage)
    getAPIDetail();
})


</script>

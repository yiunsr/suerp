<template>
  <div>
    <h2 v-if="mode == 'new'">
      {{ t("page_user.new_title") }}
      <v-btn class="mx-4" variant="flat" color="primary" @click="add">{{ t('page_common.add')}}</v-btn>
    </h2>
    <h2 v-if="mode == 'edit'">
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
      <v-form>
        <v-row>
          <v-col cols="12" md="4" v-show="data.id != undefined">
            <b class="mr-4">ID : </b> <span>{{  data.id }}</span>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-feild :label="t('page_common.email')" type="email" :mode="detail.mode"
              required v-model="data.email" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_common.status')" :items="UserStatusItems" :mode="detail.mode"
            required v-model="data.status" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_uesr.user_role')" :items="UserRoleItems" :mode="detail.mode"
            required v-model="data.user_role" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-feild :label="t('page_common.last_name')" type="text" :mode="detail.mode"
              required  v-model="data.last_name"></mode-text-feild>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-feild :label="t('page_common.first_name')" type="text" :mode="detail.mode" 
              required v-model="data.first_name"></mode-text-feild>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-feild :label="t('page_user.nickname')" type="text" :mode="detail.mode"
            required v-model="data.nickname"></mode-text-feild>
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-feild :label="t('page_uesr.display')" type="text" :mode="detail.mode"
            required v-model="data.display"></mode-text-feild>
          </v-col>
          
          <v-col cols="12" md="4">
            <mode-text-feild label="ref_id0" type="number" :mode="detail.mode"
              required v-model="data.ref_id0" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-feild label="ref_id1" type="number" :mode="detail.mode"
              required v-model="data.ref_id1" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-feild label="ref_id2" type="number" :mode="detail.mode"
              required v-model="data.ref_id2" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-feild label="ref_id3" type="number" :mode="detail.mode"
              required v-model="data.ref_id3" />
          </v-col>
        </v-row>

        <v-row v-show="detail.mode == 'edit'">
          <v-col md="4">
            <v-btn color="success">{{ t('page_common.apply_modify') }}</v-btn>
          </v-col>
        </v-row>
        <!-- <mode-radio-group label="Name2" :items="[{label: 'label', value: 'value'}]"></mode-radio-group> -->
      </v-form>
    </fieldset>
  </div>
</template>
  
<script setup>
import { reactive } from 'vue';
import { toast } from 'vue3-toastify';
import { useStore } from 'vuex';
import { useRoute,  useRouter } from 'vue-router';
import {i18n} from '@/plugins/i18n';

import {UserStatusItems, UserRoleItems} from '@/commonValue';
import {users} from '@/api/service/users';
import ModeTextFeild from "@/widgets/ModeTextFeild";
import ModeRadioGroup from "@/widgets/ModeRadioGroup";
import ModeSelect from "@/widgets/ModeSelect";
import { onMounted } from 'vue';

const store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const userId = $route.params.userId;

let mode = $route.path.includes("new")?"edit":"read";
let detail = reactive({ mode });

let data = reactive({
  id: undefined, email: "", status: "", user_role: "", 
  last_name: "", first_name: "", nickname: "", display: "", 
  ref_id0: undefined, ref_id1: undefined, 
  ref_id2: undefined, ref_id3: undefined,
});

function add(){
  users.add(data).then(function(res){
    toast.success(t('page_common.add_success'));
  }).catch(function(error){
  });
}

function getAPIDetail(){
  users.detail(userId).then(function(res){
    data.id = res.data.id;
    data.email = res.data.email;
    data.status = res.data.status;
    data.user_role = res.data.user_role;

    data.last_name = res.data.last_name;
    data.first_name = res.data.first_name;
    data.nickname = res.data.nickname;
    data.display = res.data.display;
  }).catch(function(error){
  });
}

onMounted(() => {
  getAPIDetail();
})


</script>

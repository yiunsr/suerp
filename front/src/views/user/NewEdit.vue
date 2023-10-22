<template>
  <div>
    <h2 v-if="mode == 'new'">
      {{ t("page_user.new_title") }}
      <v-btn class="mx-4" variant="flat" color="primary" @click="add">{{ t('page_common.add')}}</v-btn>
    </h2>
    <h2 v-if="mode == 'edit'">
      {{ t("page_user.edit_title") }}
    </h2>

    <v-card variant="outlined" class="my-2 pt-4 px-2">
      <v-form>
        <mode-text-feild :label="t('page_common.email')" type="email" v-model="data.email"></mode-text-feild>
        <mode-text-feild :label="t('page_common.last_name')" type="text" required  v-model="data.last_name"></mode-text-feild>
        <mode-text-feild :label="t('page_common.first_name')" type="text" required v-model="data.first_name"></mode-text-feild>
        <mode-text-feild :label="t('page_user.nickname')" type="text" required v-model="data.nickname"></mode-text-feild>
        <!-- <mode-radio-group label="Name2" :items="[{label: 'label', value: 'value'}]"></mode-radio-group> -->
      </v-form>
    </v-card>
  </div>
</template>
  
<script setup>
import { reactive } from 'vue';
import { toast } from 'vue3-toastify';

import { useStore } from 'vuex';
import { useRoute,  useRouter } from 'vue-router';
import {i18n} from '@/plugins/i18n';
import {utils} from '@/plugins/utils';
import {users} from '@/api/service/users';
import ModeTextFeild from "@/widgets/ModeTextFeild";
import ModeRadioGroup from "@/widgets/ModeRadioGroup";

const store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const mode = $route.path.includes("new")?"new":"edit";

let data = reactive({
  email: "", last_name: "", first_name: "", nickname: "",
});

function add(){
  users.add(data).then(function(res){
    toast.success(t('page_common.add_success'));
  }).catch(function(error){
  });
}
</script>

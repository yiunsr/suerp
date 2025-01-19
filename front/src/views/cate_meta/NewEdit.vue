<template>
  <div>
    <h2 v-if="isNewPage">
      {{ t("page_cate_meta.new_title") }}
    </h2>
    <h2 v-else>
      {{ t("page_cate_meta.edit_title") }}
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
            <mode-select :label="t('page_common.status')" :items="ColMetaStateItems" item-title="str" 
              :mode="detail.mode"
              required v-model="data.status" :rules="[rule.req]" />
          </v-col>
          
          <v-col cols="12" md="4">
            <mode-select :label="t('page_cate_meta.table_meta_id')" 
              :items="ColMetaTableItems" item-title="str" item-value="value_int"
              :mode="detail.mode"
              required v-model="data.table_meta_id" :rules="[rule.req]" />
          </v-col>

          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_common.name')" type="text" :mode="detail.mode" 
              :counter=32
              required v-model="data.name"></mode-text-field>
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

import {reverseItem, strSubtitle,
  ColMetaStateItems, ColMetaTableItems, ColMetaColumnMetaItems, 
  ColMetaDataTypeItems, ColMetaVisibleItems, ColMetaHTMLTypeItems} from '@/js/commonValue';
import {cateMetaAPI} from '@/api/service/cate_meta';
import ModeTextField from "@/widgets/ModeTextField";
import ModeTextArea from "@/widgets/ModeTextArea";
import ModeDragableTwoText from "@/widgets/ModeDragableTwoText";
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
  id: null, status: "A", table_meta_id: null, 
  name: "",
});

async function submitAdd(){
  console.log("form valid : " + detail.valid);
  if(!detail.valid){
    await detailForm.value.validate();
    return;
  }

  cateMetaAPI.add(data).then(function(res){
    $router.push('/cate_meta/' + res.data.id);
    toast.success(t('page_common.add_success'));
  }).catch(function(error){
  });

}

function submitUpdate(){
  let id = data.id;

  cateMetaAPI.update(id, data).then(function(res){
    toast.success(t('page_common.add_success'));
    detail.mode = 'read';
  }).catch(function(error){

  })

}

function getAPIDetail(){
  cateMetaAPI.get(userId).then(function(res){
    data.id = res.data.id;
    data.status = res.data.status;
    data.name = res.data.name;
    data.table_meta_id = res.data.table_meta_id;
  }).catch(function(error){
    
  });
}


onMounted(() => {
  if(!isNewPage)
    getAPIDetail();
})


</script>

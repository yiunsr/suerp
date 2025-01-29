<template>
  <div>
    <h2 v-if="isNewPage">
      {{ t("page_col_meta.new_title") }}
    </h2>
    <h2 v-else>
      {{ t("page_col_meta.edit_title") }}
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
              :mode="detail.mode" :i18nValue="false"
              required v-model="data.status" :rules="[rule.req]" />
          </v-col>
          
          <v-col cols="12" md="4">
            <mode-select :label="t('page_col_meta.table_meta_id')" 
              :items="ColMetaTableItems" item-title="str" item-value="value_int"
              :mode="detail.mode" :i18nValue="false"
              v-model="data.table_meta_id"
              required :rules="[rule.req]" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_col_meta.category')" :items="categoryDict[data.table_meta_id]"
              item-value="id" item-title="name"  :i18nValue="false"
              :mode="detail.mode"
              required :rules="[rule.req]" v-model="data.category_meta_id" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_col_meta.column_meta')" 
              :items="ColMetaColumnMetaItems" item-title="title"
              :mode="detail.mode" :i18nValue="false"
              required v-model="data.column_meta" :rules="[rule.req]" />
          </v-col>

          <v-col cols="12" md="8" v-show="data.data_type == 'e' || data.data_type == 'M'">
            <mode-dragable-two-text :label="t('page_col_meta.options_jb')"
              key0="title" key1="value"
              :sub-label0="t('page_col_meta.options_jb_sub_label0')"
              :sub-label1="t('page_col_meta.options_jb_sub_label1')"
              :mode="detail.mode" 
              required v-model="data.options_jb" 
              :rules0="[rule.req]"  :rules1="[rule.req]" />
          </v-col>

          <v-col cols="12" md="4" v-if="detail.mode == 'read'">
            <mode-text-field label="Code" type="text" :mode="detail.mode"
              :counter=16 :readonly="true"
              v-model="data.code"></mode-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_col_meta.data_type')" :items="ColMetaDataTypeItems" 
              :item-props="strSubtitle"
              :mode="detail.mode"
              required v-model="data.data_type" :rules="[rule.req]" />
          </v-col>
          
          <v-col cols="12" md="4">
            <!--
            <mode-text-field label="default_jb" type="text" :mode="detail.mode"
              :counter=16
              v-model="data.default_jb"></mode-text-field>
          -->
            <mode-jsonb-field :label="t('page_col_meta.default_value')" type="text" :mode="detail.mode"
              :counter=16
              v-model="data.default_jb" />
          </v-col>
          <v-col cols="12" md="4">
            <mode-text-field :label="t('page_common.name')" type="text" :mode="detail.mode" 
              :counter=32
              required v-model="data.name"></mode-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <mode-select :label="t('page_col_meta.visible')" :items="ColMetaVisibleItems" 
              item-title="str" item-value="value_int" :i18nValue="false"
              :mode="detail.mode"
              required v-model="data.visible" :rules="[rule.req]" />
          </v-col>
          <v-col cols="12" md="12">
            <mode-text-area :label="t('page_col_meta.detail')" type="text" :mode="detail.mode"
              :counter=128
              :rows="2"
              v-model="data.detail"></mode-text-area>
          </v-col>
          
          <v-col cols="12" md="4">
            <mode-select label="HTML type" :items="ColMetaHTMLTypeItems" item-title="title" 
              :mode="detail.mode" :i18nValue="false"
              required v-model="data.html_type" :rules="[rule.req]" />
          </v-col>

          <v-col cols="12" md="4">
            <mode-text-area label="HTML pattern" type="text" :mode="detail.mode"
              :counter=128 :rows="3"
              v-model="data.html_pattern"></mode-text-area>
          </v-col>

          <v-col cols="12" md="4">
            <mode-text-area label="HTML detail" type="text" :mode="detail.mode"
              :counter=128
              :rows="3"
              v-model="data.html_detail"></mode-text-area>
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
import _ from 'lodash';
import { ref, reactive, watch } from 'vue';
import { toast } from 'vue3-toastify';
import { useStore } from 'vuex';
import { useRoute,  useRouter } from 'vue-router';
import {i18n} from '@/plugins/i18n';
import {utils} from '@/plugins/utils';
import {rule} from '@/js/rule';

import {reverseItem, strSubtitle,
  ColMetaStateItems, ColMetaTableItems, ColMetaColumnMetaItems, 
  ColMetaDataTypeItems, ColMetaVisibleItems, ColMetaHTMLTypeItems} from '@/js/commonValue';
import {colMetaAPI} from '@/api/service/col_meta';
import {categoryMetaAPI} from '@/api/service/category_meta';

import ModeTextField from "@/widgets/ModeTextField";
import ModeTextArea from "@/widgets/ModeTextArea";
import ModeDragableTwoText from "@/widgets/ModeDragableTwoText";
import ModeSelect from "@/widgets/ModeSelect";
import ModeJsonbField from "@/widgets/ModeJsonbField";

import { onMounted, computed } from 'vue';

const store = useStore();
const $route = useRoute();
let $router = useRouter();
let t=i18n.global.t;

const detailForm = ref(null);
const objectID = $route.params.id;

let isNewPage = $route.path.includes("new")?true:false;
let mode = $route.path.includes("new")?"edit":"read";
let detail = reactive({ mode, valid: false });


let data = reactive({
  id: null, status: "A", table_meta_id: null, 
  column_meta: "", data_type: "", code: "", 
  category_meta_id: null,
  name: "", detail: "", visible: null,
  options_jb: [], 
  default_jb: null, 
  html_type: "", html_pattern: "", html_detail: "",
});

let categoryDict = reactive({
  "1": [], "2": [], "3": [], "4": [], "5": [],
})

async function submitAdd(){
  console.log("form valid : " + detail.valid);
  if(!detail.valid){
    await detailForm.value.validate();
    return;
  }
  
  let paramDict = JSON.parse(JSON.stringify(data));
  //paramDict["default_jb"] = JSON.parse(paramDict["default_jb"])
  colMetaAPI.add(paramDict).then(function(res){
    $router.push('/col_meta/' + res.data.id);
    toast.success(t('page_common.add_success'));
  }).catch(function(error){
  });
}

function submitUpdate(){
  let id = data.id;
  let paramDict = JSON.parse(JSON.stringify(data));
  //paramDict["default_jb"] = JSON.parse(paramDict["default_jb"])
  colMetaAPI.update(id, paramDict).then(function(res){
    toast.success(t('page_common.add_success'));
    detail.mode = 'read';
  }).catch(function(error){
  });
}

function getAPIDetail(){
  colMetaAPI.get(objectID).then(function(res){
    data.id = res.data.id;
    data.status = res.data.status;
    data.name = res.data.name;
    data.table_meta_id = res.data.table_meta_id;
    data.category_meta_id = res.data.category_meta_id;
    

    data.data_type = res.data.data_type;
    data.code = res.data.code;
    data.column_meta = res.data.column_meta;
    data.visible = res.data.visible;
    data.default_jb = res.data.default_jb;
    data.detail = res.data.detail;

    data.html_detail = res.data.html_detail;
    data.html_pattern = res.data.html_pattern;
    data.html_type = res.data.html_type;
    

  }).catch(function(error){
  });
}


function getCategoryMetaList(){
  const filter = [];
  const sort = [];
  const limit= 1000;
  categoryMetaAPI.list(filter, sort, 1, limit).then(function(res){
    let groupDict = _.groupBy(res.data.data, "table_meta_id");
    // keep reactive
    for(let key in groupDict){
      categoryDict[key] = groupDict[key];
    }
    
  }).catch(function(error){
  });
}

getCategoryMetaList();
onMounted(() => {
  if(!isNewPage)
    getAPIDetail();
})

</script>

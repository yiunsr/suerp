<template>
  <div>
    <span v-show="mode == 'read'">
      <b class="mr-4">{{ props.label+ (props.required?' ★':'') }} :</b> {{  summary }}
    </span>
    <span v-show="mode == 'edit'">
      <b class="mr-4">{{ props.label+ (props.required?' ★':'') }} :</b> {{  summary }}
      <v-dialog width="800">
        <template v-slot:activator="{ props }">
          <v-btn v-bind="props" text="..." density="comfortable"></v-btn>
        </template>

        <template v-slot:default="{ isActive }">
          <v-form ref="itemForm" validate-on="input" v-model="data.valid">
            <v-card>
              <v-card-text>
                <v-container class="v-card-text mx-0 px-0">
                  <v-row>
                    <v-col cols="4">
                      <v-select densityp="compact" label="type"
                        v-model="data.dataType"
                        :items="['string', 'number', 'true', 'false', 'null']"></v-select>
                    </v-col>
                    <v-col cols="8" v-show="valueShow">
                      <v-text-field v-model="data.dataValue" densityp="compact" :rules="[rule_jsonb_value]"></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions class="float-rightd-flex flex-row-reverse">
                <v-btn variant="tonal" text="close" @click="isActive.value = false"></v-btn>
                <v-btn class="mr-4" variant="tonal" color="primary" text="apply" 
                  @click="updateIData(isActive)"></v-btn>
              </v-card-actions>
            </v-card>
          </v-form>
        </template>
      </v-dialog>
    </span>
  </div>
</template>
  
<script setup>
import _ from 'lodash';
import { reactive, ref, computed, watch } from "vue";
import { useRoute } from 'vue-router';

import {rule} from '@/js/rule';
import {i18n} from '@/plugins/i18n';
let t=i18n.global.t;

function isNumeric(num){
  return !isNaN(num)
}

function rule_jsonb_value(value){
  switch(data.dataType){
    case "true":
    case "false":
    case "null":
      return true;
    case "number":
      if(isNumeric(value))
        return true;
      return t("rule.number");
  }
  return true;
  
}

const props = defineProps({
  required: { type: Boolean, default: false},
  label: { type: String, default: ""},
  mode: { type: String, required: true },
});

const modelValue = defineModel();

function calJsonTypeAndValue(){
  let defaultJsonbType = "null";
  let defaultJsonbValue = "";
  switch (typeof modelValue.value) {
    case "number":
      defaultJsonbType = "number";
      defaultJsonbValue = modelValue.value.toString();
      break;
    case "string":
      defaultJsonbType = "string";
      defaultJsonbValue = modelValue.value.toString();
      break;
    case "boolean":
      if(modelValue.value === true){
        defaultJsonbType = "true";
        defaultJsonbValue = "";
      }
      else{
        defaultJsonbType = "false";
        defaultJsonbValue = "";
      }
      break;
    case "null":
    default:
      defaultJsonbValue = "";
      break;
  }
  return {type: defaultJsonbType, value: defaultJsonbValue};
}

let defaultTypeAndValue = calJsonTypeAndValue();
const data = reactive({
  dataValue: defaultTypeAndValue["value"],
  dataType: defaultTypeAndValue["type"],
  formValid: false,
});

const itemForm = ref(null);
async function updateIData(isActive){
  await itemForm.value.validate();
  if(!data.valid)
    return;
  isActive.value = false;

  const jsonb = getJsonb();
  modelValue.value = jsonb;
}


const summary = computed(() => {
  switch(data.dataType){
    case "string":
      return 'string : "' + (data.dataValue || "").toString() + '"';
    case "number":
      return "number : " + (data.dataValue || 0);
    case "true":
      return "true";
    case "false":
      return "false";
  }
  return "null";
});

const valueShow = computed(() => {
  switch(data.dataType){
    case "string":
    case "number":
      return true;
  }
  return false;
});

function getJsonb(){
  switch(data.dataType){
    case "string":
      return (data.dataValue || "").toString();
    case "number":
      return Number(data.dataValue || 0);
    case "true":
      return true;
    case "false":
      return false;
  }
  return null;
};

watch(() => modelValue, (newValue, oldValue) => {
    let typeAndValue = calJsonTypeAndValue();
    data.dataType = typeAndValue["type"];
    data.dataValue = typeAndValue["value"];
  },
  {deep: true, immediate: true}
)


</script>

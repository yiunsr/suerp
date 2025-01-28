<template>
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
                      v-model="data.modelDataType"
                      :items="['string', 'number', 'true', 'false', 'null']"></v-select>
                  </v-col>
                  <v-col cols="8" v-show="valueShow">
                    <v-text-field v-model="data.modelValue" densityp="compact" :rules="[rule_jsonb_value]"></v-text-field>
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
  switch(data.modelDataType){
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
  modelValue: { type: Object, default: ""},
  label: { type: String, default: ""},
  mode: { type: String, required: true },
});

let defaultJsonbType = "null";
switch (typeof props.modelValue) {
  case "number":
    defaultJsonbType = "number";
    break;
  case "string":
    defaultJsonbType = "string";
    break;
  case "boolean":
    if(props.modelValue === true)
      defaultJsonbType = "true";
    else
      defaultJsonbType = "false";
    break;
  default:
    break;
}


const data = reactive({
  modelValue: props.modelValue,
  modelDataType: defaultJsonbType,
  formValid: false,
});
const itemForm = ref(null);

const $route = useRoute();
const $emit = defineEmits(['update:modelValue']);

const update = (value) => {
  if(props.type == "number"){
    value = (value === '' ? null : value);
  }
}


async function updateIData(isActive){
  await itemForm.value.validate();
  if(!data.valid)
    return;
  isActive.value = false;

  const jsonb = getJsonb();
  $emit('update:modelValue', jsonb);
}


const summary = computed(() => {
  switch(data.modelDataType){
    case "string":
      return "string : " + (data.modelValue || "").toString();
    case "number":
      return "number : " + (data.modelValue || 0);
    case "true":
      return "true";
    case "false":
      return "false";
  }
  return "null";
});

const valueShow = computed(() => {
  switch(data.modelDataType){
    case "string":
    case "number":
      return true;
  }
  return false;
});

function getJsonb(){
  switch(data.modelDataType){
    case "string":
      return (props.modelValue || "").toString();
    case "number":
      return Number(props.modelValue || 0);
    case "true":
      return true;
    case "false":
      return false;
  }
  return null;
};

watch(() => props.modelValue,
  (newValue, oldValue) => {
  },
  {deep: true, immediate: true}
)

watch(() => data,
  (newValue, oldValue) => {
  },
  {deep: true, immediate: true}
)
</script>

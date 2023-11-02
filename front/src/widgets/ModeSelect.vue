<template>
  <div>
    <v-select :label="props.label + (props.required?' ★':'')" 
      :items="i18nItems" v-show="props.mode == 'edit'"
      :model-value="props.modelValue"  
      :required="props.required" density="compact"
      v-bind="$attrs"
    ></v-select>

    <span v-show="mode == 'read'">
      <b class="mr-4">{{ props.label }} :</b>  {{  modelValueLabel }}
    </span>
  </div>
</template>

<script setup>
import {i18n} from '@/plugins/i18n';
import {utils} from '@/plugins/utils';


import { computed } from 'vue';
let t=i18n.global.t;

const props = defineProps({
  required: { type: Boolean, default: false},
  modelValue: { type: String, default: ""},
  label: { type: String, default: ""},
  items: { type: Object, default: []},
  mode: { type: String, required: true }
});
  
const modelValueLabel = computed(() => {
  let item = utils.getItemByValue(props.items, props.modelValue)
  if(item){
    return t(item.title) + "(" + item.value + ")";
  }
  return "";
});

const i18nItems= computed(() => {
  let items = [];
  for(const item of props.items){
    items.push({title: t(item.title) + "(" + item.value + ")", value: item.value})
  }
  return items;
});


</script>

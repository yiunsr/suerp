<template>
  <div>
    <v-select :label="props.label + (props.required?' ★':'')" 
      :items="props.items" v-show="props.mode == 'edit'"
      v-model="modelValue"  
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
import { computed, useAttrs, watch } from 'vue';

const t=i18n.global.t;
const $attrs = useAttrs()


const props = defineProps({
  required: { type: Boolean, default: false},
  label: { type: String, default: ""},
  items: { type: Object, default: []},
  mode: { type: String, required: true },
  i18nValue: { type: Boolean, default: true }
});

const modelValue = defineModel();

const modelValueLabel = computed(() => {
  let debug = $attrs["debug"] || false;
  if(debug)
    debugger;
  let prop_title = $attrs["item-title"] || "title";
  let prop_value = $attrs["item-value"] || "value";
  let item = utils.getItemByValue(props.items, modelValue.value, prop_value)

  if(item){
    let title = item[prop_title];
    if(props.i18nValue){
      title = t(title);
    }
    return title + "(" + item[prop_value] + ")";
  }
  return "";
});


</script>

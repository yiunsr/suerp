<template>
  <span>
    <template v-if="widgetType == 'text'">
      <mode-text-field :mode="props.mode" :label="props.label"></mode-text-field>
    </template>
  </span>
</template>
  
<script setup>
import { computed} from 'vue';

import { ModeTextField } from './ModeTextField';
import { ModeTextArea } from './ModeTextArea';
import { ModeSelect } from './ModeSelect';

const props = defineProps({
  required: { type: Boolean, default: false},
  modelValue: { default: ""},
  dataType: "",
  label: { type: String, default: ""},
  type: { type: String, default: "text"},
  mode: { type: String, required: true },
});


const $emit = defineEmits(['update:modelValue']);
  
  
const update = (value) => {
  if(props.type == "number"){
    value = (value === '' ? null : value);
  }
  $emit('update:modelValue', value);
}

const widgetType = computed(() => {
  switch(props.type){
    case "date":
    case "time":
    case "datetime":
    case "number":
    case "text":
      return "text";
    case "textarea":
      return "textarea"
  }
  return "text";
});
</script>
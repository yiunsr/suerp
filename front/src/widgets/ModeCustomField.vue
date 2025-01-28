<template>
  <span>
    <template v-if="widgetType == 'text'">
      <mode-text-field v-model="modelValue" :mode="props.mode" 
        :label="props.label" :type="props.type"></mode-text-field>
    </template>
  </span>
</template>
  
<script setup>
import { computed} from 'vue';

import ModeTextField from "@/widgets/ModeTextField";
import ModeRadioGroup from "@/widgets/ModeRadioGroup";
import ModeSelect from "@/widgets/ModeSelect";

const props = defineProps({
  required: { type: Boolean, default: false},
  dataType: "",
  label: { type: String, default: ""},
  type: { type: String, default: "text"},
  mode: { type: String, required: true },
});


const modelValue = defineModel({ type: String })

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
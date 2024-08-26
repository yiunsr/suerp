<template>
  <span>
    <v-text-field v-if="mode == 'edit'"
      :type="props.type"
      :model-value="props.modelValue"  density="compact"
      :label="props.label + (props.required?' ★':'')" 
      :required="props.required"
      v-bind="$attrs"
      @update:modelValue="update" 
    ></v-text-field>
    <span v-show="mode == 'read'">
      <b class="mr-4">{{ props.label }} :</b> {{  props.modelValue }}
    </span>
  </span>
</template>

<script setup>
import { useRoute } from 'vue-router';

const props = defineProps({
  required: { type: Boolean, default: false},
  modelValue: { default: ""},
  label: { type: String, default: ""},
  type: { type: String, default: "text"},
  mode: { type: String, required: true }
});

const $route = useRoute();
const $emit = defineEmits(['update:modelValue']);


const update = (value) => {
  if(props.type == "number"){
    value = (value === '' ? null : value);
  }
  $emit('update:modelValue', value);
}
</script>
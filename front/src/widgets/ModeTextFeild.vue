<template>
  <v-text-field v-show="mode == 'edit' || mode == 'new'" 
    :model-value="modelValue"  density="compact"
    :label="label"
    v-bind="$attrs"
    @update:modelValue="v => $emit('update:modelValue', v)" 
  ></v-text-field>
  <span v-show="mode == 'detail'">
    {{ label }}  {{  modelValue }}
  </span>
</template>

<script setup>
import { useRoute } from 'vue-router';

const props = defineProps({
  modelValue: {},
  label: { type: String, default: ""}
});

const $route = useRoute();
let mode = $route.path.includes("new")?"edit":"detail";
  
</script>
<template>
  <v-select label="User" :items="items"></v-select>

  <span v-show="mode == 'detail'">
    {{ label }}  {{  modelValue }}
  </span>
</template>

<script setup>
import { useRoute } from 'vue-router';

const props = defineProps({
  modelValue: {},
  label: { type: String, default: ""},
  items: { type: Object, default: []},
});

const $route = useRoute();
let mode = $route.path.includes("new")?"edit":"detail";
  
</script>

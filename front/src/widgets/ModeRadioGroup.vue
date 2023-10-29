<template>
  <v-radio-group v-model="radios"  v-for="item in items" v-if="mode == 'edit'">
    <template v-slot:label>
      <div>{{ label }}</div>
    </template>
    <v-radio :label="item.label" :value="item.value"></v-radio>
  </v-radio-group>

  <span v-show="mode == 'read'">
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
  
</script>

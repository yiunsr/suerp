<template>
  <span>
    <v-text-field v-if="mode == 'edit'"
      :model-value="props.modelValue"  density="compact"
      :label="props.label"
      v-bind="$attrs"
      @update:modelValue="v => $emit('update:modelValue', v)" 
    ></v-text-field>
    <span v-show="mode == 'read'">
      <b class="mr-4">{{ props.label }} :</b> {{  props.modelValue }}
    </span>
  </span>
</template>

<script setup>
import { useRoute } from 'vue-router';

const props = defineProps({
  modelValue: { type: String, default: ""},
  label: { type: String, default: ""},
  mode: { type: String, required: true }
});

const $route = useRoute();
  
</script>
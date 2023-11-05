<template>
  <span v-show="mode == 'read'">
    <b class="mr-4">{{ props.label + (props.required?' ★':'') }} :</b> {{  summary }}
  </span>
  <span v-show="mode == 'edit'">
    <b class="mr-4">{{ props.label + (props.required?' ★':'') }} :</b> {{  summary }}
    <v-dialog width="600">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" text="..." density="comfortable"></v-btn>
      </template>

      <template v-slot:default="{ isActive }">
        <v-form ref="itemForm" validate-on="input" v-model="data.valid">
          <v-card>
            <v-card-title>
              <span class="mr-4">{{  props.label  }}</span>
              <v-btn variant="tonal" color="primary"  density="compact" icon="mdi-plus"
                @click="addItem"></v-btn>
            </v-card-title>
            <v-card-text>
              <v-container class="v-card-text mx-0 px-0">
                <v-row :dense="true" v-for="(textItem, textItemIdx) in data.textItems" :key="textItemIdx">
                  <v-col cols="1">
                    <v-btn variant="tonal" color="primary"  density="compact" icon="mdi-minus"
                      @click="removeItem(textItemIdx)"></v-btn>
                  </v-col>
                  <v-col cols="4">
                    <v-select density="compact" :label="t('widget.type')" :rules="[rule.req]"
                      :items="[
                        {title: t('widget.type_home'), value: 'home'}, 
                        {title: t('widget.type_work'), value: 'work'}, 
                        {title: t('widget.type_else'), value: 'else'}, 
                      ]" 
                      v-model="data.textItems[textItemIdx].type"
                      @update:modelValue="update">
                    </v-select>
                  </v-col>
                  <v-col cols="7">
                    <v-text-field v-if="mode == 'edit'"
                      :type="props.type"
                       density="compact"
                      :label="props.label + (props.required?' ★':'')" 
                      :required="props.required"
                      :rules="props.rules"
                      v-bind="$attrs"
                      @update:modelValue="update"
                      v-model="data.textItems[textItemIdx].value"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions class="float-rightd-flex flex-row-reverse">
              <v-btn variant="tonal" text="close" @click="isActive.value = false"></v-btn>
              <v-btn class="mr-4" variant="tonal" color="primary" text="apply" 
                @click="updateItem(isActive)"></v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </template>
    </v-dialog>
  </span>
  
  </template>
  
  <script setup>
  import _ from 'lodash';
  import { defineEmits, reactive, ref, computed, watch } from "vue";
  import { useRoute } from 'vue-router';

  import {rule} from '@/js/rule';
  import {i18n} from '@/plugins/i18n';
  let t=i18n.global.t;
  
  const props = defineProps({
    required: { type: Boolean, default: false},
    modelValue: { type: Array, default: []},
    label: { type: String, default: ""},
    type: { type: String, default: "text"},
    mode: { type: String, required: true },
    rules: { default: [] },
  });

  const data = reactive({textItems: [],
    formValid: false,
  });
  const itemForm = ref(null);
  
  const $route = useRoute();
  const $emit = defineEmits(['update:modelValue']);
  
  const update = (value) => {
    if(props.type == "number"){
      value = (value === '' ? null : value);
    }
    //$emit('update:modelValue', value);
  }

  function addItem(){
    data.textItems.push({type: "else", value: ""})
  }
  function removeItem(idx){
    data.textItems.splice(idx, 1);
  }

  async function updateItem(isActive){
    await itemForm.value.validate();
    if(!data.valid)
      return;
    isActive.value = false;
    //props.modelValue = textItems;

    $emit('update:modelValue', data.textItems);
  }

  const summary = computed(() => {
    let values = [];
    for(const item of props.modelValue){
      values.push("(" + t('widget.type_' + item.type) + ")" + item.value);
    }
    return values.join(", ");
  });

  watch(
    () => props.modelValue,
    (newValue, oldValue) => {
      data.textItems = _.cloneDeep(newValue);
    },
    {deep: true, immediate: true}
)
</script>

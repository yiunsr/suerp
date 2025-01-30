<template>
  <div>
    <span v-show="props.mode == 'read'">
      <b class="mr-4">{{ props.label+ (props.required?' ★':'') }} :</b> {{  summary }}
    </span>
    <span v-show="props.mode == 'edit'">
      <b class="mr-4">{{ props.label+ (props.required?' ★':'') }} :</b> {{  summary }}
      <v-dialog width="800">
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
                  <draggable tag="div" :list="data.textItems" class="list-group" handle=".handle" item-key="name">
                    <template #item="{ element, index }">
                      <v-row :dense="true" :key="index" class="mb-n4">
                        <v-col cols="1">
                          <v-btn variant="tonal" color="primary"  density="compact" icon="mdi-swap-vertical"
                            class="handle mt-2"></v-btn>
                        </v-col>
                        <v-col cols="5">
                          <v-text-field v-if="props.mode == 'edit'"
                            :type="props.type0"
                            density="compact"
                            :label="props.subLabel0 + (props.required?' ★':'')" 
                            :required="props.required"
                            :rules="props.rules0"
                            v-model="data.textItems[index].value0"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="5">
                          <v-text-field v-if="props.mode == 'edit'"
                            :type="props.type1"
                            density="compact"
                            :label="props.subLabel1 + (props.required?' ★':'')" 
                            :required="props.required"
                            :rules="props.rules1"
                            v-model="data.textItems[index].value1"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="1">
                          <v-btn variant="tonal" color="primary"  density="compact" icon="mdi-minus"
                            @click="removeItem(index)" class="mt-2"></v-btn>
                        </v-col>
                      </v-row>
                    </template>
                  </draggable>
                </v-container>
              </v-card-text>

              <v-card-text>
                <v-container class="v-card-text mx-0 px-0">
                  <v-row :dense="true" :key="index" class="mb-n4">
                    <v-col cols="12">
                      <v-textarea label="JSON"  
                        density="compact" rows="2"
                        :modelValue="JSON.stringify(modelValue)"
                        @update:modelValue="updateRawJson" />
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
  </div>
</template>
  
<script setup>
import _ from 'lodash';
import draggable from 'vuedraggable'
import { reactive, ref, computed, watch } from "vue";

import {rule} from '@/js/rule';
import {i18n} from '@/plugins/i18n';
let t=i18n.global.t;

const props = defineProps({
  required: { type: Boolean, default: false},
  label: { type: String, default: ""},
  subLabel0: { type: String, default: ""},
  subLabel1: { type: String, default: ""},
  type0: { type: String, default: "text"},
  type1: { type: String, default: "text"},
  key0: { type: String, required: true},
  key1: { type: String, required: true},
  mode: { type: String, required: true },
  rules0: { default: [] },
  rules1: { default: [] },
});

const modelValue = defineModel({ default: [] });


const data = reactive({textItems: [],
  formValid: false,
});
const itemForm = ref(null);


function addItem(){
  data.textItems.push({value0: "", value1: ""});
}
function removeItem(idx){
  data.textItems.splice(idx, 1);
}

function updateRawJson(value){
  let jsonb = "";
  try {
    jsonb = JSON.parse(value);
  } catch (e) {
    return;
  }
  modelValue.value = jsonb;

}

async function updateItem(isActive){
  await itemForm.value.validate();
  if(!data.valid)
    return;
  isActive.value = false;
  
  let items = [];
  const key0 = props.key0;
  const key1 = props.key1;
  for(const item of data.textItems){
    let newItem = {};
    newItem[key0] = item.value0;
    newItem[key1] = item.value1;
    items.push(newItem);
  }
  modelValue.value = items;
}

const summary = computed(() => {
  let sum_text = JSON.stringify(modelValue.value);
  if(props.mode == 'read'){
    return sum_text;
  }

  if(sum_text.length > 31){
    sum_text = sum_text.slice(0, 31);
    sum_text += " ..."
  }
  return sum_text;
});

watch(() => modelValue.value,(newValue, oldValue) => {
    const items = newValue;
    let newItems = [];
    let key0 = props.key0;
    let key1 = props.key1;
    for(const item of items){
      const value0 = item[key0];
      const value1 = item[key1];
      newItems.push({value0, value1});
    }
    data.textItems = newItems;
  },
  {deep: true, immediate: false}
)
</script>

<style scoped>
div:deep(.v-messages__message){
  margin-top: -5px;
}
</style>

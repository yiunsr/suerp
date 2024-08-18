<template>
  <div>
    <table class="header-table">
      <colgroup><col><col><col v-if="props.search"></colgroup>
      <thead>
        <tr>
          <td>
            <div class="text-h5 pa-2">
              {{ props.listTitle }}
            </div>
          </td>
          <td>
            <v-btn v-if="props.addUrl != ''" :to="props.addUrl" density="comfortable" class="ma-1 " size="large" color="blue-darken-4">
              {{ t('page_common.add') }}
            </v-btn>
          </td>
          <td v-if="props.search">
            <v-btn density="compact" class="ma-1" @click="search">
              <v-icon icon="mdi mdi-magnify"  ></v-icon>
            </v-btn>
          </td>
        </tr>
      </thead>
    </table>
  </div>
</template>

<script setup>
import {i18n} from '@/plugins/i18n';

const props = defineProps({
  listTitle: { type: String, default: "", required: true},
  addUrl: { type: String, default: ""},
  search: { type: Boolean, default: true},
});

const emit = defineEmits(['search']);
function search(){
  emit('search')
}


let t=i18n.global.t;

</script>
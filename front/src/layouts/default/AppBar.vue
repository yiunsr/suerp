<template>
  <v-app-bar flat>
    <v-app-bar-title>
      <!-- <v-icon icon="mdi-circle-slice-4" />  -->
      {{ $t('common.title') }}
    </v-app-bar-title>
    <v-spacer></v-spacer>
    <v-btn icon href="https://vuetifyjs.com/en/" target="_blank">
      <v-icon>mdi-help</v-icon>
    </v-btn>
    
    <v-btn icon @click="$emit('show-login-dialog')">
      <v-icon>mdi-login</v-icon>
    </v-btn>

    <v-menu>
      <template v-slot:activator="{ props }">
        <v-btn icon="mdi-translate"  v-bind="props"></v-btn>
      </template>
      <v-list>
        <v-list-item  @click="changeLang('en')">
          <v-list-item-title>English</v-list-item-title>
        </v-list-item>
        <v-list-item  @click="changeLang('ko')">
          <v-list-item-title>한국어</v-list-item-title>
        </v-list-item>
        </v-list>
      </v-menu>

  
  </v-app-bar>
</template>

<script setup>
  import { i18n } from '@/plugins/i18n'
  import {defineEmits} from "vue";


  function changeLang(newLocale){
    i18n.global.locale.value = newLocale;
  }

  const emit = defineEmits([
    'onShowLoginDialog'
  ]);
</script>
